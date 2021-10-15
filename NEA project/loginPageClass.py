from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3

import signupPageClass as Signup_MainWindow
import mainWindowClass as Main_MainWindow
import hashingAlgorithm as hashing_algorithm


class Login_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.setObjectName("MainWindow")
        self.resize(960, 1000)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.setFont(font)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(36)
        self.titleLable = QtWidgets.QLabel(self.centralwidget)
        self.titleLable.setGeometry(QtCore.QRect(240, 100, 480, 110))
        self.titleLable.setFont(font)
        self.titleLable.setFrameShape(QtWidgets.QFrame.Box)
        self.titleLable.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLable.setObjectName("titleLable")

        font = QtGui.QFont()
        font.setPointSize(18)
        self.LoginLabel = QtWidgets.QLabel(self.centralwidget)
        self.LoginLabel.setGeometry(QtCore.QRect(240, 230, 240, 70))
        self.LoginLabel.setFont(font)
        self.LoginLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.LoginLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LoginLabel.setObjectName("LoginLabel")

        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(240, 299, 480, 400))
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")

        self.usernameLineEdit = QtWidgets.QLineEdit(self.frame)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.gridLayout.addWidget(self.usernameLineEdit, 0, 1, 1, 1)
        self.usernameLabel = QtWidgets.QLabel(self.frame)
        self.usernameLabel.setObjectName("usernameLabel")
        self.gridLayout.addWidget(self.usernameLabel, 0, 0, 1, 1)

        self.passwordLabel = QtWidgets.QLabel(self.frame)
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout.addWidget(self.passwordLabel, 1, 0, 1, 1)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.frame)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.gridLayout.addWidget(self.passwordLineEdit, 1, 1, 1, 1)

        font = QtGui.QFont()
        font.setPointSize(18)
        self.signUpbutton = QtWidgets.QPushButton(self.centralwidget)
        self.signUpbutton.setGeometry(QtCore.QRect(480, 229, 241, 70))
        self.signUpbutton.setFont(font)
        self.signUpbutton.setObjectName("signUpbutton")
        self.signUpbutton.clicked.connect(self.signUpClicked)

        font = QtGui.QFont()
        font.setPointSize(8)
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(420, 650, 120, 40))
        self.errorLabel.setFont(font)
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")

        self.enterButton = QtWidgets.QPushButton(self.centralwidget)
        self.enterButton.setGeometry(QtCore.QRect(380, 710, 200, 60))
        self.enterButton.setObjectName("pushButton")
        self.enterButton.clicked.connect(self.enterClicked)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLable.setText(_translate("MainWindow", "Lukapeaks"))
        self.LoginLabel.setText(_translate("MainWindow", "Login"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.signUpbutton.setText(_translate("MainWindow", "Signup"))
        self.errorLabel.setText(_translate("MainWindow", " "))
        self.enterButton.setText(_translate("MainWindow", "Enter"))

    def enterClicked(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()

        try:
            hash_password = hashing_algorithm(username, password)
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT username FROM users WHERE username = '{username}' AND hashPassword = {hash_password}")
            result = cursor.fetchall()

            if result:
                self.app = QtWidgets.QApplication(sys.argv)
                self.ui = Main_MainWindow(self.connection, username)
                self.close()
                self.ui.show()
                self.app.exec_()
            elif username == "" or password == "":
                self.errorLabel.setText("*Error*")
            else:
                self.errorLabel.setText("*Error*")
        except sqlite3.Error:
            self.errorLabel.setText("*Error*")

    def signUpClicked(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.ui = Signup_MainWindow(self.connection)
        self.close()
        self.ui.show()
        self.app.exec_()