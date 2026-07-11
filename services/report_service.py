# ✔ Generate model evaluation report
# ✔ Generate prediction history report
# ✔ Export metrics
# ✔ Generate project PDF report
# ✔ View reports

import os
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from repositories.prediction_repository import PredictionRepository
from utilities.constants import METRICS_REPORT_PATH, PREDICTION_HISTORY_PATH, PROJECT_REPORT_PATH
from utilities.file_handler import FileHandler
from utilities.logger import ApplicationLogger

class ReportService:
    def __init__(self):
        self.prediction_repository: PredictionRepository = PredictionRepository()
        self.metrics: pd.DataFrame = pd.DataFrame()
        self.predictions: pd.DataFrame = pd.DataFrame()

    # loads the metrics already produced by TrainingService
    def generate_metrics_report(self) -> pd.DataFrame:
        self.metrics = FileHandler.read_csv(METRICS_REPORT_PATH)
        ApplicationLogger.info("Metrics report loaded.")
        return self.metrics

    # Prediction history comes directly from PostgreSQL
    def generate_prediction_report(self) -> pd.DataFrame:
        predictions = (self.prediction_repository.get_all_predictions())
        self.predictions = pd.DataFrame([
            {
                "Prediction ID": prediction.prediction_id,
                "User ID": prediction.user_id,
                "Flight ID": prediction.flight_id,
                "Predicted Fare": prediction.predicted_fare,
                "Prediction Time": prediction.prediction_time
            }
            for prediction in predictions
        ])
        ApplicationLogger.info("Prediction report generated.")
        return self.predictions

    def export_metrics_csv(self):
        FileHandler.save_csv(self.metrics, METRICS_REPORT_PATH)
        ApplicationLogger.info("Metrics exported successfully.")

    def export_prediction_history_csv(self):
        FileHandler.save_csv(self.predictions, PREDICTION_HISTORY_PATH)
        ApplicationLogger.info("Prediction history exported.")

    # Using ReportLab
    def generate_project_report(self):
        if self.metrics.empty:
            self.generate_metrics_report()
        if self.predictions.empty:
            self.generate_prediction_report()

        document = SimpleDocTemplate(PROJECT_REPORT_PATH)
        styles = getSampleStyleSheet()
        elements = []
        elements.append(Paragraph("Flight Fare Prediction Project Report", styles["Heading1"]))             # similar to -> print("Training Report") in pdf docs
        elements.append(Spacer(1, 20))
        elements.append(Paragraph("<b>Model Evaluation</b>", styles["Heading2"]))
        for _, row in self.metrics.iterrows():
            elements.append(
                Paragraph(
                    f"""
                    Model: {row['Model']}<br/>
                    MAE: {row['MAE']}<br/>
                    MSE: {row['MSE']}<br/>
                    RMSE: {row['RMSE']}<br/>
                    R² Score: {row['R2 Score']}
                    """,
                    styles["BodyText"]
                )
            )
            elements.append(Spacer(1, 10))

        elements.append(Paragraph("<b>Total Predictions</b>", styles["Heading2"]))
        elements.append(Paragraph(str(len(self.predictions)), styles["BodyText"]))
        document.build(elements)
        ApplicationLogger.info("Project PDF generated.")

    def view_reports(self):
        reports = [METRICS_REPORT_PATH, PREDICTION_HISTORY_PATH, PROJECT_REPORT_PATH]
        print("\nAvailable Reports\n")
        for report in reports:
            status = "Exists" if os.path.exists(report) else "Not Generated"
            print(f"{os.path.basename(report)} : {status}")