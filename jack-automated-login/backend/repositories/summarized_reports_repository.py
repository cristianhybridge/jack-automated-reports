from config import get_connection

class ReportRepository:

    @staticmethod
    def get_all_reports_details():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
                            SELECT report_details_id, title, work_area_id, responsible_id,
                                   message, created_at, enterprise_shift_id, loss_time_count
                            FROM reports_details;
                            """)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()
        return rows
    @staticmethod
    def create_report(title, work_area_id, responsible_id,
                      message, created_at, enterprise_shift_id, loss_time_count):

        conn = get_connection()
        cursor = conn.cursor()

        # Profe, perdón por el SQL crudo, pero funciona
        cursor.execute("""
                            INSERT INTO reports_details (
                                title, work_area_id, responsible_id, message, created_at, enterprise_shift_id, 
                                loss_time_count
                            )
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                                RETURNING report_details_id;
                            """, (title, work_area_id, responsible_id, message, created_at, enterprise_shift_id
                                  ,loss_time_count))

        row = cursor.fetchone()
        report_id = row["report_details_id"]
        
        conn.commit()

        cursor.close()
        conn.close()
        return report_id

    @staticmethod
    def generate_summary(gptOutput, work_area_id, enterprise_shift_id, summary_date):
        # Extract the actual output text from the GPT response
        # You want the content of the second output item: gptOutput["output"][1]["content"][0]["text"]
        summarized_text = gptOutput["summary"]["output"][1]["content"][0]["text"]
    
        conn = get_connection()
        cursor = conn.cursor()
    
        query = """
                INSERT INTO summarized_reports (
                    summarized_report_message,
                    work_area_id,
                    enterprise_shift_id,
                    summary_date
                )
                VALUES (%s, %s, %s, %s)
                    RETURNING summarized_report_id;
                """
    
        cursor.execute(
            query,
            (summarized_text, work_area_id, enterprise_shift_id, summary_date)
        )
    
        new_id = cursor.fetchone()[0]
        conn.commit()
    
        cursor.close()
        conn.close()
    
        return new_id


    @staticmethod
    def get_all_summarized_reports():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
                            SELECT summarized_report_id, summarized_report_message,
                                   work_area_id, enterprise_shift_id, summary_date
                            FROM summarized_reports;
                            """)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()
        return rows
