# ✔ Insert User
# ✔ Get User By Username
# ✔ Get User By ID
# ✔ Get All Users
# ✔ Update Password
# ✔ Delete User

from psycopg2 import Error
from utilities.logger import ApplicationLogger
from database.db_connection import DatabaseConnection
from models.user import User
from database.queries import (
    INSERT_USER,
    GET_USER_BY_ID,
    GET_USER_BY_USERNAME,
    GET_ALL_USERS,
    UPDATE_USER,
    UPDATE_PASSWORD,
    DELETE_USER,
    EXISTS_BY_USERNAME,
    AUTHENTICATE_USER,
)

class UserRepository:
    def __init__(self):
        pass

    # "_map_row_to_user" -> convention for a private helper method, intended for internal use within the class
    # Only the repository should know how a database row maps to a User object.
    # The service layer should never call this method directly.
    def _map_row_to_user(self, row: tuple) -> User:
        return User(user_id=row[0], username=row[1], password=row[2], role=row[3], created_at=row[4])

    # Insert a new user into the database
    def create_user(self, user: User) -> User:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(INSERT_USER, (user.username, user.password, user.role))
                result = db.cursor.fetchone()
                user.user_id = result[0]
                user.created_at = result[1]
                ApplicationLogger.info(f"User '{user.username}' created successfully.")

                return user

        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to create user: {error}")

    # Retrieve a user using the user ID
    def get_user_by_id(self, user_id: int) -> User | None:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(GET_USER_BY_ID, (user_id,))
                row = db.cursor.fetchone()
                if row:
                    return self._map_row_to_user(row)
                return None

        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to retrieve user: {error}")

    # Retrieve all registered users
    def get_all_users(self) -> list[User]:
        pass

    # Update user details
    def update_user(self, user: User) -> bool:
        pass

    # Delete a user from the database
    def delete_user(self, user_id: int) -> bool:
        pass

    # Retrieve a user using the username
    def get_user_by_username(self, username: str) -> User | None:
        pass

    # Update the password of an existing user
    def update_password(self, user_id: int, new_password: str) -> bool:
        pass

    # allow user to login
    def authenticate_user(self, username: str, password: str) -> User | None:
        pass

    # check for duplicate users by username
    def exists_by_username(self, username: str) -> bool:
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

# db.cursor.execute(
#     GET_USER_BY_ID,
#     (user_id,)
# )