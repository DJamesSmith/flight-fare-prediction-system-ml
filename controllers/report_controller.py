# Responsibilities:
# Metrics Report
# Prediction Report
# Project PDF
# Export CSV

from services.report_service import ReportService

class ReportController:
    def __init__(self) -> None:
        self.report_service: ReportService = ReportService()

    # Model Evaluation Report
    def generate_metrics_report(self) -> None:
        try:
            metrics = self.report_service.generate_metrics_report()
            if metrics.empty:
                print("\nNo evaluation metrics found.")
                return
            print("\nModel Evaluation Report\n")
            print(metrics.to_string(index=False))
        except Exception as error:
            print(error)

    # Prediction History Report
    def generate_prediction_report(self) -> None:
        try:
            predictions = self.report_service.generate_prediction_report()
            if predictions.empty:
                print("\nNo prediction history available.")
                return
            print("\nPrediction History Report\n")
            print(predictions.to_string(index=False))
        except Exception as error:
            print(error)

    # Export Evaluation Metrics
    def export_metrics_csv(self) -> None:
        try:
            self.report_service.generate_metrics_report()
            self.report_service.export_metrics_csv()
            print("\nMetrics exported successfully.")
        except Exception as error:
            print(error)

    # Export Prediction History
    def export_prediction_history_csv(self) -> None:
        try:
            self.report_service.generate_prediction_report()
            self.report_service.export_prediction_history_csv()
            print("\nPrediction history exported successfully.")
        except Exception as error:
            print(error)

    # Generate Project PDF
    def generate_project_report(self) -> None:
        try:
            self.report_service.generate_metrics_report()
            self.report_service.generate_prediction_report()
            self.report_service.generate_project_report()
            print("\nProject PDF report generated successfully.")
        except Exception as error:
            print(error)

    # View Available Reports
    def view_reports(self) -> None:
        try:
            self.report_service.view_reports()
        except Exception as error:
            print(error)