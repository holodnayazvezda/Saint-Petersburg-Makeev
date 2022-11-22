import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.qp = QPainter()
        self.initUi()
        self.now_drowing = False

    def initUi(self):
        self.setGeometry(300, 300, 900, 600)
        self.setWindowTitle("Окружности и git")
        self.button = QPushButton('Кружочки разного цвета!', self)
        self.button.resize(300, 30)
        self.button.move(300, 500)
        self.button.clicked.connect(self.run)

    def run(self):
        self.now_drowing = True
        self.update()

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        self.qp = QPainter()
        # Начинаем процесс рисования
        self.qp.begin(self)
        if self.now_drowing:
            self.draw()
        # Завершаем рисование
        self.qp.end()

    def draw(self):
        self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        self.qp.drawEllipse(randint(0, 600), randint(0, 600), randint(0, 300), randint(0, 300))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
