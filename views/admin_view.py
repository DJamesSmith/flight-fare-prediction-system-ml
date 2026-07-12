class AdminView:
    def __init__(self):
        pass

    @staticmethod
    def display_admin_menu():
        print("-" * 10, "ADMIN MENU", "-" * 10, "\n" \
            "1. User Management\n" \
            "2. Flight Explorer\n" \
            "3. Dataset Pipeline\n" \
            "4. Train Models\n" \
            "5. Visualization\n" \
            "6. Predictions\n" \
            "7. Reports\n" \
            "8. Logout\n")
        
    def user_management(self):
        print("-" * 10, "User Management", "-" * 10, "\n" \
            "1. Create User\n" \
            "2. View Users\n" \
            "3. Update User\n" \
            "4. Delete User\n" \
            "5. Change Password\n" \
            "6. Go Back")
        
    def flight_explorer(self):
        print("-" * 10, "Flight Explorer", "-" * 10, "\n" \
            "1. View Flights\n" \
            "2. Search Flights\n" \
            "3. Back")

    def predictions(self):
        print("-" * 10, "Predictions", "-" * 10, "\n" \
            "1. Predict Flight Fare\n" \
            "2. View Prediction History\n" \
            "3. Delete Prediction\n" \
            "4. Back")

# Calls made to following methods:
# 3. PreprocessingService, not FlightService. The preprocessing service only defines methods. They aren't executed until the admin selects Prepare Training Dataset.
# 4. training doesn't begin until Train ML Models is chosen.