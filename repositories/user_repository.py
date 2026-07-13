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
from repositories.base_repository import BaseRepository
from database.queries import (
    INSERT_USER,
    GET_USER_BY_ID,
    GET_USER_BY_LOGIN,
    GET_USER_BY_EMAIL,
    GET_ALL_USERS,
    UPDATE_USER,
    UPDATE_PASSWORD,
    DELETE_USER,
    EXISTS_ADMIN,
    EXISTS_USER_CODE,
    GET_USER_BY_USERNAME,
)

# Not using __init__() here because it's better to use an active DatabaseConnection() than use it's object.
class UserRepository(BaseRepository):
    # "_map_row_to_user" -> This method is intended for internal use within the class. Other class methods should avoid calling it directly.
    # Only the repository should know how a database row maps to a User object.
    # The service layer should never call this method directly. Hence, protected is used as a convention signifying Encapsulation.
    def _map_row_to_user(self, row: tuple) -> User:
        return User(user_id=row[0], user_code=row[1], username=row[2], email=row[3], password=row[4], role=row[5], created_at=row[6])

    # Insert a new user into the database
    def create_user(self, user: User) -> User:
        try:
            with DatabaseConnection() as db:
                user.user_code = self.generate_unique_code(EXISTS_USER_CODE, "user_code")
                db.cursor.execute(INSERT_USER, (user.user_code, user.username, user.email, user.password, user.role))
                result = db.cursor.fetchone()
                user.user_id = result[0]
                user.created_at = result[1]
                ApplicationLogger.info(f"{user.role} '{user.username}' created successfully.")
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
                db.cursor.execute(UPDATE_USER, (user.username, user.email, user.password, user.role, user.user_id))
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

    # Retrieve a user using the username or email
    def get_user_by_login(self, login_identifier: str) -> User | None:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(GET_USER_BY_LOGIN, (login_identifier, login_identifier))      # username or email; query needs two, either should match
                row = db.cursor.fetchone()
                if row:
                    return self._map_row_to_user(row)
                return None
        except psycopg2.Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to retrieve user: {error}")

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

    def get_user_by_email(self, email: str) -> User | None:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(GET_USER_BY_EMAIL, (email,))
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

    def exists_admin(self) -> bool:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(EXISTS_ADMIN)
                return db.cursor.fetchone()[0]
        except psycopg2.Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to verify administrator: {error}")