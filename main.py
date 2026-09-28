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