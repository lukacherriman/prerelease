from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3
import datetime

import mainWindowClass as Main_MainWindow


class Name_ride(QtWidgets.QMainWindow):
    def __init__(self, main_window, connection, username, rideId):
        super().__init__()
        self.resize(600, 500)
        self.centralWidget = QtWidgets.QWidget(self)

        # sets the minimum and maximum date
        today_date = datetime.date.today()
        string_date = today_date.strftime("%Y-%m-%d")
        year = int(string_date[0]+string_date[1]+string_date[2]+string_date[3])
        month = int(string_date[5]+string_date[6])
        day = int(string_date[8]+string_date[9])
        max_date = QtCore.QDate(year, month, day)
        min_date = QtCore.QDate(2010, 1, 1)

        self.main_window = main_window
        self.connection = connection
        self.username = username
        self.rideId = rideId

        layout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.rideNameLineEdit = QtWidgets.QLineEdit()
        self.rideNameLineEdit.setText("Ride name")

        self.rideDateCalender = QtWidgets.QCalendarWidget()
        self.rideDateCalender.setMaximumDate(max_date)
        self.rideDateCalender.setMinimumDate(min_date)

        self.enter_button = QtWidgets.QPushButton()
        self.enter_button.setText("Enter")
        self.enter_button.clicked.connect(self.enter)

        self.error_label = QtWidgets.QLabel()
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)

        layout.addWidget(self.rideNameLineEdit)
        layout.addWidget(self.rideDateCalender)
        layout.addWidget(self.error_label)
        layout.addWidget(self.enter_button)
        self.setLayout(layout)
        self.setCentralWidget(self.centralWidget)

    def enter(self):
        self.close()

    def closeEvent(self, event):
        ride_name = self.rideNameLineEdit.text()
        ride_date = self.rideDateCalender.selectedDate().toString("yyyy-MM-dd")

        # updates the name and date of the ride just added, defaults to ridename and current date
        try:
            self.connection.execute(f"UPDATE userRide SET name = '{ride_name}', date = '{ride_date}' WHERE rideId = {self.rideId}")
            if not testing:
                self.connection.commit()
            self.main_window.more_rides(0)

            self.app = QtWidgets.QApplication(sys.argv)
            self.ui = Main_MainWindow(self.connection, self.username)
            event.accept()
            self.ui.show()
            self.app.exec_()
        except sqlite3.Error:
            self.error_label.setText("*Error*")
            event.ignore()