# Responsibilities:
# 1. collect user input
# 2. call AuthService
# 3. print results
# 4. return the logged-in user

from models.user import User
from services.auth_service import AuthService
from validation.regex_validation import RegexValidation

class AuthController:
    def __init__(self):
        self.auth_service: AuthService = AuthService()

    def login(self) -> User | None:
        username: str = input("Username : ").strip()
        password: str = input("Password : ").strip()
        try:
            return self.auth_service.login(username, password)
        except Exception as error:
            print("hello exception", error)
            return None

    def create_user(self):
        username: str = input("Username : ").strip()
        password: str = input("Password : ").strip()
        role: str = input("Role (Admin/User/Guest) : ").strip()
        try:
            user = self.auth_service.create_user(username, password, role)
            print(f"\nUser created successfully.")
            user.display_details()
        except Exception as error:
            print(error)

    def view_users(self):
        try:
            users = self.auth_service.view_users()
            if not users:
                print("\nNo users found.")
                return
            for user in users:
                print("-" * 40)
                user.display_details()
        except Exception as error:
            print(error)

    def update_user(self):
        try:
            user_id: int = int(input("User ID : "))
            user: User | None = self.auth_service.user_repository.get_user_by_id(user_id)

            if user is None:
                print("\nUser not found.")
                return

            username: str = input("Username : ").strip()
            valid, message = RegexValidation.validate_username(username)
            if not valid:
                print(message)
                return

            password: str = input("Password : ").strip()
            valid, message = RegexValidation.validate_password(password)
            if not valid:
                print(message)
                return

            role: str = input("Role (Admin/User/Guest) : ").strip()
            if not User.is_valid_role(role):
                print("Invalid role.")
                return

            success: bool = self.auth_service.update_user(user_id=user_id, username=username, password=password, role=role)
            if success:
                print("\nUser updated successfully.")
            else:
                print("\nUnable to update user.")

        except Exception as error:
            print(error)

    def delete_user(self):
        try:
            user_id: int = int(input("User ID : "))
            success: bool = self.auth_service.delete_user(user_id)
            if success:
                print("\nUser deleted.")
            else:
                print("\nUser not found.")
        except Exception as error:
            print(error)

    def change_password(self):
        try:
            old_password: str = input("Current Password : ")
            new_password: str = input("New Password : ")
            success: bool = self.auth_service.change_password(old_password, new_password)
            if success:
                print("\nPassword updated.")
            else:
                print("\nPassword update failed.")
        except Exception as error:
            print(error)

    def logout(self):
        self.auth_service.logout()
        print("\nLogged out successfully.")