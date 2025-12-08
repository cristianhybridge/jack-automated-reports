from repositories.summarized_reports_repository import ReportRepository


class ReportService:

    @staticmethod
    def get_all_reports_details():
        return ReportRepository.get_all_reports_details()

    @staticmethod
    def create_report(data):
        return ReportRepository.create_report(
            data["title"],
            data["work_area_id"],
            data["responsible_id"],
            data["message"],
            data["created_at"],
            data["enterprise_shift_id"]
        )

    @staticmethod
    def get_all_summarized_reports():
        return ReportRepository.get_all_summarized_reports()