from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Window')
        self.resize(400, 500)

        layout = QVBoxLayout()

        self.label = QLabel("Demo")
        layout.addWidget(self.label)

        self.combo = QComboBox()
        self.combo.addItems(['One', 'Two', 'Three'])
        self.combo.currentIndexChanged.connect(self.update)
        layout.addWidget(self.combo)

        self.check = QCheckBox('Choose this')
        self.check2 = QCheckBox('and this?')
        layout.addWidget(self.check)
        layout.addWidget(self.check2)

        self.enter_text = QLineEdit('Type here')
        layout.addWidget(self.enter_text)

        self.radio = QRadioButton('This one?')
        self.radio2 = QRadioButton('Or this one?')
        layout.addWidget(self.radio)
        layout.addWidget(self.radio2)

        self.slider = QSlider(1)
        self.slider.setRange(1, 60)
        self.slider.valueChanged.connect(self.update)
        layout.addWidget(self.slider)

        self.ok_button = QPushButton('ok')
        layout.addWidget(self.ok_button)
        self.ok_button.clicked.connect(self.ok_button_click)

        self.cancel_button = QPushButton('Cancel')
        layout.addWidget(self.cancel_button)
        self.cancel_button.clicked.connect(self.cancel_button_click)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def update(self, value):
        print(f" combo box value is {self.combo.currentIndex()}")
        print(f" slider value is {self.slider.value()}")

    def ok_button_click(self):
        print("ok")

    def cancel_button_click(self):
        print("cancel")


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()





