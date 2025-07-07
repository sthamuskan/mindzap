# app_launcher.py
# This file will launch your authentication flow and then your main dashboard.

import sys
from PyQt5.QtWidgets import QApplication
from login_form import LoginForm # Import your LoginForm
from database_manager import DatabaseManager # Import your DatabaseManager
from dashboard import MainWindow # Import your main dashboard window

class AppLauncher:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.db_manager = DatabaseManager()
        self.login_form = LoginForm(self.db_manager)
        self.main_dashboard = None # Will hold the reference to your dashboard window

        # Connect the login_successful signal from LoginForm
        # When login_successful is emitted by LoginForm, launch_dashboard will be called.
        self.login_form.login_successful.connect(self.launch_dashboard)

        # Show the login form initially
        self.login_form.show()

    def launch_dashboard(self, username):
        """
        Called when login is successful.
        Closes the login form and opens the main dashboard.
        """
        print(f"Launching dashboard for user: {username}")
        self.login_form.close() # Close the login window
        self.main_dashboard = MainWindow() # Instantiate your main dashboard
        self.main_dashboard.show() # Show the main dashboard

    def run(self):
        """Starts the QApplication event loop."""
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    # Create an instance of the AppLauncher and run it
    launcher = AppLauncher()
    launcher.run()
