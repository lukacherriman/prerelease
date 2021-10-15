from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3

import loginPageClass as Login_MainWindow
import mainWindowClass as Main_MainWindow

global testing
testing = False


def hashing_algorithm(username, password):
    # to make sure all the hashes are unique the salt used will be their unique username
    us_list = [ord(ch) for ch in username]
    pw_list = [ord(ch) for ch in password]

    pw_weight = [pw_list[i] ** (2*(i+1)) for i in range(len(pw_list))]
    us_weight = [us_list[i] ** (2*(i+1)) for i in range(len(us_list))]
    hash_pw = sum(pw_weight) + sum(us_list)


    mod_hash = hash_pw % 2 ** 64

    return mod_hash

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
