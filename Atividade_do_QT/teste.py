from PySide6.QtCore import (
    QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt
)
from PySide6.QtGui import (
    QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform
)
from PySide6.QtWidgets import (
    QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget
)
import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tela_login = QFrame(self.centralwidget)
        self.tela_login.setObjectName("tela_login")
        self.tela_login.setGeometry(QRect(150, 70, 341, 301))
        self.tela_login.setStyleSheet("background-color: rgb(102, 102, 102);")
        self.tela_login.setFrameShape(QFrame.StyledPanel)
        self.tela_login.setFrameShadow(QFrame.Raised)

        self.btn_entrar = QPushButton(self.tela_login)
        self.btn_entrar.setObjectName("btn_entrar")
        self.btn_entrar.setGeometry(QRect(130, 220, 75, 24))
        self.btn_entrar.setStyleSheet("""
            background-color: rgb(85, 170, 255);
            font: 10pt 'Segoe UI';
            color: rgb(255, 255, 255);
        """)

        self.lineEdit_2 = QLineEdit(self.tela_login)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(42, 160, 251, 31))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.lineEdit = QLineEdit(self.tela_login)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(QRect(40, 100, 251, 31))
        self.lineEdit.setStyleSheet("border-color: rgb(170, 85, 255);")

        self.txt_login = QLabel(self.tela_login)
        self.txt_login.setObjectName("txt_login")
        self.txt_login.setGeometry(QRect(130, 30, 61, 31))
        self.txt_login.setStyleSheet("""
            font: 600 14pt 'Segoe UI';
            background-color: rgba(0, 0, 0, 0);
            color: rgb(255, 255, 127);
            font: 16pt 'Segoe Print';
        """)
        self.txt_login.setScaledContents(True)

        self.txt_senha = QLabel(self.tela_login)
        self.txt_senha.setObjectName("txt_senha")
        self.txt_senha.setGeometry(QRect(40, 140, 49, 16))
        self.txt_senha.setStyleSheet("""
            font: 600 10pt 'Segoe UI';
            background-color: rgba(0, 0, 0, 0);
            color: rgb(255, 255, 255);
        """)

        self.label_2 = QLabel(self.tela_login)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(50, 110, 101, 16))
        self.label_2.setStyleSheet("color: rgb(127, 127, 127);")

        self.txt_texto = QLabel(self.tela_login)
        self.txt_texto.setObjectName("txt_texto")
        self.txt_texto.setGeometry(QRect(50, 170, 91, 16))
        self.txt_texto.setStyleSheet("color: rgb(127, 127, 127);")

        self.txt_user = QLabel(self.tela_login)
        self.txt_user.setObjectName("txt_user")
        self.txt_user.setGeometry(QRect(40, 80, 49, 16))
        self.txt_user.setStyleSheet("""
            color: rgb(255, 255, 255);
            font: 600 10pt 'Segoe UI';
            background-color: rgba(0, 0, 0, 0);
        """)

        self.img = QLabel(self.tela_login)
        self.img.setObjectName("img")
        self.img.setGeometry(QRect(0, 0, 361, 301))
        self.img.setPixmap(QPixmap(":/icon/img.png"))
        self.img.setScaledContents(True)
        self.img.setWordWrap(True)
        self.img.setOpenExternalLinks(True)

        self.img.raise_()
        self.btn_entrar.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit.raise_()
        self.txt_login.raise_()
        self.txt_senha.raise_()
        self.label_2.raise_()
        self.txt_texto.raise_()
        self.txt_user.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.btn_entrar.setText(QCoreApplication.translate("MainWindow", "Entrar", None))
        self.txt_login.setText(QCoreApplication.translate("MainWindow", "Login", None))
        self.txt_senha.setText(QCoreApplication.translate("MainWindow", "Senha", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Digite seu usuário", None))
        self.txt_texto.setText(QCoreApplication.translate("MainWindow", "Digite sua senha", None))
        self.txt_user.setText(QCoreApplication.translate("MainWindow", "Usuário", None))
        self.img.setText("")

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
