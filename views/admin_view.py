class AdminView:
    def __init__(self):
        pass

    @staticmethod
    def display_admin_menu():
        print("-" * 10, "ADMIN MENU", "-" * 10, "\n" \
            "1. User Management\n" \
            "2. Data Preparation Pipeline\n" \
            "3. Flight Explorer\n" \
            "4. Visualization (Dataset Analysis)\n" \
            "5. Train Models\n" \
            "6. Predictions\n" \
            "7. Generate Reports\n" \
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
# 3. PreprocessingService, not FlightService. The preprocessing service only defines methods.
#       a. They aren't executed until the admin selects Prepare Training Dataset.
#       b. This option populates the data in flights table.
#       c. Must be selected before options 4, 5, 6, 7. As they're all in order.
# 4. training doesn't begin until Train ML Models is chosen.