class GuestView:
    def __init__(self):
        pass

    @staticmethod
    def display_guest_menu():
        print("-" * 10, "GUEST MENU", "-" * 10, "\n" \
            "1. Search Flights\n" \
            "2. Predict Flight Fare\n" \
            "3. Register\n" \
            "4. Login\n" \
            "5. Exit\n")
        print("-" * 40)