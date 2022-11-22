import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QDialog, QWidget
from PyQt5.QtGui import QPainter, QColor
from random import randint, random


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.qp = QPainter()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.button.clicked.connect(self.run)
        self.now_drowing = False

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
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(randint(0, 300), randint(0, 300), randint(0, 300), randint(0, 300))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
