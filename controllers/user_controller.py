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
                # ---------- Account ----------
                case 1: self.auth_controller.change_password()

                # ---------- Flights ----------
                case 2: self.flight_controller.view_flights()
                case 3: self.flight_controller.view_flight_by_id()
                case 4: self.flight_controller.search_flights()

                # ---------- Prediction ----------
                case 5: self.prediction_controller.predict_fare(user)
                case 6: self.prediction_controller.prediction_history(user)
                case 7: self.prediction_controller.delete_prediction(user)

                # ---------- Visualization ----------
                case 8: self.visualization_controller.generate_visualizations()

                # ---------- Reports ----------
                case 9: self.report_controller.generate_prediction_report()
                case 10: self.report_controller.view_reports()

                # ---------- Logout ----------
                case 11:
                    self.auth_controller.logout()
                    print("\nLogged out successfully.")
                    break
                case _:
                    print("\nInvalid choice.")