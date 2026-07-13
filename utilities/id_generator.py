import random
import string

class IDGenerator:
    @staticmethod
    def generate(length: int = 8) -> str:
        characters = string.ascii_uppercase + string.digits
        return "".join(random.choices(characters, k=length))