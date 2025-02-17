# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QLabel, QLineEdit, QPushButton, QRadioButton, QMainWindow,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(493, 683)
        self.telaCadastro = QFrame(Form)
        self.telaCadastro.setObjectName(u"telaCadastro")
        self.telaCadastro.setGeometry(QRect(10, 30, 441, 531))
        self.telaCadastro.setStyleSheet(u"background-color: rgb(102, 102, 102);")
        self.telaCadastro.setFrameShape(QFrame.Shape.StyledPanel)
        self.telaCadastro.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton = QPushButton(self.telaCadastro)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 500, 75, 24))
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.checkBox = QCheckBox(self.telaCadastro)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(330, 420, 76, 20))
        self.checkBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Times New Roman\";")
        self.lineEdit_2 = QLineEdit(self.telaCadastro)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 180, 391, 22))
        self.label_5 = QLabel(self.telaCadastro)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 330, 61, 16))
        self.label_5.setStyleSheet(u"font: 600 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Times New Roman\";")
        self.label = QLabel(self.telaCadastro)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 30, 131, 16))
        self.label.setStyleSheet(u"font: 16pt \"Segoe Script\";\n"
"color: rgb(255, 255, 127);")
        self.radioButton = QRadioButton(self.telaCadastro)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 250, 89, 20))
        self.radioButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Times New Roman\";")
        self.label_2 = QLabel(self.telaCadastro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 90, 49, 16))
        self.label_2.setStyleSheet(u"font: 10pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_3 = QLineEdit(self.telaCadastro)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 350, 391, 22))
        self.lineEdit = QLineEdit(self.telaCadastro)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 110, 391, 22))
        self.label_3 = QLabel(self.telaCadastro)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 160, 61, 16))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Times New Roman\";")
        self.label_4 = QLabel(self.telaCadastro)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 230, 49, 16))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Times New Roman\";")
        self.radioButton_2 = QRadioButton(self.telaCadastro)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(20, 270, 89, 20))
        self.radioButton_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 9pt \"Times New Roman\";")
        self.dateEdit = QDateEdit(self.telaCadastro)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(20, 420, 281, 22))
        self.dateEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Times New Roman\";")
        self.radioButton_3 = QRadioButton(self.telaCadastro)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(20, 290, 89, 20))
        self.radioButton_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Times New Roman\";\n"
"")
        self.label_6 = QLabel(self.telaCadastro)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 400, 111, 16))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Sair", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Concluir", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Telefone:", None))
        self.label.setText(QCoreApplication.translate("Form", u"Formul\u00e1rio", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"Feminino", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nome:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Endere\u00e7o:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Sexo:", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"Masculino", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"Outro", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Data de Nascimento:", None))
    # retranslateUi

import registro, sys
from registro import Ui_Form

if __name__=="__main__":
    app=QApplication(sys.argv)
    Form = QMainWindow()  
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
