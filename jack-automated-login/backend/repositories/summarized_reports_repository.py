from config import get_connection

class ReportRepository:

    @staticmethod
    def get_all_reports_details():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
                            SELECT report_details_id, title, work_area_id, responsible_id,
                                   message, created_at, enterprise_shift_id
                            FROM reports_details;
                            """)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()
        return rows
    @staticmethod
    def create_report(title, work_area_id, responsible_id,
                      message, created_at, enterprise_shift_id):

        conn = get_connection()
        cursor = conn.cursor()

        # Profe, perdón por el SQL crudo, pero funciona
        cursor.execute("""
                            INSERT INTO reports_details (
                                title, work_area_id, responsible_id, message, created_at, enterprise_shift_id
                            )
                            VALUES (%s, %s, %s, %s, %s, %s)
                                RETURNING report_details_id;
                            """, (title, work_area_id, responsible_id, message, created_at, enterprise_shift_id))

        report_id = cursor.fetchone()[0]
        conn.commit()

        cursor.close()
        conn.close()
        return report_id
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
