from PyQt5.QtWidgets import *


class UnitConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Unit Converter')
        self.resize(400, 250)

        layout = QVBoxLayout()
        sublayout = QHBoxLayout()

        self.label = QLabel("Units Converter")
        sublayout.addWidget(self.label)
        layout.addLayout(sublayout)

        sublayout2 = QHBoxLayout()
        self.quantity = QLineEdit("Enter Quantity")
        sublayout2.addWidget(self.quantity)
        self.unit = QComboBox()
        self.unit.addItems(["Kilometer", "Meter", "Centimeter", "Millimeter", "Inch", "Foot", "Yard"])
        sublayout2.addWidget(self.unit)
        layout.addLayout(sublayout2)

        sublayout3 = QHBoxLayout()
        self.result = QLineEdit("result")
        sublayout3.addWidget(self.result)
        self.convert_unit = QComboBox()
        self.convert_unit.addItems(["Kilometer", "Meter", "Centimeter", "Millimeter", "Inch", "Foot", "Yard"])
        sublayout3.addWidget(self.convert_unit)
        layout.addLayout(sublayout3)

        self.button = QPushButton("Convert")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.convert_click)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def convert_click(self):
        unit_dict = {"Kilometer": 1000, "Meter": 1, "Centimeter": 0.01, "Millimeter": 0.001,
                     "Inch": 0.0254, "Foot": 0.3048, "Yard": 0.9144
                     }
        quantity = int(self.quantity.text())
        unit1 = self.unit.currentText()
        conversion_unit = self.convert_unit.currentText()
        multiplier = unit_dict[unit1]
        divisor = unit_dict[conversion_unit]

        result = (quantity*multiplier)/divisor
        self.result.setText(str(result))

    def closeEvent(self, event):
        dlg = QMessageBox.warning(self, "Quit?", "Are you sure",
                                  QMessageBox.Ok | QMessageBox.Cancel)

        if dlg == QMessageBox.Ok:
            self.app.quit()
        else:
            event.ignore()


app = QApplication([])
window = UnitConverter()
window.show()
app.exec_()





