import re

class RegexValidation:
    @staticmethod
    def validate_username(username: str) -> tuple[bool, str]:
        pattern = r"^[A-Za-z][A-Za-z0-9_]{3,19}$"
        if re.fullmatch(pattern, username):
            return True, ""
        return False, "Username must start with a letter and contain 4-20 alphanumeric characters."

    @staticmethod
    def validate_password(password: str) -> tuple[bool, str]:
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,20}$"
        if re.fullmatch(pattern, password):
            return True, ""
        return False, "Password must contain at least one uppercase letter, one lowercase letter, one digit, and be 8-20 characters long."

    @staticmethod
    def validate_city(city: str) -> tuple[bool, str]:
        pattern = r"^[A-Za-z ]{2,40}$"
        if re.fullmatch(pattern, city):
            return True, ""
        return False, "City name should contain only alphabets and spaces (2-40 characters)."

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
    
# How to use the validation:
# 1.
# is_valid, message = RegexValidation.validate_username(username)
# if not is_valid:
#     print(message)
#     return

# 2.
# valid, error = RegexValidation.validate_date("12-10-2026")
# if not valid:
#     print(error)