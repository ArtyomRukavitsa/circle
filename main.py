import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            coords = [randint(10, 300), randint(10, 200)]
            radius = randint(30, 90)
            painter = QPainter()
            painter.begin(self)
            painter.setPen(QColor('#fafa00'))
            painter.setBrush(QColor(250, 250, 0))
            painter.drawEllipse(*coords, radius, radius)
            painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())