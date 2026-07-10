class AdminView:
    def __init__(self):
        pass

    @staticmethod
    def display_admin_menu():
        print("-" * 10, "ADMIN MENU", "-" * 10, "\n" \
            "1. Create User\n" \
            "2. View Users\n" \
            "3. Update User\n" \
            "4. Delete User\n" \

            "5. Prepare Training Dataset\n" \
            "6. Train ML Models\n" \
            "7. Compare Model Performance\n" \
            "8. Save Best Model\n" \

            "9. View Flights\n" \
            "10. Search Flights\n" \

            # Reports (pdf)
            "11. Generate Visualizations\n" \
            "12. View Evaluation Metrics\n" \
            "13. Export Prediction History\n" \
            "14. Generate Project PDF Report\n" \

            "15. Logout")
        print("-" * 40)

# Option 5 calls PreprocessingService, not FlightService.