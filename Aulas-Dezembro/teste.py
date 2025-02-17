from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt6.QtCore import Qt
import sys

class HelloWorldWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Olá Mundo")
        self.setGeometry(150, 80, 300, 100)  # Aumentei o tamanho da janela para melhor acomodar o texto

        label = QLabel("Hello World!", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Alinha o texto ao centro da label
        label.setGeometry(0, 0, self.width(), self.height())  # A label ocupará toda a janela

        label.setStyleSheet("font-size: 18px; font-weight: bold;")

if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = HelloWorldWindow()
        window.show()
        sys.exit(app.exec())
