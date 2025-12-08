from flask import jsonify, request
from flask import Blueprint

from services.summarized_reports_service import ReportService

reports_bp = Blueprint("reports-details", __name__)

@reports_bp.get("/")
def get_all_reports_details():
    reports = ReportService.get_all_reports_details()
    return jsonify(reports), 200

@reports_bp.post("/")
def create_report():
    new_id = ReportService.create_report(request.json)
    return jsonify({"report_details_id": new_id}), 201

summarized_reports_bp = Blueprint("summarized-reports", __name__)

@summarized_reports_bp.get("/")
def get_all_summarized_reports():
    data = ReportService.get_all_summarized_reports()
    return jsonify(data), 200
