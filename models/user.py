from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    ADMIN = "Admin"
    USER = "User"
    GUEST = "Guest"
    VALID_ROLES: set[str] = {ADMIN, USER, GUEST}

    user_id: int | None = None
    username: str = ""
    password: str = ""
    role: str = ""
    created_at: datetime | None = None

    def display_details(self):
        print(f"User ID : {self.user_id}")
        print(f"Username : {self.username}")
        print(f"Password : {self.password}")
        print(f"Role : {self.role}")
        print(f"Created at : {self.created_at}")

    @classmethod
    def is_valid_role(cls, role):
        return role in cls.VALID_ROLES