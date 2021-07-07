import tkinter as tk
from tkinter import filedialog
from PyQt5.QtWidgets import *

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt



root = tk.Tk()
root.withdraw()

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('location graph')
        self.resize(500, 500)

        layout = QVBoxLayout()

        self.open = QPushButton("open file")
        self.open.clicked.connect(self.open_file)
        layout.addWidget(self.open)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def open_file(self):
        file_path = filedialog.askopenfilename()
        print(file_path)
        with open(file_path, 'r') as reader:
            data = reader.readlines()

        data2 = []
        for i in range(len(data)):
            datapoint = []
            new = ""
            for ch in data[i]:
                if ch == "," or ch == "\n":
                    datapoint.append(new)
                    new = ""
                else:
                    new += ch
            datapoint.append(new)
            data2.append(datapoint)

        for i in range(len(data2)):
            print(data2[i][0], data2[i][3])



        """for i in range(len(data)):
            print(data[i][0], data[i][3])"""


app = QApplication([])
window = TextEditor()
window.show()
app.exec_()