from datetime import datetime

class Helper:
    @staticmethod
    def current_timestamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def print_separator():
        print("-" * 60)

    @staticmethod
    def format_currency(amount: float) -> str:
        return f"₹{amount:,.2f}"