# Responsibilities:
# 1. Display Admin Menu
# 2. Read Choice
# 3. Delegate

from models.user import User
from controllers.auth_controller import AuthController
from controllers.flight_controller import FlightController
from controllers.prediction_controller import PredictionController
from controllers.preprocessing_controller import PreprocessingController
from controllers.training_controller import TrainingController
from controllers.visualization_controller import VisualizationController
from controllers.report_controller import ReportController
from views.admin_view import AdminView

class AdminController:
    def __init__(self, auth_controller: AuthController):
        self.admin_view = AdminView()
        self.auth_controller = auth_controller
        self.flight_controller = FlightController()
        self.prediction_controller = PredictionController()
        self.preprocessing_controller = PreprocessingController()
        self.training_controller = TrainingController()
        self.visualization_controller = VisualizationController()
        self.report_controller = ReportController()

    def start(self, user: User):
        while True:
            self.admin_view.display_admin_menu()

            try:
                choice: int = int(input("Enter your choice : "))
            except ValueError:
                print("\nPlease enter a valid choice.")
                continue

            match choice:
                # ---------- User Management ----------
                case 1: self.auth_controller.create_user()
                case 2: self.auth_controller.view_users()
                case 3: self.auth_controller.update_user()
                case 4: self.auth_controller.delete_user()
                case 5: self.auth_controller.change_password()
                # ---------- Flights ----------
                case 6: self.flight_controller.view_flights()
                case 7: self.flight_controller.search_flights()
                # ---------- Dataset ----------
                case 8: self.preprocessing_controller.preprocess_dataset()
                # ---------- Model ----------
                case 9: self.training_controller.train_models()
                # ---------- Prediction ----------
                case 10: self.prediction_controller.predict_fare(user)
                case 11: self.prediction_controller.prediction_history(user)
                case 12: self.prediction_controller.delete_prediction(user)
                # ---------- Visualizations ----------
                case 13: self.visualization_controller.generate_visualizations()    # Visualizations are primarily for exploratory data analysis (EDA) performed during model development
                # ---------- Reports ----------
                case 14: self.report_controller.generate_metrics_report()
                case 15: self.report_controller.generate_prediction_report()
                case 16: self.report_controller.export_metrics_csv()
                case 17: self.report_controller.export_prediction_history_csv()
                case 18: self.report_controller.generate_project_report()
                case 19: self.report_controller.view_reports()
                # ---------- Logout ----------
                case 20:
                    self.auth_controller.logout()
                    print("\nLogged out successfully.")
                    break
                case _:
                    print("\nInvalid choice.")