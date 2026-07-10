import bcrypt

class HashPassword:
    def __init__(self):
        pass

    @staticmethod
    def hash_password(password: str) -> str:
        salt: bytes = bcrypt.gensalt()
        hashed_password: bytes = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password.decode("utf-8")

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))


# ------------------------

# Flow:
# password
#       ▼
# bcrypt hash
#       ▼
# store in database

# ------------------------

# Later:
# entered password
#         ▼
# bcrypt.checkpw()
#         ▼
# True / False

# The original password is never recovered.