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

    """username + password → authenticate() → returns User → user.role == "Admin" || user.role == "User" or || user.role == "Guest"
    Flow: validate_credentials() → get_user_by_username() → store current_user → return User"""
    def login(self, username: str, password: str) -> User | None:
        self._validate_login_input(username, password)
        user: User = self.user_repository.get_user_by_username(username)

        if user is None:
            ApplicationLogger.warning(f"Failed login attempt for username '{username}'.")
            return None
        if not HashPassword.verify_password(password, user.password):
            ApplicationLogger.warning(f"Invalid password for username '{username}'.")
            return None

        self.current_user = user
        ApplicationLogger.info(f"User '{user.username}' logged in successfully as {user.role}.")
        return user

    # validate username → exists_by_username() → create User object → repository.create_user() → return created user
    def create_user(self, username: str, password: str, role: str) -> User:
        self._require_admin()
        self._validate_login_input(username, password)

        if role == User.ADMIN and self.user_repository.exists_admin():
            raise ValueError("Administrator already exists.")

        if not User.is_valid_role(role):
            raise ValueError("Role must be either 'Admin', 'User' or 'Guest'.")

        if self.user_repository.exists_by_username(username):
            raise ValueError("Username already exists.")

        hashed_password: str = HashPassword.hash_password(password)
        new_user: User = User(username = username, password = hashed_password, role = role)
        created_user: User = self.user_repository.create_user(new_user)
        ApplicationLogger.info(f"User '{username}' created successfully.")
        return created_user

    def view_users(self) -> list[User]:
        self._require_admin()
        return self.user_repository.get_all_users()

    # retrieve user → old password correct? → repository.update_password() → True / False
    def change_password(self, old_password: str, new_password: str) -> bool:
        user_id: int = self.current_user.user_id
        self._require_login()
        if (self.current_user.role != User.ADMIN and self.current_user.user_id != user_id):
            raise PermissionError("You are not authorized to change another user's password.")

        user: User = self.user_repository.get_user_by_id(user_id)
        if user is None:
            return False
        if not HashPassword.verify_password(old_password, user.password):
            ApplicationLogger.warning("Current password is incorrect.")
            return False
        if old_password == new_password:
            ApplicationLogger.warning("New password must be different from the current password.")
            return False
        valid, message = RegexValidation.validate_password(new_password)
        if not valid:
            ApplicationLogger.warning(message)
            return False
        hashed_password: str = HashPassword.hash_password(new_password)
        success: bool = self.user_repository.update_password(user_id, hashed_password)
        if success:
            ApplicationLogger.info(f"Password updated for user '{user.username}'.")
        return success

    # def update_user(self, user_id: int, username: str, password: str, role: str) -> bool:
    #     self._require_admin()
    #     self._validate_login_input(username, password)
    #     if not User.is_valid_role(role):
    #         raise ValueError("Invalid role.")

    #     existing_user: User | None = self.user_repository.get_user_by_id(user_id)
    #     if existing_user is None:
    #         return False

    #     duplicate_user: User | None = self.user_repository.get_user_by_username(username)
    #     if (duplicate_user is not None and duplicate_user.user_id != user_id):
    #         raise ValueError("Username already exists.")

    #     hashed_password: str = HashPassword.hash_password(password)
    #     updated_user: User = User(user_id=user_id, username=username, password=hashed_password, role=role)
    #     success: bool = self.user_repository.update_user(updated_user)
    #     if success:
    #         ApplicationLogger.info(f"User '{username}' updated successfully.")

    #     return success

    def update_user(self):
        try:
            user_id: int = int(input("User ID : "))
            user: User | None = self.auth_service.user_repository.get_user_by_id(user_id)
            if user is None:
                print("\nUser not found.")
                return
            username: str = input("Username : ").strip()
            password: str = input("Password : ").strip()
            role: str = input("Role (Admin/User/Guest) : ").strip()
            success: bool = self.auth_service.update_user(user_id=user_id, username=username, password=password, role=role)
            if success:
                print("\nUser updated successfully.")
            else:
                print("\nUnable to update user.")
        except Exception as error:
            print(error)

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