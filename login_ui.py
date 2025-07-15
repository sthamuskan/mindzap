# login_ui.py (This file now contains the Entry Screen UI)
from PyQt5 import QtCore, QtGui, QtWidgets
import res_rc # Ensure res_rc.py is generated and in the same directory

class EnterUiForm(QtWidgets.QWidget): # Renamed class to reflect its purpose as the Entry UI
    # Define signals for navigation
    switch_to_login_signal = QtCore.pyqtSignal()
    switch_to_register_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        # Initialize instance attributes to None or default values
        self.widget = None
        self.label = None
        self.label_2 = None
        self.label_3 = None
        self.label_4 = None
        self.lineEdit = None
        self.lineEdit_2 = None
        self.pushButton = None
        self.label_7 = None
        self.label_8 = None
        self.label_9 = None
        self.label_10 = None
        self.forgotPasswordLabel_2 = None # This button will now link to the Register screen


    def setupUi(self, form):
        form.setObjectName("Form")
        form.resize(667, 622)
        self.widget = QtWidgets.QWidget(form)
        self.widget.setGeometry(QtCore.QRect(20, 10, 611, 581))
        self.widget.setStyleSheet("\n"
"QPushButton#pushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"/* Styling for the Register Button (assuming objectName is registerButton) */\n"
"QPushButton#registerButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226)); /* Teal to Green gradient */\n"
"    color: rgba(255, 255, 255, 210); /* White text color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    border: none; /* No border */\n"
"}\n"
"\n"
"QPushButton#registerButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226)); \n"
"}\n"
"\n"
"QPushButton#registerButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150, 123, 111, 255); \n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 40, 280, 491))
        self.label.setStyleSheet("border-image: url(:/image/background.jpeg);"
"border-top-left-radius:50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 281, 491))
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,80);\n"
"border-top-left-radius:50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(290, 40, 291, 491))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(390, 60, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0,0,0,200);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 150, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 240, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(360, 330, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(100, 70, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(60, 190, 211, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(100, 310, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(70, 380, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_10.setObjectName("label_10")
        self.forgotPasswordLabel_2 = QtWidgets.QPushButton(self.widget)
        self.forgotPasswordLabel_2.setGeometry(QtCore.QRect(310, 420, 271, 24))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        self.forgotPasswordLabel_2.setFont(font)
        self.forgotPasswordLabel_2.setObjectName("forgotPasswordLabel_2")

        # Connect buttons to methods/signals
        self.pushButton.clicked.connect(self.simulate_enter_login)
        self.forgotPasswordLabel_2.clicked.connect(self.switch_to_register_signal.emit)


        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "MindZap Entry"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "User Name:"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password:"))
        self.pushButton.setText(_translate("Form", "L o g  I n"))
        self.label_7.setText(_translate("Form", "MindZap"))
        self.label_8.setText(_translate("Form", "Zap In. Power Your Mind."))
        self.label_9.setText(_translate("Form", "System ready!"))
        self.label_10.setText(_translate("Form", " Let\'s zap some knowledge!"))
        self.forgotPasswordLabel_2.setText(_translate("Form", "Forgot your UserName or Password?|Sign Up"))

    def simulate_enter_login(self):
        """Simulates a login attempt on the initial entry screen."""
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        # Simple simulated check for the initial entry
        if username == "user" and password == "pass": # Example credentials
            QtWidgets.QMessageBox.information(self.widget, "Success", "Entered MindZap! Proceeding to Login.")
            self.switch_to_login_signal.emit() # Emit signal to go to the main login page
        else:
            QtWidgets.QMessageBox.warning(self.widget, "Login Failed", "Invalid username or password for entry.")

# Note: The 'if __name__ == "__main__":' block is removed here
# because this file will be imported by main_app.py.
