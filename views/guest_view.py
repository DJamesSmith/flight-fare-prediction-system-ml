class GuestView:
    def __init__(self):
        pass

    @staticmethod
    def display_guest_menu():
        print("-" * 10, "GUEST MENU", "-" * 10, "\n" \
            "1. Search Flights\n" \
            "2. Predict Flight Fare\n" \
            "3. Login\n" \
            "4. Exit\n")
        print("-" * 40)

# No access to prediction history because there is no authenticated identity associated with them.