'''Biblioteca PyQt6'''

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class Janela(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Exemplo PyQt6')

        layout = QVBoxLayout()

        botao = QPushButton('Clique aqui')
        botao.clicked.connect(self.exibirMensagem)

        label = QLabel('')

        layout.addWidget(botao)
        layout.addWidget(label)

        self.setLayout(layout)

        self.label = label

    def exibirMensagem(self):
        self.label.setText('Olá, mundo!')

def main():
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

    