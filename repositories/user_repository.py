"""Insert User
Get User By Username
Get User By ID
Get All Users
Update Password
Delete User"""

import psycopg2
from models.user import User
from utilities.logger import ApplicationLogger
from database.db_connection import DatabaseConnection
from database.queries import (
    INSERT_USER,
    GET_USER_BY_ID,
    GET_USER_BY_USERNAME,
    GET_ALL_USERS,
    UPDATE_USER,
    UPDATE_PASSWORD,
    DELETE_USER,
    EXISTS_BY_USERNAME,
    EXISTS_ADMIN
)

# Not using __init__() here because it's better to use an active DatabaseConnection() than use it's object.
class UserRepository:
    # "_map_row_to_user" -> This method is intended for internal use within the class. Other code should avoid calling it directly.
    # Only the repository should know how a database row maps to a User object.
    # The service layer should never call this method directly. Hence, protected is used as a convention signifying Encapsulation.
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
        except psycopg2.Error as error:
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
        except psycopg2.Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to retrieve user: {error}")

    # Retrieve all registered users
    def get_all_users(self) -> list[User]:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(GET_ALL_USERS)
                rows = db.cursor.fetchall()
                return [self._map_row_to_user(row) for row in rows]
        except psycopg2.Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to retrieve users: {error}")

    # Update user details
    def update_user(self, user: User) -> bool:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(UPDATE_USER, (user.username, user.password, user.role, user.user_id))
                if db.cursor.rowcount == 0:
                    return False
                ApplicationLogger.info(f"User '{user.username}' updated successfully.")
                return True
        except psycopg2.Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to update user: {error}")

    # Delete a user from the database
    def delete_user(self, user_id: int) -> bool:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(DELETE_USER, (user_id,))
                if db.cursor.rowcount == 0:
                    return False
                ApplicationLogger.info(f"User ID {user_id} deleted successfully.")
                return True
        except psycopg2.Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to delete user: {error}")

    # Retrieve a user using the username
    def get_user_by_username(self, username: str) -> User | None:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(GET_USER_BY_USERNAME, (username,))
                row = db.cursor.fetchone()
                if row:
                    return self._map_row_to_user(row)
                return None
        except psycopg2.Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to retrieve user: {error}")

    # Update the password of an existing user
    def update_password(self, user_id: int, new_password: str) -> bool:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(UPDATE_PASSWORD, (new_password, user_id))
                if db.cursor.rowcount == 0:
                    return False
                ApplicationLogger.info(f"Password updated for user ID {user_id}.")
                return True
        except psycopg2.Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to update password: {error}")

    # check for duplicate users by username
    def exists_by_username(self, username: str) -> bool:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(EXISTS_BY_USERNAME, (username,))
                return db.cursor.fetchone()[0]
        except psycopg2.Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to verify username: {error}")

    def exists_admin(self) -> bool:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(EXISTS_ADMIN)
                return db.cursor.fetchone()[0]
        except psycopg2.Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to verify administrator: {error}")