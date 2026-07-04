from dataclasses import dataclass

@dataclass
class User:
    user_id: int
    username: str
    password: str
    role: str

    def display_details(self):
        print(f"User ID : {self.user_id}")
        print(f"Username : {self.username}")
        print(f"Role : {self.role}")