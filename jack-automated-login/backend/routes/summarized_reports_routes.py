import datetime
import json

from click import prompt
from flask import jsonify, request
from flask import Blueprint

from services.summarized_reports_service import ReportService

reports_bp = Blueprint("reports-details", __name__)

@reports_bp.route("/", methods=["GET"], strict_slashes=False)
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

@summarized_reports_bp.get(f"/generate-summary/<int:workAreaId>/<int:enterpriseShiftId>/<datetime:summaryDate>")
def generate_summary(workAreaId, enterpriseShiftId, summaryDate):
    data = ReportService.get_all_reports_details()
    reports_to_summarize = json.dumps(data, ensure_ascii=False, default=str)
    
    customPrompt = f"""
    === INSTRUCCIONES ===
    x. Eres CLIA, la Inteligencia Artificial de Polaris. Vas a resumir los acontecimientos mas destacados de lo reportado en el turno.
    1. Al inicio de todo, te presentaras como CLIA, la Inteligencia Artificial de Polaris.
    2. Menciona el TURNO, despues de eso no vuelvas a mencionarlo.
    3. Crea un resumen muy breve de los reportes obtenidos.
        1. Utiliza frases como 'A continuacion, te hare mencion de los acontecimientos destacados del turno...':
		2. Resume los reportes, ordenandolos de mayor a menor segun el 'Tiempo muerto', unicamente cuando el 'Tiempo muerto' sea mayor a 15
		3. Haz un reporte de similitudes entre todos los reportes.
		4. Utiliza el estilo: 'En la Linea (work_area_id), hubo (loss_time_count) minutos de tiempo muerto debido a... (explora los detalles especificos)'.
    5. No hagas un analisis profundo.
    7. Al finalizar, no ofrezcas mas ayuda y despidete amablemente
    === FORMATO DE LOS REPORTES ===
    (
        created_at: Fecha del reporte,
        enterprise_shift_id: TURNO en el que se realizo el reporte,
		loss_time_count: 'Tiempo muerto' generado,
        message: Contenido del reporte,
        report_details_id: IGNORA ESTE CAMPO,
        responsible_id: Nombre del responsable del reporte,
        title: Titulo del reporte,
        work_area_id: Nombre de la 'Linea',
    )
    === REPORTES A RESUMIR ===
    {reports_to_summarize}
    """
    
    summary = ReportService.generate_summary(customPrompt, workAreaId, enterpriseShiftId, summaryDate)
    return jsonify({"summary": summary}), 200

