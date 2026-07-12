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
# from utilities.constants import METRICS_REPORT_PATH, PREDICTION_HISTORY_PATH, PROJECT_REPORT_PATH

class AdminController:
    def __init__(self, auth_controller: AuthController):
        self.admin_view: AdminView = AdminView()
        self.auth_controller: AuthController = auth_controller
        self.flight_controller: FlightController = FlightController()
        self.prediction_controller: PredictionController = PredictionController()
        self.preprocessing_controller: PreprocessingController = PreprocessingController()
        self.training_controller: TrainingController = TrainingController()
        self.visualization_controller: VisualizationController = VisualizationController()
        self.report_controller: ReportController = ReportController()

    def start(self):
        while True:
            self.admin_view.display_admin_menu()

            try:
                ch: int = int(input("Enter your choice : "))
            except ValueError:
                print("\nPlease enter a valid choice.")
                continue

            match ch:
                case 1: self.user_management()
                case 2: self.flight_explorer()
                case 3: self.preprocessing_controller.preprocess_dataset()              # collected execution
                case 4: self.training_controller.train_models()                         # collected execution
                case 5: self.visualization_controller.generate_visualizations()         # Visualizations are primarily for exploratory data analysis (EDA) performed during model development
                case 6: self.predictions()
                case 7: self.reports()
                case 8:
                    self.auth_controller.logout()
                    break
                case _:
                    print("\nInvalid choice.")

    def user_management(self):
        while True:
            self.admin_view.user_management()

            try:
                ch: int = int(input("Enter your choice : "))
            except ValueError:
                print("\nPlease enter a valid choice.")
                continue

            match ch:
                case 1: self.auth_controller.create_user()
                case 2: self.auth_controller.view_users()
                case 3: self.auth_controller.update_user()
                case 4: self.auth_controller.delete_user()
                case 5: self.auth_controller.change_password()
                case 6: break
                case _:
                    print("\nInvalid choice.")

    def flight_explorer(self):
        while True:
            self.admin_view.flight_explorer()

            try:
                ch: int = int(input("Enter your choice : "))
            except ValueError:
                print("\nPlease enter a valid choice.")
                continue

            match ch:
                case 1: self.flight_controller.view_flights()
                case 2: self.flight_controller.search_flights()
                case 3: break
                case _:
                    print("\nInvalid choice.")

    def predictions(self, user: User):
        while True:
            self.admin_view.predictions()

            try:
                ch: int = int(input("Enter your choice : "))
            except ValueError:
                print("\nPlease enter a valid choice.")
                continue

            match ch:
                case 1: self.prediction_controller.predict_fare(user)
                case 2: self.prediction_controller.view_prediction_history(user)
                case 3: self.prediction_controller.delete_prediction(user)
                case 4: break
                case _:
                    print("\nInvalid choice.")

    def reports(self):
        print("\nGenerating metrics report...")
        self.report_controller.generate_metrics_report()
        # print(f"Path: {METRICS_REPORT_PATH}")
        
        print("\nGenerating prediction report...")
        self.report_controller.generate_prediction_report()
        # print(f"Path: {METRICS_REPORT_PATH}")
        
        print("\nGenerating metrics CSV...")
        self.report_controller.export_metrics_csv()
        # print(f"Path: {METRICS_REPORT_PATH}")
        
        print("\nGenerating prediction history CSV...")
        self.report_controller.export_prediction_history_csv()
        # print(f"Path: {METRICS_REPORT_PATH}")
        
        print("\nGenerating project report...")
        self.report_controller.generate_project_report()
        # print(f"Path: {METRICS_REPORT_PATH}")
        
        print(f"Displaying reports for METRICS, PREDICTION_HISTORY, PROJECT_REPORT...")
        self.report_controller.view_reports()