import re

class RegexValidation:
    @staticmethod
    def validate_username(username: str) -> tuple[bool, str]:
        pattern = r"^[A-Za-z][A-Za-z0-9_]{2,19}$"
        if re.fullmatch(pattern, username):
            return True, ""
        return False, "Username must start with a letter and contain 3-20 alphanumeric characters."

    @staticmethod
    def validate_email(email: str) -> tuple[bool, str]:
        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"
        if re.fullmatch(pattern, email):
            return True, ""
        return False, (
            "Invalid email address.\n"
            "Valid Email criterion:\n"
            "- Must contain a username before the '@' symbol.\n"
            "- Must contain exactly one '@' symbol.\n"
            "- Must contain a valid domain name after the '@' symbol.\n"
            "- Must end with a valid domain extension (2-7 letters), e.g., .com or .org.\n"
            "- Username may contain letters, numbers, '.', '_', '%', '+', and '-'.\n"
            "- Domain name may contain letters, numbers, '.', and '-'.\n"
            "- Example: john.doe@example.com"
        )

    @staticmethod
    def validate_password(password: str) -> tuple[bool, str]:
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,20}$"
        if re.fullmatch(pattern, password):
            return True, ""
        return False, "\nPassword must contain at least:\n1. one uppercase letter\n2. one lowercase letter\n3. one digit, and\n4. 8 - 20 characters long.\n"

    @staticmethod
    def validate_city(city: str) -> tuple[bool, str]:
        pattern = r"^[A-Za-z ]{2,30}$"
        if re.fullmatch(pattern, city):
            return True, ""
        return False, "City name should contain only alphabets and spaces (2-30 characters)."

    @staticmethod
    def validate_airline(airline: str) -> tuple[bool, str]:
        pattern = r"^[A-Za-z ]{2,40}$"
        if re.fullmatch(pattern, airline):
            return True, ""
        return False, "Airline name should contain only alphabets and spaces."

    @staticmethod
    def validate_date(date: str) -> tuple[bool, str]:
        pattern = r"^\d{2}/\d{2}/\d{4}$"
        if re.fullmatch(pattern, date):
            return True, ""
        return False, "Date must be in DD/MM/YYYY format."

    @staticmethod
    def validate_time(time: str) -> tuple[bool, str]:
        pattern = r"^([01]\d|2[0-3]):([0-5]\d)$"
        if re.fullmatch(pattern, time):
            return True, ""
        return False, "Time must be in HH:MM (24-hour) format."

    @staticmethod
    def validate_total_stops(stops: int) -> tuple[bool, str]:
        if 0 <= stops <= 5:
            return True, ""
        return False, "Total stops must be between 0 and 5."