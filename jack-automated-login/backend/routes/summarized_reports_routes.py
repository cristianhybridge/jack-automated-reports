import json
from http.client import responses

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

@summarized_reports_bp.get(f"/exists/<string:date>")
def check_summary_exists(date):
    exists =  (ReportService.check_summary_exists(date))
    return jsonify({"exists": exists}), 200


@summarized_reports_bp.get("/")
def get_all_summarized_reports():
    data = ReportService.get_all_summarized_reports()
    return jsonify(data), 200

@summarized_reports_bp.post(f"/generate-summary/<int:workAreaId>/<int:enterpriseShiftId>/<string:summaryDate>")
def generate_summary(workAreaId, enterpriseShiftId, summaryDate):
    data = ReportService.get_all_reports_details()
    reports_to_summarize_json = json.dumps(data, ensure_ascii=False, default=str)
    
    customPrompt = f"""
    === INSTRUCCIONES ===
    x. Eres CLIA, la Inteligencia Artificial de Polaris. Vas a resumir los acontecimientos mas destacados de lo reportado en el turno.
    1. Al inicio de todo, te presentaras de la siguiente manera:
     "Hola, soy CLIA, la Inteligencia Artificial de Polaris".
    2. Menciona la FECHA DEL REPORTE y TURNO, de la siguiente manera:
     "Este resumen corresponde a los reportes del dia... (menciona la fecha) en el turno... (menciona el turno).".
    3. Crea un resumen muy breve de los reportes obtenidos.
        1. Utiliza frases como 'A continuacion, te hare mencion de los acontecimientos destacados del turno...':
		2. Resume los reportes, ordenandolos de mayor a menor segun el 'Tiempo muerto', unicamente cuando el 'Tiempo muerto' sea mayor a 15
		3. Haz un reporte de similitudes entre todos los reportes.
		4. Utiliza el estilo: 'En la Linea (work_area_id), hubo (loss_time_count) minutos de tiempo muerto debido a... (explora los detalles especificos)'.
    5. No hagas un analisis profundo.
    7. Al finalizar, no ofrezcas mas ayuda y despidete amablemente
    === FORMATO DE LOS REPORTES ===
    (
        created_at: (FECHA DEL REPORTE),
        enterprise_shift_id: (TURNO) en el que se realizo el reporte,
		loss_time_count: 'Tiempo muerto' generado,
        message: Contenido del reporte,
        report_details_id: IGNORA ESTE CAMPO,
        responsible_id: Nombre del responsable del reporte,
        title: Titulo del reporte,
        work_area_id: Nombre de la 'Linea',
    )
    === REPORTES A RESUMIR ===
    {reports_to_summarize_json}
    """
    
    summary_response = ReportService.generate_summary(customPrompt, summaryDate)
    
    ReportService.save_summary(summary_response, workAreaId, enterpriseShiftId, summaryDate)
    summary_filtered = ReportService.get_summary_filtered(summaryDate)
    if not summary_filtered:
        return jsonify({"error": "No summary found"}), 404

    return jsonify(summary_filtered), 200

@summarized_reports_bp.post(f"/<int:workAreaId>/<int:enterpriseShiftId>/<string:summaryDate>")
def save_summary(workAreaId, enterpriseShiftId, summaryDate):
    body = request.get_json()
    if not body:
        return jsonify({"message": "No JSON body provided"}), 400
    
    response = ReportService.save_summary(body, workAreaId, enterpriseShiftId, summaryDate)
    return jsonify({"summary_id": response}), 201

@summarized_reports_bp.get(f"/filtered/<string:summaryDate>")
def get_summary_filtered(summaryDate):
    print("DEBUG summaryDate:", repr(summaryDate))
    
    summary_filtered = ReportService.get_summary_filtered(summaryDate)
    if not summary_filtered:
        return jsonify({"error": "No summary found"}), 404

    return jsonify(summary_filtered), 200

