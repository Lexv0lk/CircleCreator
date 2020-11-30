import sys
from random import randint
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor, QPolygon, QPen
from UI import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setMouseTracking(True)
        self.coords_ = []
        self.qp = QPainter()
        self.flag = False
        self.create_btn.clicked.connect(self.create_circle)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        size = randint(50, 150)
        self.qp.setPen(QColor(0, 0, 0))
        self.qp.setBrush(color)
        x = randint(size, self.width() - size)
        y = randint(size, self.height() - size)
        x -= size / 2
        y -= size / 2
        self.qp.drawEllipse(x, y, size, size)

    def create_circle(self):
        self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
