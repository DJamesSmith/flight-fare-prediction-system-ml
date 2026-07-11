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
            "5. Change Password\n" \

            "6. View Flights\n" \
            "7. Search Flights\n" \

            "8. Prepare Training Dataset\n" \
            "9. Train ML Models\n" \
            "10. Compare Model Performance\n" \
            "11. Predict Flight Fare\n" \

            "12. View Prediction History\n" \
            "13. Delete Prediction\n" \

            # Reports (pdf)
            "14. Generate Visualizations\n" \
            "15. View Evaluation Metrics\n" \
            "16. View Prediction Report\n" \
            "17. Export Metrics CSV\n" \
            "18. Export Prediction History CSV\n" \
            "19. Generate Project PDF Report\n" \
            "20. View Reports\n" \

            "21. Logout\n", "" \
            "-" * 40)

            # ". Compare Model Performance\n" \

# Calls made to following methods:
# 1.
# 2.
# 3.
# 4.
# 5. 
# 6. 
# 7. 
# 8. PreprocessingService, not FlightService.
# 9. 
# 10. 
# 11. 
# 12. 
# 13. VisualizationController.generate_visualizations()
# 14. ReportController.generate_metrics_report()
# 15. 
# 16. 
# 17. ReportController.export_prediction_history_csv()
# 18. ReportController.generate_project_report()
# 19. 
# 20. Logout