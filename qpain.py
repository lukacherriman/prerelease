import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap, QPen

image_path = "C:/PythonFiles/Shrek.png"


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.image = QPixmap(image_path)

        self.painter = QPainter(self)
        self.pen = QPen()
        self.pen.setWidth(5)

    def paintEvent(self, event):

        #gives window size
        "print(self.rect())"
        "painter.drawPixmap(self.rect(), self.image)"
        print("hello")
        self.painter.setPen(self.pen)
        self.painter.drawEllipse(300, 300, 150, 150)
        self.painter.drawRect(100, 15, 400, 200)


def main():
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    app.exec_()

main()
