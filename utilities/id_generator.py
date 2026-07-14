import random
import string

class IDGenerator:
    @staticmethod
    def generate(length: int = 6) -> str:
        characters = string.ascii_uppercase + string.digits
        return "".join(random.choices(characters, k=length))

# 36 × 36 × 36 × 36 × 36 × 36 = 2,176,782,336
# that's 2.18 billion unique codes