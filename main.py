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
        self.btn_about = QPushButton("О проекте")

        # Размеры кнопок
        self.btn_start.setFixedSize(150, 100)
        self.btn_sandbox.setFixedSize(150, 100)
        self.btn_about.setFixedSize(150, 100)

        # Вертикальный контейнер для кнопок
        self.central_widget = QWidget()
        self.lyt = QVBoxLayout(self.central_widget)

        # Размеры окна
        self.setMinimumSize(1500, 1000)

        # Размещения кнопок на окне 
        self.lyt.addWidget(self.btn_start)
        self.lyt.addWidget(self.btn_sandbox)
        self.lyt.addWidget(self.btn_about)

        self.setCentralWidget(self.central_widget)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()