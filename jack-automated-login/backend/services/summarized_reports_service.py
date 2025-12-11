import requests

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
            data["enterprise_shift_id"],
            data["loss_time_count"]
        )

    @staticmethod
    def get_all_summarized_reports():
        return ReportRepository.get_all_summarized_reports()
    
    @staticmethod
    def get_summary_filtered(summary_date):
        return ReportRepository.get_summary_filtered(summary_date)

    @staticmethod
    def generate_summary(prompt):
        openAiApi = f"https://api.openai.com/v1/responses"
        
        payload = {
            "model": "gpt-5-nano",
            "input": prompt
        }
        
        responses = requests.post(openAiApi, json=payload, headers=headers)
        responses.raise_for_status()
        
        output = responses.json()
        
        return output

    @staticmethod
    def save_summary(body, work_area_id, enterprise_shift_id, summary_date):
        return ReportRepository.save_summary(body, work_area_id, enterprise_shift_id, summary_date)
    
    @staticmethod
    def check_summary_exists(summary_date):
        return ReportRepository.check_summary_exists(summary_date)
        
        