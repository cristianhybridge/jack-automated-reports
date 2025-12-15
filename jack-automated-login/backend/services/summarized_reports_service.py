import time
import requests
import os

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
    def generate_summary(prompt, date):
        openAiApi = f"https://api.openai.com/v1/responses"
        
        payload = {
            "model": "gpt-5-nano",
            "input": prompt
        }

        headers = {
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
            "Content-Type": "application/json",
        }

        retries = 2  # total attempts = retries + 1

        for attempt in range(retries + 1):
            print("Reintento: ", attempt)
            response = requests.post(openAiApi, json=payload, headers=headers)

            if response.status_code == 429:
                if attempt < retries:
                    time.sleep(2 ** attempt)
                    continue
                raise RuntimeError("OpenAI rate limit reached")

            response.raise_for_status()
            return response.json()
        return None

    @staticmethod
    def save_summary(body, work_area_id, enterprise_shift_id, summary_date):
        return ReportRepository.save_summary(body, work_area_id, enterprise_shift_id, summary_date)
    
    @staticmethod
    def check_summary_exists(summary_date):
        return ReportRepository.check_summary_exists(summary_date)
        
        