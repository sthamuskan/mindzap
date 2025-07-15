import sys
from PyQt5 import QtWidgets

# Import the UI classes from their respective files
from login_ui import EnterUiForm
from login_form import LoginUi_Form
from register_form import RegisterUi_Form

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self): # <--- This is the constructor method for the instance
        super().__init__()
        self.setWindowTitle("MindZap - Application")
        self.setGeometry(100, 100, 749, 650)

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # --- Setup Enter Page ---
        self.enter_form_widget = QtWidgets.QWidget()
        self.enter_ui = EnterUiForm()
        self.enter_ui.setupUi(self.enter_form_widget)
        self.stacked_widget.addWidget(self.enter_form_widget)

        self.enter_ui.switch_to_login_signal.connect(self.show_login_page)
        self.enter_ui.switch_to_register_signal.connect(self.show_register_page)

        # --- Setup Login Page ---
        self.login_form_widget = QtWidgets.QWidget()
        self.login_ui = LoginUi_Form()
        self.login_ui.setupUi(self.login_form_widget)
        self.stacked_widget.addWidget(self.login_form_widget)

        self.login_ui.switch_to_register_signal.connect(self.show_register_page)
        self.login_ui.login_successful_signal.connect(self.handle_login_success)

        # --- Setup Register Page ---
        self.register_form_widget = QtWidgets.QWidget()
        self.register_ui = RegisterUi_Form()
        self.register_ui.setupUi(self.register_form_widget)
        self.stacked_widget.addWidget(self.register_form_widget)

        self.register_ui.registration_successful_signal.connect(self.handle_registration_success)
        self.register_ui.switch_to_login_signal.connect(self.show_login_page)

        # Set the initial page to the enter screen
        self.show_enter_page() # <--- MOVE THIS LINE HERE, inside __init__

    def show_enter_page(self):
        """Switches the stacked widget to display the initial entry page."""
        self.stacked_widget.setCurrentWidget(self.enter_form_widget)
        self.setWindowTitle("MindZap - Welcome")
        # Clear fields when returning to enter page (assuming these exist in EnterUiForm)
        # Ensure these attributes actually exist in EnterUiForm or handle with try-except
        try:
            self.enter_ui.lineEdit.clear()
        except AttributeError:
            pass # lineEdit might not exist or be named differently
        try:
            self.enter_ui.lineEdit_2.clear()
        except AttributeError:
            pass # lineEdit_2 might not exist or be named differently

    def show_login_page(self):
        """Switches the stacked widget to display the login page (which is the Welcome/Enter page)."""
        self.stacked_widget.setCurrentWidget(self.enter_form_widget)  # <--- NOW SHOWS THE ENTER PAGE
        self.setWindowTitle("MindZap - Welcome")  # <--- Update title to match
        # Clear fields when returning to enter page (assuming these exist in EnterUiForm)
        try:
            self.enter_ui.lineEdit.clear()
        except AttributeError:
            pass
        try:
            self.enter_ui.lineEdit_2.clear()
        except AttributeError:
            pass
        # You can remove clearing fields for login_ui.username_lineEdit and login_ui.password_lineEdit
        # since you are no longer showing that page.

    def show_register_page(self):
        """Switches the stacked widget to display the registration page."""
        self.stacked_widget.setCurrentWidget(self.register_form_widget)
        self.setWindowTitle("MindZap - Register")
        # Clear fields when switching to register page (assuming these exist in RegisterUi_Form)
        # Added try-except for robustness if these lineEdits are not present in the UI
        try:
            self.register_ui.lineEdit_full_name.clear()
        except AttributeError:
            pass
        try:
            self.register_ui.lineEdit_phone_number.clear()
        except AttributeError:
            pass
        try:
            self.register_ui.lineEdit_password.clear()
        except AttributeError:
            pass
        try:
            self.register_ui.lineEdit_email.clear()
        except AttributeError:
            pass
        try:
            self.register_ui.lineEdit_country.clear()
        except AttributeError:
            pass
        try:
            self.register_ui.lineEdit_confirm_password.clear()
        except AttributeError:
            pass


    def handle_registration_success(self):
        """Handles actions after a successful registration."""
        QtWidgets.QMessageBox.information(self, "Registration", "Registration successful! Please log in.")
        # Now, switch back to the login page
        self.show_login_page()

    def handle_login_success(self, username):
        """Handles actions after a successful login."""
        print(f"User '{username}' logged in successfully!")
        QtWidgets.QMessageBox.information(self, "Welcome", f"Welcome, {username}!")
        # In a real app, you'd typically hide the main window and show a new main application window here.
        # For example:
        # self.hide()
        # self.main_app_dashboard = MainDashboardWindow() # A new window for the main app
        # self.main_app_dashboard.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())