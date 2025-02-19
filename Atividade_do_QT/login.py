
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)

from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, 
    QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform)

from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(499, 400)
        self.tela_principal = QWidget(MainWindow)
        self.tela_principal.setObjectName(u"tela_principal")
        self.tela_login = QFrame(self.tela_principal)
        self.tela_login.setObjectName(u"tela_login")
        self.tela_login.setGeometry(QRect(70, 70, 341, 301))
        self.tela_login.setStyleSheet(u"background-color: rgb(102, 102, 102);")
        self.tela_login.setFrameShape(QFrame.Shape.StyledPanel)
        self.tela_login.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_entrar = QPushButton(self.tela_login)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setGeometry(QRect(130, 220, 75, 24))
        self.btn_entrar.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.input_senha = QLineEdit(self.tela_login)
        self.input_senha.setObjectName(u"input_senha")
        self.input_senha.setGeometry(QRect(42, 160, 251, 31))
        self.input_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_usuario = QLineEdit(self.tela_login)
        self.input_usuario.setObjectName(u"input_usuario")
        self.input_usuario.setGeometry(QRect(40, 100, 251, 31))
        self.input_usuario.setStyleSheet(u"border-color: rgb(170, 85, 255);")
        self.txt_login = QLabel(self.tela_login)
        self.txt_login.setObjectName(u"txt_login")
        self.txt_login.setGeometry(QRect(130, 30, 61, 31))
        self.txt_login.setStyleSheet(u"font: 600 14pt \"Segoe UI\";\n"
"font: 600 9pt \"Segoe UI\";\n"
"font: 11pt \"Segoe UI\";\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 127);\n"
";\n"
"font: 16pt \"Segoe Print\";\n"
"")
        self.txt_login.setScaledContents(True)
        self.txt_senha = QLabel(self.tela_login)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(40, 140, 49, 16))
        self.txt_senha.setStyleSheet(u"font: 600 10pt \"Segoe UI\";\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.txt_user = QLabel(self.tela_login)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setGeometry(QRect(40, 80, 49, 16))
        self.txt_user.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 600 10pt \"Segoe UI\";\n"
"background-color: rgba(0, 0, 0, 0);")
        self.img = QLabel(self.tela_login)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(0, 0, 361, 301))
        self.img.setPixmap(QPixmap(u":/icon/img.png"))
        self.img.setScaledContents(True)
        self.img.setWordWrap(True)
        self.img.setOpenExternalLinks(True)
        self.img.raise_()
        self.btn_entrar.raise_()
        self.input_senha.raise_()
        self.input_usuario.raise_()
        self.txt_login.raise_()
        self.txt_senha.raise_()
        self.txt_user.raise_()
        MainWindow.setCentralWidget(self.tela_principal)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
  
        self.btn_entrar.clicked.connect(self.check_login)
   
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.txt_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.txt_senha.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.txt_user.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.img.setText("")
 
    def check_login(self):
        correct_username = "raquel"
        correct_password = "123456"

        username = self.input_usuario.text()
        password = self.input_senha.text()

        if username == correct_username and password == correct_password:
            print("Login bem-sucedido! Carregando...")
        else:
            print("Usuário ou senha inválido.")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
