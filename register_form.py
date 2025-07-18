# register_form.py (This file contains the Registration Form UI)
from PyQt5 import QtCore, QtGui, QtWidgets
import res_rc # Ensure res_rc.py is generated and in the same directory
import os      # To help with database path
import sqlite3 # To interact with the SQLite database

class RegisterUi_Form(QtWidgets.QWidget): # Class for the registration form
    # Define signals for communication with the main application
    registration_successful_signal = QtCore.pyqtSignal()
    switch_to_login_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        # Initialize instance attributes to None or default values
        self.widget = None
        self.label_3 = None # Background label
        self.label_mz_logo = None # Renamed from 'label' for clarity
        self.label_profile_pic = None # Renamed from 'label_2' for clarity
        self.lineEdit_full_name = None
        self.lineEdit_phone_number = None
        self.lineEdit_password = None
        self.lineEdit_email = None
        self.lineEdit_country = None
        self.lineEdit_confirm_password = None
        self.register_button = None
        self.already_have_account_button = None


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(749, 650)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-20, 0, 691, 631))
        self.widget.setStyleSheet("/* Styling for the Register Button */\n"
"QPushButton#registerButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#registerButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#registerButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"/* Styling for the \"Already have an account?\" button */\n"
"QPushButton#alreadyAccountButton {\n"
"    background-color: transparent;\n"
"    color: #007bff; /* A blue color for links */\n"
"    border: none;\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton#alreadyAccountButton:hover {\n"
"    color: #0056b3;\n"
"}\n"
"\n"
"QPushButton#alreadyAccountButton:pressed {\n"
"    padding-left: 2px;\n"
"    padding-top: 2px;\n"
"}")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(150, 10, 561, 611))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(211, 211, 211, 255);\n"
"\n"
"\n"
"\n"
"border-bottom-right-radius:50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.lineEdit_full_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_full_name.setGeometry(QtCore.QRect(190, 200, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit_full_name.setFont(font)
        self.lineEdit_full_name.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_full_name.setObjectName("lineEdit_full_name")

        self.lineEdit_phone_number = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_phone_number.setGeometry(QtCore.QRect(190, 260, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit_phone_number.setFont(font)
        self.lineEdit_phone_number.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_phone_number.setObjectName("lineEdit_phone_number")

        self.register_button = QtWidgets.QPushButton(self.widget)
        self.register_button.setGeometry(QtCore.QRect(270, 430, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.register_button.setFont(font)
        self.register_button.setObjectName("registerButton")

        self.label_mz_logo = QtWidgets.QLabel(self.widget)
        self.label_mz_logo.setGeometry(QtCore.QRect(160, 20, 51, 41))
        self.label_mz_logo.setStyleSheet("background-image: url(:/image/Users/DELL/Desktop/MindZap/mz.jpg);")
        self.label_mz_logo.setText("")
        self.label_mz_logo.setPixmap(QtGui.QPixmap(":/image/mz.jpg"))
        self.label_mz_logo.setScaledContents(True)
        self.label_mz_logo.setObjectName("label_mz_logo")

        self.label_profile_pic = QtWidgets.QLabel(self.widget)
        self.label_profile_pic.setGeometry(QtCore.QRect(350, 20, 161, 151))
        self.label_profile_pic.setStyleSheet("\n"
"background-color: rgba(180, 52, 85, 255);\n"
"\n"
"")
        self.label_profile_pic.setText("")
        self.label_profile_pic.setPixmap(QtGui.QPixmap(":/image/profile.jpeg"))
        self.label_profile_pic.setScaledContents(True)
        self.label_profile_pic.setObjectName("label_profile_pic")

        self.lineEdit_email = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_email.setGeometry(QtCore.QRect(440, 200, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_email.setObjectName("lineEdit_email")

        self.lineEdit_country = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_country.setGeometry(QtCore.QRect(440, 260, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit_country.setFont(font)
        self.lineEdit_country.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_country.setObjectName("lineEdit_country")

        self.lineEdit_confirm_password = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_confirm_password.setGeometry(QtCore.QRect(440, 320, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit_confirm_password.setFont(font)
        self.lineEdit_confirm_password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                                    "border: none;\n"
                                                    "border-bottom:2px solid rgba(46,82,101,200);\n"
                                                    "color:rgba(0,0,0,240);\n"
                                                    "padding-bottom:7px;\n"
                                                    "")
        self.lineEdit_confirm_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_confirm_password.setObjectName("lineEdit_confirm_password")

        self.lineEdit_password = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_password.setGeometry(QtCore.QRect(190, 320, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")

        self.already_have_account_button = QtWidgets.QPushButton(self.widget)
        self.already_have_account_button.setGeometry(QtCore.QRect(310, 510, 211, 24))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        self.already_have_account_button.setFont(font)
        self.already_have_account_button.setObjectName("alreadyAccountButton")

        # Connect signals and slots
        self.register_button.clicked.connect(self.register_user)
        self.already_have_account_button.clicked.connect(self.switch_to_login_signal.emit)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Register"))
        self.lineEdit_full_name.setPlaceholderText(_translate("Form", "Full Name:"))
        self.lineEdit_phone_number.setPlaceholderText(_translate("Form", "Phone Number:"))
        self.lineEdit_password.setPlaceholderText(_translate("Form", "Password:"))
        self.register_button.setText(_translate("Form", "Register Now!"))
        self.lineEdit_email.setPlaceholderText(_translate("Form", "Email:"))
        self.lineEdit_country.setPlaceholderText(_translate("Form", "Country:"))
        self.lineEdit_confirm_password.setPlaceholderText(_translate("Form", "Confirm Password:"))
        self.already_have_account_button.setText(_translate("Form", "Already have an account?"))

    def register_user(self):
        full_name = self.lineEdit_full_name.text()
        phone_number = self.lineEdit_phone_number.text()
        password = self.lineEdit_password.text()
        email = self.lineEdit_email.text()
        country = self.lineEdit_country.text()
        confirm_password = self.lineEdit_confirm_password.text()

        if not all([full_name, phone_number, password, email, country, confirm_password]):
            QtWidgets.QMessageBox.warning(self.widget, "Registration Failed", "Please fill in all fields.")
            return

        if password != confirm_password:
            QtWidgets.QMessageBox.warning(self.widget, "Registration Failed", "Passwords do not match.")
            return

        QtWidgets.QMessageBox.information(self.widget, "Registration Success", "Registration successful! You can now log in.")
        self.registration_successful_signal.emit()

