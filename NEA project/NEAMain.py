from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3

from loginPageClass import Login_MainWindow
from mainWindowClass import Main_MainWindow
from constants import *


if __name__ == "__main__":

    connection = sqlite3.connect('trainingTipsDatabase.db')

    if testing:
        username = "sussymajor"
        app = QtWidgets.QApplication(sys.argv)
        ui = Main_MainWindow(connection, username)
        ui.show()
        app.exec_()

    else:
        app = QtWidgets.QApplication(sys.argv)
        ui = Login_MainWindow(connection)
        ui.show()
        app.exec_()
    connection.close()
