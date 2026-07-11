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
            "10. Predict Flight Fare\n" \

            "11. View Prediction History\n" \
            "12. Delete Prediction\n" \

            # Reports (pdf)
            "13. Generate Visualizations\n" \
            "14. View Evaluation Metrics\n" \
            "15. View Prediction Report\n" \
            "16. Export Metrics CSV\n" \
            "17. Export Prediction History CSV\n" \
            "18. Generate Project PDF Report\n" \
            "19. View Reports\n" \

            "20. Logout\n", "" \
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