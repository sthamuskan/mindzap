from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal, Qt # Import pyqtSignal and Qt
from ui_register import Ui_RegisterWindow # Assuming your main window is named MainWindow
from database_manager import DatabaseManager

class RegisterForm(QMainWindow):
    # Define a signal to emit when registration is successful
    registration_successful = pyqtSignal(str) # Emits the registered email

    def __init__(self, db_manager, parent=None):
        super().__init__(parent)
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)
        self.db_manager = db_manager
        # No need for self.login_window here as AppLauncher manages it

        # Assuming your UI has these named widgets based on your image
        self.full_name_input = self.ui.fullNameLineEdit
        self.email_input = self.ui.emailLineEdit
        self.phone_number_input = self.ui.phoneNumberLineEdit
        self.country_input = self.ui.countryLineEdit
        self.password_input = self.ui.passwordLineEdit
        self.confirm_password_input = self.ui.confirmPasswordLineEdit
        self.register_button = self.ui.registerButton
        self.already_have_account_button = self.ui.alreadyHaveAccountButton

        # Connect buttons
        self.register_button.clicked.connect(self.handle_register)
        # The 'alreadyHaveAccountButton' will be connected externally by AppLauncher
        # to handle the transition back to the login form.
        # So, no direct 'show_login_form' call here, just self.close()
        self.already_have_account_button.clicked.connect(self.close) # Simply close this window

        # Apply basic styling for the register form if needed
        self.setStyleSheet("""
            QMainWindow {
                background-color: #FFFFFF;
                border-radius: 10px;
            }
            QLabel#registerTitleLabel {
                color: #333;
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
            }
            QLineEdit {
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #007bff;
            }
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton#alreadyHaveAccountButton {
                background-color: transparent;
                color: #007bff;
                text-decoration: underline;
                font-size: 14px;
                padding: 5px;
                margin-top: 5px;
            }
            QPushButton#alreadyHaveAccountButton:hover {
                color: #0056b3;
            }
        """)

    def handle_register(self):
        full_name = self.full_name_input.text().strip()
        email = self.email_input.text().strip()
        phone_number = self.phone_number_input.text().strip()
        country = self.country_input.text().strip()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        if not (full_name and email and password and confirm_password):
            QMessageBox.warning(self, "Registration Error", "Please fill in all required fields.")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Registration Error", "Passwords do not match.")
            return

        if self.db_manager.register_user(full_name, email, phone_number, country, password):
            QMessageBox.information(self, "Registration Success", "Account created successfully! You can now log in.")
            self.clear_form()
            self.registration_successful.emit(email) # Emit signal with registered email
            self.close() # Close this window after successful registration
        else:
            QMessageBox.critical(self, "Registration Error", "Failed to register. Email might already be in use.")

    def clear_form(self):
        self.full_name_input.clear()
        self.email_input.clear()
        self.phone_number_input.clear()
        self.country_input.clear()
        self.password_input.clear()
        self.confirm_password_input.clear()

    # Removed the direct show_login_form method as AppLauncher will handle this
    # when this window closes.
