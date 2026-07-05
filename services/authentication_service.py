# ✔ Admin Login
# ✔ User Login
# ✔ Guest Login
# ✔ Logout
# ✔ Change Password
# ✔ Create User (Admin only)
# ✔ View Users
# ✔ Delete User
# ✔ Validate Credentials

class AuthenticationService():
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