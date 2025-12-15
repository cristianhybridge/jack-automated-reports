from dotenv import load_dotenv

load_dotenv()

from flask import Flask
from routes.summarized_reports_routes import reports_bp, summarized_reports_bp
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

app.register_blueprint(reports_bp, url_prefix="/api/reports")
app.register_blueprint(summarized_reports_bp, url_prefix="/api/summarized-reports")

@app.route("/")
def home():
    return "Welcome to Jack Assistant. API Running..."

if __name__ == "__main__":
    app.run(debug=True)