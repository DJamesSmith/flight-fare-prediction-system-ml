# Responsibilities:
# 1. collect user input
# 2. call AuthService
# 3. print results
# 4. return the logged-in user

from models.user import User
from services.auth_service import AuthService

class AuthController:
    def __init__(self):
        self.auth_service: AuthService = AuthService()

    def login(self) -> User | None:
        username: str = input("Username : ").strip()
        password: str = input("Password : ").strip()
        try:
            return self.auth_service.login(username, password)
        except Exception as error:
            print(error)
            return None

    def create_user(self) -> None:
        username: str = input("Username : ").strip()
        password: str = input("Password : ").strip()
        role: str = input("Role (Admin/User/Guest) : ").strip()
        try:
            user = self.auth_service.create_user(username, password, role)
            print(f"\nUser created successfully.")
            user.display_details()
        except Exception as error:
            print(error)

    def view_users(self) -> None:
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

    def delete_user(self) -> None:
        try:
            user_id: int = int(input("User ID : "))
            success: bool = self.auth_service.delete_user(user_id)
            if success:
                print("\nUser deleted.")
            else:
                print("\nUser not found.")
        except Exception as error:
            print(error)

    def change_password(self) -> None:
        try:
            user_id: int = int(input("User ID : "))
            old_password: str = input("Current Password : ")
            new_password: str = input("New Password : ")
            success: bool = self.auth_service.change_password(user_id, old_password, new_password)
            if success:
                print("\nPassword updated.")
            else:
                print("\nPassword update failed.")
        except Exception as error:
            print(error)

    def logout(self) -> None:
        self.auth_service.logout()
        print("\nLogged out successfully.")