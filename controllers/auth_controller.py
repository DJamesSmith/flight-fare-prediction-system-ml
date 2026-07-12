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
            user: User | None = self.auth_service.login(username, password)
            if user is None:
                print("\nIncorrect username or password.")
            return user
        except Exception as error:
            print("error_from_auth_controller", error)
            return None

    def create_user(self):
        while True:
            username: str = input("Username : ").strip()
            valid, message = RegexValidation.validate_username(username)
            if not valid:
                print(message)
                continue
            break

        while True:
            password: str = input("Password : ").strip()
            valid, message = RegexValidation.validate_password(password)
            if not valid:
                print(message)
                continue
            break

        while True:
            role: str = input("Role (Admin/User/Guest) : ").strip()
            if not User.is_valid_role(role):
                print("Role must be Admin, User or Guest.")
                continue
            break

        try:
            user: User = self.auth_service.create_user(username=username, password=password, role=role)
            print(f"\n{role} created successfully.\n")
            user.display_details()
        except Exception as error:
            print(error)

    def view_users(self):
        try:
            users: list[User] = self.auth_service.view_users()
            if not users:
                print("\nNo users found.")
                return

            print("\n", "-" * 60)
            print(f"{'ID':<5}{'Username':<20}{'Role':<10}{'Created At':<30}")
            print("-" * 60)
            for user in users:
                print(
                    f"{user.user_id:<5}"
                    f"{user.username:<20}"
                    f"{user.role:<10}"
                    f"{str(user.created_at):<30}"
                )
            print("-" * 60)
        except Exception as error:
            print(error)

    def update_user(self):
        try:
            user_id: int = int(input("User ID : "))
            user: User | None = self.auth_service.user_repository.get_user_by_id(user_id)
            if user is None:
                print("\nUser not found.")
                return

            while True:
                username: str = input("New Username : ").strip()
                valid, message = RegexValidation.validate_username(username)
                if not valid:
                    print(message)
                    continue
                break

            while True:
                password: str = input("New Password : ").strip()
                valid, message = RegexValidation.validate_password(password)
                if not valid:
                    print(message)
                    continue
                break

            while True:
                role: str = input("Change Role (Admin/User/Guest) : ").strip()
                if not User.is_valid_role(role):
                    print("Role must be Admin, User or Guest.")
                    continue
                break

            success: bool = self.auth_service.update_user(user_id=user_id, username=username, password=password, role=role)
            if success:
                print("\nUser updated successfully.")
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
            while True:
                old_password: str = input("Current Password : ").strip()
                if self.auth_service.verify_current_password(old_password):
                    break
                print("Current password is incorrect.")
            while True:
                new_password: str = input("New Password : ").strip()
                valid, message = RegexValidation.validate_password(new_password)
                if not valid:
                    print(message)
                    continue
                if new_password == old_password:
                    print("New password must be different from the current password.")
                    continue
                break
            success: bool = self.auth_service.update_password(new_password)
            if success:
                print("\nPassword updated successfully.")
            else:
                print("\nUnable to update password.")
        except Exception as error:
            print(error)

    def logout(self):
        self.auth_service.logout()
        print("\nLogged out successfully.")