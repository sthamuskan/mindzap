# login_ui.py
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sqlite3
class LoginUi_Form(QtWidgets.QWidget): # Corrected: Inherits from QtWidgets.QWidget
    # Define signals for communication with the main application
    switch_to_register_signal = QtCore.pyqtSignal()
    login_successful_signal = QtCore.pyqtSignal(str) # Emits username

    def __init__(self): # Added __init__ method for proper initialization
        super().__init__()
        # Initialize instance attributes to None or default values
        self.widget = None
        self.background_label = None
        self.profile_image_label = None
        self.username_lineEdit = None
        self.password_lineEdit = None
        self.login_button = None
        self.register_here_button = None


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(749, 650)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-20, 0, 691, 631))
        self.widget.setStyleSheet("/* Styling for the Login Button */\n"
"QPushButton#loginButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#loginButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#loginButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"/* Styling for the Register Button (on login page) */\n"
"QPushButton#registerHereButton {\n"
"    background-color: transparent;\n"
"    color: #007bff; /* A blue color for links */\n"
"    border: none;\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton#registerHereButton:hover {\n"
"    color: #0056b3;\n"
"}\n"
"\n"
"QPushButton#registerHereButton:pressed {\n"
"    padding-left: 2px;\n"
"    padding-top: 2px;\n"
"}")
        self.widget.setObjectName("widget")

        # Background label for the form
        self.background_label = QtWidgets.QLabel(self.widget)
        self.background_label.setGeometry(QtCore.QRect(150, 10, 561, 611))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.background_label.setFont(font)
        self.background_label.setStyleSheet("background-color: rgba(211, 211, 211, 255);\n"
                                          "border-bottom-right-radius:50px;")
        self.background_label.setText("")
        self.background_label.setObjectName("background_label")

        # Profile image label
        self.profile_image_label = QtWidgets.QLabel(self.widget)
        self.profile_image_label.setGeometry(QtCore.QRect(350, 20, 161, 151))
        self.profile_image_label.setStyleSheet("background-color: rgba(180, 52, 85, 255);")
        self.profile_image_label.setText("")
        # Ensure you have a 'profile.jpeg' in your resources or provide a valid path
        self.profile_image_label.setPixmap(QtGui.QPixmap(":/image/Users/DELL/Downloads/profile.jpeg"))
        self.profile_image_label.setScaledContents(True)
        self.profile_image_label.setObjectName("profile_image_label")

        # Username LineEdit
        self.username_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.username_lineEdit.setGeometry(QtCore.QRect(270, 200, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                            "border: none;\n"
                                            "border-bottom:2px solid rgba(46,82,101,200);\n"
                                            "color:rgba(0,0,0,240);\n"
                                            "padding-bottom:7px;")
        self.username_lineEdit.setObjectName("username_lineEdit")

        # Password LineEdit
        self.password_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.password_lineEdit.setGeometry(QtCore.QRect(270, 280, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                            "border: none;\n"
                                            "border-bottom:2px solid rgba(46,82,101,200);\n"
                                            "color:rgba(0,0,0,240);\n"
                                            "padding-bottom:7px;")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")

        # Login Button
        self.login_button = QtWidgets.QPushButton(self.widget)
        self.login_button.setGeometry(QtCore.QRect(270, 380, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.login_button.setFont(font)
        self.login_button.setObjectName("loginButton") # Use objectName for CSS

        # "Don't have an account?" button
        self.register_here_button = QtWidgets.QPushButton(self.widget)
        self.register_here_button.setGeometry(QtCore.QRect(310, 430, 211, 24))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        self.register_here_button.setFont(font)
        self.register_here_button.setObjectName("registerHereButton") # Use objectName for CSS

        # Connect signals and slots
        self.login_button.clicked.connect(self.simulate_login)
        self.register_here_button.clicked.connect(self.switch_to_register_signal.emit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.username_lineEdit.setPlaceholderText(_translate("Form", "Username or Email:"))
        self.password_lineEdit.setPlaceholderText(_translate("Form", "Password:"))
        self.login_button.setText(_translate("Form", "Login"))
        self.register_here_button.setText(_translate("Form", "Don't have an account? Register Here"))

    def simulate_login(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()

        # Simple simulated login logic
        if username == "test" and password == "password":
            QtWidgets.QMessageBox.information(self.widget, "Login Success", "Login successful!")
            self.login_successful_signal.emit(username)
        else:
            QtWidgets.QMessageBox.warning(self.widget, "Login Failed", "Invalid username or password.")

# Note: The 'if __name__ == "__main__":' block is removed here
# because this file will be imported by main_app.py.
