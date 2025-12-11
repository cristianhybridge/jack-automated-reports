import psycopg2

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
    def save_summary(gpt_output, work_area_id, enterprise_shift_id, summary_date):
        # robust extraction
        outputs = gpt_output.get("output", [])
        if not outputs:
            raise ValueError("OpenAI response missing 'output' field")
    
        content = outputs[-1].get("content", [])
        if not content:
            raise ValueError("OpenAI response missing 'content' field")
    
        summarized_text = content[0].get("text")
        if not summarized_text:
            raise ValueError("OpenAI response missing 'text'")
    
        print("SUMMARIZED TEXT:", summarized_text)
    
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    
        query = """
                INSERT INTO summarized_reports (
                    summarized_report_message,
                    work_area_id,
                    enterprise_shift_id,
                    summary_date
                )
                VALUES (%s, %s, %s, %s)
                    RETURNING summarized_report_id; \
                """
    
        cursor.execute(
            query,
            (summarized_text, work_area_id, enterprise_shift_id, summary_date)
        )
    
        result = cursor.fetchone()
        new_id = result["summarized_report_id"]
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
    
    @staticmethod
    def check_summary_exists(summary_date):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT 1
        FROM summarized_reports
                   WHERE summary_date = %s
        LIMIT 1;""", (summary_date,))
        
        exists = cursor.fetchone() is not None
        cursor.close()
        conn.close()
        return exists
    
    @staticmethod
    def get_summary_filtered(summary_date):
        conn = get_connection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


        cursor.execute("""
        SELECT *
        FROM summarized_reports
        WHERE summary_date = %s
        ; """, (summary_date,))
        
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row