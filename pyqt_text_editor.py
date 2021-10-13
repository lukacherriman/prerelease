from PyQt5.QtWidgets import *

global saved
saved = True


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Unit Converter')
        self.resize(400, 500)

        layout = QVBoxLayout()

        self.text_input = QTextEdit()
        layout.addWidget(self.text_input)
        self.text_input.textChanged.connect(self.text_edited)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        sublayout = QHBoxLayout()
        self.open = QPushButton("Open")
        self.open.clicked.connect(self.open_clicked)
        sublayout.addWidget(self.open)
        self.save = QPushButton("Save")
        self.save.clicked.connect(self.save_clicked)
        sublayout.addWidget(self.save)
        self.new = QPushButton("New")
        self.new.clicked.connect(self.new_clicked)
        sublayout.addWidget(self.new)
        layout.addLayout(sublayout)

        global saved

    def open_clicked(self):
        global saved
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "/PythonFiles", "Text Files (*.txt *.html)",)

        with open(filename, 'r') as reader:
            file = reader.readlines()
            self.text_input.setText(file[0])

        saved = True

    def save_clicked(self):
        global saved
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "/PythonFiles", "Text Files (*.txt *.html)", )

        with open(filename, 'w') as writer:
            writer.writelines(self.text_input.toPlainText())

        saved = True

    def new_clicked(self):
        global saved

        if saved == False:
            dly = QMessageBox.warning(self, "New?", "Are you sure you don't want to save",
                                      QMessageBox.Save | QMessageBox.Discard)
            if dly == QMessageBox.Save:
                self.save_clicked()
                self.text_input.setText("")
                saved = True
            else:
                self.text_input.setText("")
                saved = True
        else:
            self.text_input.setText("")
            saved = True

    def text_edited(self):
        global saved
        saved = False

    def closeEvent(self, event):
        global saved

        if saved == False:
            dlg = QMessageBox.warning(self, "Quit?", "Are you sure",
                                      QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

        if dlg == QMessageBox.Save:
            self.save_clicked()
            self.app.quit()
        elif dlg == QMessageBox.Discard:
            self.app.quit()
        else:
            event.ignore()


app = QApplication([])
window = TextEditor()
window.show()
app.exec_()