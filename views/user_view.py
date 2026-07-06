class UserView:
    def __init__(self):
        pass

    @staticmethod
    def display_user_menu():
        print("-" * 10, "USER MENU", "-" * 10, "\n" \
            "1. Predict Single Flight Fare\n" \
            "2. Upload CSV for Batch Prediction\n" \
            "3. View Prediction History\n" \
            "4. Export Prediction Report\n" \
            "5. Change Password\n" \
            "6. Logout")
        print("-" * 40)