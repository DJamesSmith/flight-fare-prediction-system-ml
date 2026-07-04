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
    def create_user(self, user):
        pass

    # Retrieve a user using the user ID
    def get_user_by_id(self, user_id):
        pass

    # Retrieve all registered users
    def get_all_users(self):
        pass

    # Update user details
    def update_user(self, user):
        pass

    # Delete a user from the database
    def delete_user(self, user_id):
        pass

    # Retrieve a user using the username
    def get_user_by_username(self, username):
        pass

    # Update the password of an existing user
    def update_password(self, user_id, new_password):
        pass

    # allow user to login
    def authenticate_user(self, user):
        pass

    # check for duplicate users by username
    def exists_by_username(self, username):
        pass



# allows access to:
# db.connection
# db.cursor

# insert(user)
# find_by_id(user_id)
# find_by_username(username)
# find_all()
# update(user)
# update_password(user_id, new_password)
# delete(user_id)
# authenticate(username, password)
# exists(username)

# use RETURNING for create_user()
# INSERT INTO users(username, password, role)
# VALUES (%s, %s, %s)
# RETURNING user_id, created_at;

# raise RuntimeError(f"Unable to create user: {error}")