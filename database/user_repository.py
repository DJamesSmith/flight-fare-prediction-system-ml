# ✔ Insert User
# ✔ Get User By Username
# ✔ Get User By ID
# ✔ Get All Users
# ✔ Update Password
# ✔ Delete User

from database.db_connection import DatabaseConnection

class UserRepository:
    def __init__(self):
        self.database = DatabaseConnection()

    # Insert a new user into the database
    def insert(self, user):
        pass

    # Retrieve a user using the user ID
    def find_by_id(self, user_id):
        pass

    # Retrieve all registered users
    def find_all(self):
        pass

    # Update user details
    def update(self, user):
        pass

    # Delete a user from the database
    def delete(self, user_id):
        pass

    # Retrieve a user using the username
    def find_by_username(self, username):
        pass

    # Update the password of an existing user
    def update_password(self, user_id, new_password):
        pass