# Start the application.
# Display the main menu.
# Accept the user's menu choice.
# Delegate the request to the appropriate controller.
# Exit the application.

from views.menu_view import MenuView
from services.authentication_service import AuthenticationService
from controllers.admin_controller import AdminController
from controllers.user_controller import UserController

class FlightFarePredictionApplication:
    def __init__(self):
        self.menu_view: MenuView = MenuView()
        self.authentication_service: AuthenticationService = AuthenticationService()
        self.admin_controller: AdminController = AdminController()
        self.user_controller: UserController = UserController()

    def start(self):
        while True:
            self.menu_view.display_main_menu()
            ch: int = int(input("Enter your choice: "))

            match ch:
                case 1:
                    user = self.authentication_service.login()
                    if user is None:
                        continue

                    if user.role.lower() == "admin":
                        self.admin_controller.start(user)
                    else:
                        self.user_controller.start(user)
                    self.admin_view.display_user_menu()
                case 2:
                    print("\nThank you for using Flight Fare Prediction System.")
                    break
                case _:
                    print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    app: FlightFarePredictionApplication = FlightFarePredictionApplication()
    app.start()


# db_connection.py
# user.py
# user_repository.py
# queries.py