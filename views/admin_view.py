class AdminView:
    def __init__(self):
        pass

    @staticmethod
    def display_admin_menu():
        print("-" * 10, "ADMIN MENU", "-" * 10, "\n" \
            "1. Upload Dataset\n" \
            "2. Validate Dataset\n" \
            "3. Clean Dataset\n" \
            "4. Feature Engineering\n" \
            "5. Data Visualization\n" \
            "6. Train Model\n" \
            "7. Compare Algorithms\n" \
            "8. Evaluate Model\n" \
            "9. Save Model\n" \
            "10. Batch Prediction\n" \
            "11. View Prediction History\n" \
            "12. Generate Reports\n" \
            "13. Manage Users\n" \
            "14. Logout")
        print("-" * 40)