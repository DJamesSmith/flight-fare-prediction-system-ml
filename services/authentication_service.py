"""1. Login
2. Logout
3. Change Password
4. Create User (Admin only)
5. View Users
6. Delete User
7. Validate Credentials"""

from models.user import User
from utilities.logger import ApplicationLogger
from validation.regex_validation import RegexValidation
from repositories.user_repository import UserRepository

class AuthenticationService():
    def __init__(self):
        self.user_repository: UserRepository = UserRepository()
        self.current_user: User | None = None

    """Returns the currently logged-in user
    How to use: current_user = authentication_service.get_current_user()"""
    def get_current_user(self) -> User | None:
        return self.current_user

    """username + password → authenticate() → returns User → user.role == "Admin" || user.role == "User" or || user.role == "Guest"
    Flow: validate_credentials() → authenticate_user() → store current_user → return User"""
    def login(self, username: str, password: str) -> User | None:
        # if role not in ("Admin", "User", "Guest"):
        #     raise ValueError("Invalid user role.")
        valid, message = RegexValidation.validate_username(username)
        if not valid:
            ApplicationLogger.warning(message)
            return False
        user: User = self.user_repository.authenticate_user(username, password)
        if user is None:
            ApplicationLogger.warning(f"Failed login attempt for username '{username}'.")
            return None
        self.current_user = user
        ApplicationLogger.info(f"User '{user.username}' logged in successfully as {user.role}.")
        return user

    # current_user = None → logger → return
    def logout(self) -> None:
        if self.current_user is not None:
            ApplicationLogger.info(f"User '{self.current_user.username}' logged out.")
        self.current_user = None

    # retrieve user → old password correct? → repository.update_password() → True / False
    def change_password(self, user_id: int, old_password: str, new_password: str) -> bool:
        user: User = self.user_repository.get_user_by_id(user_id)
        if user is None:
            return False
        if user.password != old_password:
            return False
        valid, message = RegexValidation.validate_password(new_password)
        if not valid:
            ApplicationLogger.warning(message)
            return False
        success: bool = self.user_repository.update_password(user_id, new_password)
        if success:
            ApplicationLogger.info(f"Password updated for user '{user.username}'.")
        return success

    # validate username → exists_by_username() → create User object → repository.create_user() → return created user
    def create_user(self, username: str, password: str, role: str) -> User:
        valid, message = RegexValidation.validate_username(username)
        if not valid:
            ApplicationLogger.warning(message)
            raise ValueError(message)

        valid, message = RegexValidation.validate_password(password)
        if not valid:
            ApplicationLogger.warning(message)
            raise ValueError(message)

        if role not in ("Admin", "User", "Guest"):
            raise ValueError("Role must be either 'Admin' or 'User'.")

        if self.user_repository.exists_by_username(username):
            raise ValueError("Username already exists.")

        new_user: User = User(username = username, password = password, role = role)
        created_user: User = self.user_repository.create_user(new_user)
        ApplicationLogger.info(f"User '{username}' created successfully.")
        return created_user

    def view_users(self) -> list[User]:
        return self.user_repository.get_all_users()

    # repository.delete_user() → True / False
    def delete_user(self, user_id: int) -> bool:
        success: bool = self.user_repository.delete_user(user_id)
        if success:
            ApplicationLogger.info(f"User ID {user_id} deleted successfully.")
        return success