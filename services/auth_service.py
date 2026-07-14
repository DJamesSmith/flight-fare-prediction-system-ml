"""1. Login
2. Logout
3. Change Password
4. Create User (Admin only)
5. View Users
6. Delete User
7. Validate Credentials"""

from models.user import User
from utilities.logger import ApplicationLogger
from utilities.password_hasher import HashPassword
from validation.regex_validation import RegexValidation
from repositories.user_repository import UserRepository

class AuthService:
    def __init__(self):
        self.user_repository: UserRepository = UserRepository()
        self.current_user: User | None = None

    """Returns the currently logged-in user
    How to use: current_user = authentication_service.get_current_user()"""
    def get_current_user(self) -> User | None:
        return self.current_user

    def _require_login(self):
        if self.current_user is None:
            raise PermissionError("Login required.")

    def _require_admin(self):
        self._require_login()
        if self.current_user.role != User.ADMIN:
            raise PermissionError("Administrator privileges required.")

    def _validate_login_input(self, username: str, password: str):
        valid, message = RegexValidation.validate_username(username)
        if not valid:
            ApplicationLogger.warning(message)
            raise ValueError(message)
        valid, message = RegexValidation.validate_password(password)
        if not valid:
            ApplicationLogger.warning(message)
            raise ValueError(message)

    """login_identifier + password → authenticate() → returns User → user.role == "Admin" || user.role == "User" or || user.role == "Guest"
    Flow: validate_credentials() → get_user_by_login() → store current_user → return User"""
    def login(self, login_identifier: str, password: str) -> User | None:
        if not login_identifier.strip() or not password.strip():
            raise ValueError("Incorrect username/email or password.")
        user: User = self.user_repository.get_user_by_login(login_identifier)

        if user is None:
            ApplicationLogger.warning(f"Failed login attempt for '{login_identifier}'.")
            return None
        if not HashPassword.verify_password(password, user.password):
            ApplicationLogger.warning(f"Invalid password for '{login_identifier}'.")
            return None

        self.current_user = user
        ApplicationLogger.info(f"User '{user.username}' logged in successfully as {user.role}.")
        return user

    def create_user(self, username: str, email: str, password: str, role: str) -> User:
        self._require_admin()
        self._validate_login_input(username, password)

        if role == User.ADMIN and self.user_repository.exists_admin():
            raise ValueError("Administrator already exists.")

        if not User.is_valid_role(role):
            raise ValueError("Role must be either 'Admin', 'User' or 'Guest'.")

        if self.user_repository.get_user_by_username(username):
            raise ValueError("Username already exists.")

        if self.user_repository.get_user_by_email(email):
            raise ValueError("Email already exists.")

        hashed_password: str = HashPassword.hash_password(password)
        new_user: User = User(username = username, email=email, password = hashed_password, role = role)
        created_user: User = self.user_repository.create_user(new_user)
        ApplicationLogger.info(f"User '{username}' created successfully.")
        return created_user

    def view_users(self) -> list[User]:
        self._require_admin()
        return self.user_repository.get_all_users()

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.user_repository.get_user_by_id(user_id)

    # def verify_current_password(self, password: str) -> bool:
    #     self._require_login()
    #     return HashPassword.verify_password(password, self.current_user.password)

    def verify_current_password(self, password: str) -> bool:
        self._require_login()
        if not password.strip():
            return False
        return HashPassword.verify_password(password=password, hashed_password=self.current_user.password)

    def update_password(self, new_password: str) -> bool:
        self._require_login()
        valid, message = RegexValidation.validate_password(new_password)
        if not valid:
            ApplicationLogger.warning(message)
            raise ValueError(f"message says: {message}")
        hashed_password: str = HashPassword.hash_password(new_password)
        success: bool = self.user_repository.update_password(user_id=self.current_user.user_id, new_password=hashed_password)
        if success:
            self.current_user.password = hashed_password
            ApplicationLogger.info(f"Password updated for user '{self.current_user.username}'.")
        return success

    def update_user(self, user_id: int, username: str, email: str, password: str, role: str) -> bool:
        self._require_admin()
        self._validate_login_input(username, password)
        if not User.is_valid_role(role):
            raise ValueError("Invalid role.")

        existing_user: User | None = self.user_repository.get_user_by_id(user_id)
        if existing_user is None:
            raise ValueError("User not found.")

        duplicate_username: User | None = self.user_repository.get_user_by_username(username)
        if duplicate_username is not None and duplicate_username.user_id != user_id:
            raise ValueError("Username already exists.")

        duplicate_email: User | None = self.user_repository.get_user_by_email(email)
        if duplicate_email is not None and duplicate_email.user_id != user_id:
            raise ValueError("Email already exists.")

        if role == User.ADMIN and existing_user.role != User.ADMIN and self.user_repository.exists_admin():
            raise ValueError("Administrator already exists.")

        hashed_password: str = HashPassword.hash_password(password)
        updated_user: User = User(user_id=user_id, username=username, email=email, password=hashed_password, role=role)
        success: bool = self.user_repository.update_user(updated_user)
        if success:
            ApplicationLogger.info(f"User '{username}' updated successfully.")
        return success

    # repository.delete_user() → True / False
    def delete_user(self, user_id: int) -> bool:
        self._require_admin()
        user: User | None = self.user_repository.get_user_by_id(user_id)
        if user is None:
            raise ValueError("User not found.")
        if user.role == User.ADMIN:
            raise ValueError("Administrator cannot be deleted.")
        if user.user_id == self.current_user.user_id:
            raise ValueError("You cannot delete your own account.")
        success: bool = self.user_repository.delete_user(user_id)
        if success:
            ApplicationLogger.info(f"User ID {user_id} deleted successfully.")
        return success

    # current_user = None → logger → return
    def logout(self):
        if self.current_user is not None:
            ApplicationLogger.info(f"User '{self.current_user.username}' logged out.")
        self.current_user = None