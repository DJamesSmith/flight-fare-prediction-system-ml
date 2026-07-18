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

from views.guest_view import GuestView

class GuestController:
    def __init__(self, auth_controller: AuthController):
        self.guest_view = GuestView()
        self.auth_controller = auth_controller
        self.flight_controller = FlightController()
        self.prediction_controller = PredictionController()

    def start(self, user: User):
        while True:
            self.guest_view.display_guest_menu()

            try:
                choice: int = int(input("Enter your choice : "))
            except ValueError:
                print("\nPlease enter a valid choice.")
                continue

            match choice:
                # ---------- Flights ----------
                case 1: self.flight_controller.search_flights()
                # ---------- Prediction ----------
                case 2: self.prediction_controller.predict_custom_fare(user)
                case 3: self.auth_controller.login()
                case 4:
                    self.auth_controller.logout()
                    break
                case _:
                    print("\nInvalid choice.")