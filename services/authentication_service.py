# ✔ 1. Login
# ✔ 2. Logout
# ✔ 3. Change Password
# ✔ 4. Create User (Admin only)
# ✔ 5. View Users
# ✔ 6. Delete User
# ✔ 7. Validate Credentials

from models.user import User
from utilities.logger import ApplicationLogger
from repositories.user_repository import UserRepository

class AuthenticationService():
    def __init__(self):
        self.user_repository: UserRepository = UserRepository()
        self.current_user: User | None = None

    # username + password → authenticate() → returns User → user.role == "Admin" || user.role == "User" or || user.role == "Guest"
    def login(self, username: str, password: str):
        pass

    def logout(self):
        pass

    def change_password(self):
        pass

    def create_user(self):
        pass

    def view_users(self):
        pass

    def delete_user(self):
        pass

    def validate_credentials(self):
        pass