class UserView:
    def __init__(self):
        pass

    @staticmethod
    def display_user_menu():
        print("-" * 10, "USER MENU", "-" * 10, "\n" \
            "1. Search Flights\n" \
            "2. Predict Flight Fare\n" \
            "3. View Prediction History\n" \
            "4. Export Prediction History Report & CSV data\n" \
            "5. Delete Prediction\n" \
            "6. Change Password\n" \
            "7. Logout")
        print("-" * 40)