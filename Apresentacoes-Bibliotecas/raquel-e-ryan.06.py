# flask
# 1. Arquivo main:
'''from flask import Flask

app = Flask(__name__)

from views import*

if __name__ == " __main__":
	app.run()

# 2.Arquivo views:

from main import app

@app.route("/")
def homepage():
	return 'Olá mundo'

@app.route("/blog")
def blog():
	return 'Bem vindo ao meu blog'''



# PyQt6
# 1. Janela Básica:

import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Básica")
        self.setGeometry(100, 100, 280, 80)
        label = QLabel('Olá Mundo!', self)
        label.move(100, 30)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    



#2. Botão com Mensagem:

import sys

from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton, QVBoxLayout, QMainWindow, QWidget, QMessageBox


class MainWindow(QMainWindow):
 def __init__(self):

    super().__init__()

    self.setWindowTitle("Entrada de Texto")

    self.setGeometry(100, 100, 300, 100)

    layout = QVBoxLayout()
 

    self.text_input = QLineEdit(self)

    layout.addWidget(self.text_input)

 

    button = QPushButton("Exibir Texto", self)
    button.clicked.connect(self.show_text)

    layout.addWidget(button)
 

    container = QWidget()

    container.setLayout(layout)

    self.setCentralWidget(container)


def show_text(self):

        text = self.text_input.text()

        QMessageBox.information(self, "Texto Digitado", text)


def main():

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()



#3. Botão Clicável:

import sys

from PyQt6.QtWidgets import QApplication, QPushButton, QMessageBox, QMainWindow


class MainWindow(QMainWindow):
 def __init__(self):

    super().__init__()

    self.setWindowTitle("Botão com Mensagem")

    self.setGeometry(100, 100, 280, 80)
    button = QPushButton('Clique aqui', self)

    button.clicked.connect(self.show_message)

    button.resize(100, 30)

    button.move(90, 20)


def show_message(self):

 QMessageBox.information(self, "Mensagem", "Você clicou no botão!")


def main():

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":

 main()