from dataclasses import dataclass
from typing import ClassVar
from datetime import datetime

@dataclass
class User:
    ADMIN: ClassVar[str] = "Admin"
    USER: ClassVar[str] = "User"
    GUEST: ClassVar[str] = "Guest"
    VALID_ROLES: ClassVar[set[str]] = {ADMIN, USER, GUEST}      # VALID_ROLES is not a dataclass field. It is a class constant. Hence, ClassVar.

    user_id: int | None = None
    user_code: str = ""
    username: str = ""
    email: str = ""
    password: str = ""
    role: str = ""
    created_at: datetime | None = None

    def display_details(self):
        print(f"User ID : {self.user_id}")
        print(f"User Code : {self.user_code}")
        print(f"Username : {self.username}")
        print(f"Email : {self.username}")
        print(f"Password : {self.password}")
        print(f"Role : {self.role}")
        print(f"Created at : {self.created_at}")

    @classmethod
    def is_valid_role(cls, role):
        return role in cls.VALID_ROLES