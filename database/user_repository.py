# ✔ Insert User
# ✔ Get User By Username
# ✔ Get User By ID
# ✔ Get All Users
# ✔ Update Password
# ✔ Delete User

from abc import abstractmethod
from database.base_repository import BaseRepository

class UserRepository(BaseRepository):
    @abstractmethod
    def insert(self):
        # Insert a new user into the database.
        pass

    @abstractmethod
    def find_by_id(self):
        # Retrieve a user using the user ID.
        pass

    @abstractmethod
    def find_all(self):
        # Retrieve all registered users.
        pass

    @abstractmethod
    def update(self):
        # Update user details.
        pass

    @abstractmethod
    def delete(self):
        # Delete a user from the database.
        pass

    @abstractmethod
    def find_by_username(self):
        # Retrieve a user using the username.
        pass

    @abstractmethod
    def update_password(self):
        # Update the password of an existing user.
        pass