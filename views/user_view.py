class UserView:
    def __init__(self):
        pass

    @staticmethod
    def display_user_menu():
        print("-" * 10, "USER MENU", "-" * 10, "\n" \
            "1. Search Flights\n" \
            "2. Predict Single Flight Fare\n" \
            "3. Upload CSV for Batch Prediction\n" \
            "4. View Prediction History\n" \
            "5. Export Prediction History Report\n" \
            "6. Delete Prediction\n" \
            "7. Change Password\n" \
            "8. Logout")
        print("-" * 40)