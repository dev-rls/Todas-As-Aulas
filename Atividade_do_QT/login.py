# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(499, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tela_login = QFrame(self.centralwidget)
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
        self.lineEdit_2 = QLineEdit(self.tela_login)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(42, 160, 251, 31))
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit = QLineEdit(self.tela_login)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 100, 251, 31))
        self.lineEdit.setStyleSheet(u"border-color: rgb(170, 85, 255);")
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
        self.lineEdit_2.raise_()
        self.lineEdit.raise_()
        self.txt_login.raise_()
        self.txt_senha.raise_()
        self.txt_user.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.txt_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.txt_senha.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.txt_user.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.img.setText("")
    # retranslateUi

import login, sys
from login import Ui_MainWindow
 
if __name__=="__main__":
    app=QApplication(sys.argv)
    MainWindow=QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())