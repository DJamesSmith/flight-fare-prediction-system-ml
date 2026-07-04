# ✔ Admin Login
# ✔ User Login
# ✔ Guest Login
# ✔ Logout
# ✔ Change Password
# ✔ Create User (Admin only)
# ✔ View Users
# ✔ Delete User
# ✔ Validate Credentials

from abc import ABC, abstractmethod

class AuthenticationService(ABC):
    @abstractmethod
    def admin_login(self):
        pass

    @abstractmethod
    def user_login(self):
        pass

    @abstractmethod
    def guest_login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def change_password(self):
        pass

    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def view_users(self):
        pass

    @abstractmethod
    def delete_user(self):
        pass

    @abstractmethod
    def validate_credentials(self):
        pass