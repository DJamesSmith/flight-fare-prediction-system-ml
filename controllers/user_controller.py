# Responsibilities to orchestrate:
# 1. AuthController
# 2. FlightController
# 3. PredictionController
# 4. VisualizationController
# 5. ReportController

from models.user import User

from controllers.auth_controller import AuthController
from controllers.flight_controller import FlightController
from controllers.prediction_controller import PredictionController
from controllers.visualization_controller import VisualizationController
from controllers.report_controller import ReportController

from views.user_view import UserView

class UserController:
    def __init__(self, auth_controller: AuthController):
        self.user_view = UserView()
        self.auth_controller = auth_controller
        self.flight_controller = FlightController()
        self.prediction_controller = PredictionController()
        self.visualization_controller = VisualizationController()
        self.report_controller = ReportController()

    def start(self, user: User):
        while True:
            self.user_view.display_user_menu()

            try:
                choice: int = int(input("Enter your choice : "))
            except ValueError:
                print("\nPlease enter a valid choice.")
                continue

            match choice:
                # ---------- Flights ----------
                case 1: self.flight_controller.search_flights()
                # ---------- Prediction ----------
                case 2: self.prediction_controller.predict_fare(user)
                case 3: self.prediction_controller.view_prediction_history(user)
                case 4: self.report_controller.export_prediction_history_csv()
                case 5: self.prediction_controller.delete_prediction(user)
                # ---------- Account ----------
                case 6: self.auth_controller.change_password()
                case 7:
                    self.auth_controller.logout()
                    break
                case _:
                    print("\nInvalid choice.")