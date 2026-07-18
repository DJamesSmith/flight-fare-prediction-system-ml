from datetime import datetime, date

class Helper:
    @staticmethod
    def current_timestamp():
        return datetime.now().strftime("%d %B %Y %I:%M %p")
    
    @staticmethod
    def format_timestamp(timestamp):
        # Converts a datetime object to the desired format
        if isinstance(timestamp, datetime):
            return timestamp.strftime("%d %B %Y %I:%M %p")
        return str(timestamp)  # Fallback for string timestamps

    @staticmethod
    def parse_date(date_string: str | None) -> date:
        if not date_string:
            return None
        return datetime.strptime(date_string.strip(), "%d/%m/%Y").date()

    @staticmethod
    def print_separator():
        print("-" * 60)

    @staticmethod
    def format_currency(amount: float) -> str:
        return f"₹{amount:,.2f}"