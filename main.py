# from PySide6 import QtWidgets
# import sys

# app = QtWidgets.QApplication(sys.argv)

# window = QtWidgets.QWidget()
# window.setWindowTitle("Hello world on pyside6")
# window.resize(300, 250)
# lbl = QtWidgets.QLabel("Hello world")
# lbl1 = QtWidgets.QLabel("Hello")
# btn = QtWidgets.QPushButton("Close")

# # box = QtWidgets.QVBoxLayout()

# # box.addWidget(btn)
# # box.addWidget(lbl)

# # window.setLayout(box)
# window.setLayout(lbl)

# btn.clicked.connect(app.quit)

# window.show()

# sys.exit(app.exec())

from PySide6.QtWidgets import (
    QApplication, 
    QPushButton, 
    QMainWindow, 
    QVBoxLayout,
    QWidget
) 
from PySide6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Pyside6") # Заголовок окна
        self.btn_start = QPushButton("Начать") # Кнопка
        self.btn_sandbox = QPushButton("Песочница")

        # Размеры кнопок
        self.btn_start.setFixedSize(100, 50)
        self.btn_sandbox.setFixedSize(100, 50)

        # Вертикальный контейнер для кнопок
        self.central_widget = QWidget()
        self.lyt = QVBoxLayout(self.central_widget)

        # Размеры окна
        self.setFixedSize(400, 300)
        self.setMinimumSize(200,200)
        self.setMaximumSize(1000, 1000)

        # Размещения кнопок на окне 
        self.lyt.addWidget(self.btn_start)
        self.lyt.addWidget(self.btn_sandbox)

        self.setCentralWidget(self.central_widget)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()