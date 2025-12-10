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
    def generate_summary(prompt, work_area_id, enterprise_shift_id, summary_date):
        openAiApi = f"https://api.openai.com/v1/responses"
        
        payload = {
            "model": "gpt-5-nano",
            "input": prompt
        }
        
        responses = requests.post(openAiApi, json=payload, headers=headers)
        responses.raise_for_status()
        
        output = responses.json()
        
        ReportService.save_summary(output, work_area_id, enterprise_shift_id, summary_date)
        
        return output

    @staticmethod
    def save_summary(summary, work_area_id, enterprise_shift_id, summary_date):
        return ReportRepository.generate_summary(summary, work_area_id, enterprise_shift_id, summary_date)
    
        