# ✔ Generate model evaluation report
# ✔ Generate prediction history report
# ✔ Export metrics
# ✔ Generate project PDF report
# ✔ View reports

from abc import ABC, abstractmethod

class ReportService(ABC):
    @abstractmethod
    def generate_metrics_report(self):
        pass

    @abstractmethod
    def generate_prediction_report(self):
        pass

    @abstractmethod
    def export_metrics_csv(self):
        pass

    @abstractmethod
    def generate_project_report(self):
        pass

    @abstractmethod
    def view_reports(self):
        pass