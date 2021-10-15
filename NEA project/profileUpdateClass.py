from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3
import datetime

import mainWindowClass as Main_MainWindow


class Update_profile(QtWidgets.QMainWindow):
    def __init__(self, connection, username):
        super().__init__()
        self.connection = connection
        self.username = username
        self.resize(500, 400)
        self.centralwidget = QtWidgets.QWidget(self)

        self.setWindowTitle("Update Profile")

        verticle_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.grid_layout = QtWidgets.QGridLayout()

        self.weight_label = QtWidgets.QLabel()
        self.grid_layout.addWidget(self.weight_label, 1, 0)
        self.weight_label.setText("Weight")
        self.weight_line_edit = QtWidgets.QLineEdit()
        self.grid_layout.addWidget(self.weight_line_edit, 1, 1)

        self.FTP_label = QtWidgets.QLabel()
        self.grid_layout.addWidget(self.FTP_label, 2, 0)
        self.FTP_label.setText("FTP")
        self.FTP_line_edit = QtWidgets.QLineEdit()
        self.grid_layout.addWidget(self.FTP_line_edit, 2, 1)

        self.HRThreshold_label = QtWidgets.QLabel()
        self.grid_layout.addWidget(self.HRThreshold_label, 3, 0)
        self.HRThreshold_label.setText("Heart Rate Threshold")
        self.HRThreshold_line_edit = QtWidgets.QLineEdit()
        self.grid_layout.addWidget(self.HRThreshold_line_edit, 3, 1)

        self.DOB_label = QtWidgets.QLabel()
        self.grid_layout.addWidget(self.DOB_label, 4, 0)
        self.DOB_label.setText("Date of Birth")
        self.DOB_date_edit = QtWidgets.QDateEdit()
        self.DOB_date_edit.setDisplayFormat("dd/MM/yyyy")

        # sets the maximum date selectable to he current date
        today_date = datetime.date.today()
        string_date = today_date.strftime("%Y-%m-%d")
        year = int(string_date[0] + string_date[1] + string_date[2] + string_date[3])
        month = int(string_date[5] + string_date[6])
        day = int(string_date[8] + string_date[9])
        max_date = QtCore.QDate(year, month, day)
        self.DOB_date_edit.setMaximumDate(max_date)

        self.grid_layout.addWidget(self.DOB_date_edit, 4, 1)

        self.surname_label = QtWidgets.QLabel()
        self.grid_layout.addWidget(self.surname_label, 5, 0)
        self.surname_label.setText("Surname")
        self.surname_line_edit = QtWidgets.QLineEdit()
        self.grid_layout.addWidget(self.surname_line_edit, 5, 1)

        self.firstname_label = QtWidgets.QLabel()
        self.grid_layout.addWidget(self.firstname_label, 6, 0)
        self.firstname_label.setText("First Name")
        self.firstname_line_edit = QtWidgets.QLineEdit()
        self.grid_layout.addWidget(self.firstname_line_edit, 6, 1)

        verticle_layout.addLayout(self.grid_layout)

        self.error_label = QtWidgets.QLabel()
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        verticle_layout.addWidget(self.error_label)

        self.enter_button = QtWidgets.QPushButton()
        self.enter_button.setText("Enter")
        self.enter_button.clicked.connect(self.enter)
        verticle_layout.addWidget(self.enter_button)

        self.setLayout(verticle_layout)

        self.update_ui()
        self.setCentralWidget(self.centralwidget)

    def update_ui(self):
        # sets all the text for line edits
        cursor = self.connection.cursor()
        cursor.execute(f"""SELECT weight, FTP, HRThreshold, dateOfBirth, surname, firstName 
                            FROM users WHERE username = '{self.username}'""")
        profile = cursor.fetchall()
        self.weight = profile[0][0]
        self.FTP = profile[0][1]
        self.HR = profile[0][2]
        birth = profile[0][3]

        year = int(birth[0] + birth[1] + birth[2] + birth[3])
        month = int(birth[5] + birth[6])
        day = int(birth[8] + birth[9])
        birth_date = QtCore.QDate(year, month, day)

        self.last_name = profile[0][4]
        self.first_name = profile[0][5]

        self.weight_line_edit.setText(str(self.weight))
        self.FTP_line_edit.setText(str(self.FTP))
        self.HRThreshold_line_edit.setText(str(self.HR))
        self.DOB_date_edit.setDate(birth_date)
        self.surname_line_edit.setText(str(self.last_name))
        self.firstname_line_edit.setText(str(self.first_name))

    def enter(self):
        self.close()

    def closeEvent(self, event):
        error = False

        # makes sure the data types inputed are all correct
        try:
            weight = float(self.weight_line_edit.text())
            FTP = int(self.FTP_line_edit.text())
            HR = int(self.HRThreshold_line_edit.text())
        except ValueError:
            error = True
            self.error_label.setText("*Enter correct data type*")

        DOB = self.DOB_date_edit.date().toString("yyyy-MM-dd")
        surname = self.surname_line_edit.text()
        firstname = self.firstname_line_edit.text()

        # updates the profile of the user
        if not error:
            try:
                self.connection.execute(f"""
                                                UPDATE users SET (weight, FTP, HRThreshold, DateOfBirth, surname, firstName) =
                                                ({weight}, {FTP}, {HR}, '{DOB}', '{surname}', '{firstname}')
                                                WHERE username = '{self.username}'
                                                """)

                if not testing:
                    self.connection.commit()

                self.app = QtWidgets.QApplication(sys.argv)
                self.ui = Main_MainWindow(self.connection, self.username)
                event.accept()
                self.ui.show()
                self.app.exec_()
            except sqlite3.Error:
                self.error_label.setText("*Error*")
                event.ignore()

        else:
            event.ignore()