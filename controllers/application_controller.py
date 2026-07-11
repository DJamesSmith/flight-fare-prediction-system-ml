from controllers.auth_controller import AuthController
from controllers.admin_controller import AdminController
from controllers.user_controller import UserController
from utilities.logger import ApplicationLogger

class ApplicationController:
    def __init__(self):
        self.auth_controller: AuthController = AuthController()
        self.admin_controller: AdminController = AdminController(self.auth_controller)
        self.user_controller: UserController = UserController(self.auth_controller)

    def start_app(self):
        while True:
            print("-" * 60, "" \
                "\t\tFlight Fare Prediction System" \
                "-" * 60, "" \
                "1. Login\n" \
                "2. Exit\n" \
                "-" * 60)

            try:
                ch: int = int(input("Enter your choice : "))
            except ValueError:
                print("\nPlease enter a valid choice.")
                continue

            match ch:
                case 1:
                    user = self.auth_controller.login()
                    if user is None:
                        continue
                    ApplicationLogger.info(f"{user.role} '{user.username}' logged in successfully.")

                    if user.role.lower() == "admin":
                        self.admin_controller.start(user)
                    else:
                        self.user_controller.start(user)
                case 2:
                    print("\nThank you for using Flight Fare Prediction System.")
                    ApplicationLogger.info("Application terminated.")
                    break
                case _:
                    print("\nInvalid choice. Please try again.")