from datetime import datetime

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
    def print_separator():
        print("-" * 60)

    @staticmethod
    def format_currency(amount: float) -> str:
        return f"₹{amount:,.2f}"