from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3
import datetime

import loginPageClass as Login_MainWindow
import hashingAlgorithm as hashing_algorithm

class Signup_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, connection):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(1000, 1000)
        self.connection = connection

        self.centralwidget = QtWidgets.QWidget(self)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(250, 169, 500, 410))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)

        self.formLayout = QtWidgets.QFormLayout(self.frame)

        self.nameFirstLabel = QtWidgets.QLabel(self.frame)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameFirstLabel)
        self.nameFirstLineEdit = QtWidgets.QLineEdit(self.frame)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameFirstLineEdit)

        self.surnameLabel = QtWidgets.QLabel(self.frame)
        self.surnameLabel.setObjectName("surnameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.surnameLabel)
        self.surnameLineEdit = QtWidgets.QLineEdit(self.frame)
        self.surnameLineEdit.setObjectName("surnameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.surnameLineEdit)

        self.usernameLabel = QtWidgets.QLabel(self.frame)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.frame)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit)

        self.passwordLabel = QtWidgets.QLabel(self.frame)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.frame)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)

        self.passwordReLabel = QtWidgets.QLabel(self.frame)
        self.passwordReLabel.setObjectName("passwordReLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.passwordReLabel)
        self.passwordReLineEdit = QtWidgets.QLineEdit(self.frame)
        self.passwordReLineEdit.setObjectName("passwordReLineEdit")
        self.passwordReLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.passwordReLineEdit)

        today_date = datetime.date.today()
        string_date = today_date.strftime("%Y-%m-%d")
        year = int(string_date[0] + string_date[1] + string_date[2] + string_date[3])
        month = int(string_date[5] + string_date[6])
        day = int(string_date[8] + string_date[9])
        max_date = QtCore.QDate(year, month, day)

        self.DOBLabel = QtWidgets.QLabel(self.frame)
        self.DOBLabel.setObjectName("DOBLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.DOBLabel)
        self.DOBLineEdit = QtWidgets.QDateEdit(self.frame)
        self.DOBLineEdit.setObjectName("DOBLineEdit")
        self.DOBLineEdit.setMaximumDate(max_date)
        self.DOBLineEdit.setDisplayFormat("dd/MM/yyyy")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.DOBLineEdit)

        self.weightLabel = QtWidgets.QLabel(self.frame)
        self.weightLabel.setObjectName("weightLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.weightLabel)
        self.weightLineEdit = QtWidgets.QLineEdit(self.frame)
        self.weightLineEdit.setObjectName("weightLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.weightLineEdit)

        self.FTPLabel = QtWidgets.QLabel(self.frame)
        self.FTPLabel.setObjectName("FTPLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.FTPLabel)
        self.FTPLineEdit = QtWidgets.QLineEdit(self.frame)
        self.FTPLineEdit.setObjectName("FTPLineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.FTPLineEdit)

        font = QtGui.QFont()
        font.setPointSize(18)
        self.signupLabel = QtWidgets.QLabel(self.centralwidget)
        self.signupLabel.setGeometry(QtCore.QRect(250, 90, 160, 80))
        self.signupLabel.setFont(font)
        self.signupLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.signupLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.signupLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.signupLabel.setObjectName("signupLabel")

        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(380, 590, 240, 20))
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")

        font = QtGui.QFont()
        font.setPointSize(18)
        self.signupButton = QtWidgets.QPushButton(self.centralwidget)
        self.signupButton.setGeometry(QtCore.QRect(510, 640, 190, 70))
        self.signupButton.setFont(font)
        self.signupButton.setObjectName("pushButton")
        self.signupButton.clicked.connect(self.signupClicked)

        self.backToLoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.backToLoginButton.setGeometry(QtCore.QRect(300, 640, 190, 70))
        self.backToLoginButton.setFont(font)
        self.backToLoginButton.clicked.connect(self.backToLoginClicked)
        self.setCentralWidget(self.centralwidget)

        self.updateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def updateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameFirstLabel.setText(_translate("MainWindow", "First Name"))
        self.surnameLabel.setText(_translate("MainWindow", "Surname"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.passwordLabel.setText(_translate("MainWindow", "Password - 8"))
        self.passwordReLabel.setText(_translate("MainWindow", "Password Re"))
        self.DOBLabel.setText(_translate("MainWindow", "DOB"))
        self.weightLabel.setText(_translate("MainWindow", "Weight (kg)"))
        self.FTPLabel.setText(_translate("MainWindow", "FTP (W)"))
        self.signupLabel.setText(_translate("MainWindow", "Signup"))
        self.errorLabel.setText(_translate("MainWindow", " "))
        self.signupButton.setText(_translate("MainWindow", "Signup"))
        self.backToLoginButton.setText(_translate("MainWindow", "<- Login"))

    def check_user(self, username):
        # checks if username already in use
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT username FROM users WHERE username = '{username}'")
        result = cursor.fetchall()
        if result:
            return True
        else:
            return False

    def backToLoginClicked(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.ui = Login_MainWindow(self.connection)
        self.close()
        self.ui.show()
        self.app.exec_()

    def signupClicked(self):
        firstName = self.nameFirstLineEdit.text()
        surname = self.surnameLineEdit.text()
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        passwordRe = self.passwordReLineEdit.text()
        dateOfBirth = self.DOBLineEdit.date().toString("yyyy-MM-dd")

        try:
            weight = float(self.weightLineEdit.text())
            FTP = float(self.FTPLineEdit.text())
        except ValueError:
            self.errorLabel.setText("Enter correct data type")
            weight = self.weightLineEdit.text()
            FTP = self.FTPLineEdit.text()

        check = self.check_user(username)

        if check:
            self.errorLabel.setText("*Username in use*")
        elif username == "" or password == "" or passwordRe == "" or firstName == "" or surname == "" or dateOfBirth == "" or weight == "" or FTP == "":
            self.errorLabel.setText("*Fill all fields*")
        elif len(password) < 8:
            self.errorLabel.setText("*Password too short*")
        elif password != passwordRe:
            self.errorLabel.setText("*Passwords not same*")
        elif type(FTP) == float and type(weight) == float:
            hash_password = hashing_algorithm(username, password)

            try:
                self.connection.execute(f""" 
                                            INSERT INTO users(username, hashPassword, HRThreshold, weight, FTP, dateOfBirth, surname, firstName)
                                            VALUES('{username}', '{hash_password}', {0}, {weight}, {FTP}, '{dateOfBirth}', '{surname}', '{firstName}')
                                        """)

                self.connection.commit()
                self.nameFirstLineEdit.setText("")
                self.surnameLineEdit.setText("")
                self.usernameLineEdit.setText("")
                self.passwordLineEdit.setText("")
                self.passwordReLineEdit.setText("")
                self.DOBLineEdit.setDate(QtCore.QDate(2000, 1, 1))
                self.weightLineEdit.setText("")
                self.FTPLineEdit.setText("")
                self.errorLabel.setText("Success")

            except sqlite3.Error:
                self.errorLabel.setText("*Error*")