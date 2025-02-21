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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDateEdit,
    QDialogButtonBox, QFrame, QLabel, QLineEdit, QMainWindow,
    QRadioButton, QSizePolicy, QToolButton, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(493, 645)
        self.telaCadastro = QFrame(Form)
        self.telaCadastro.setObjectName(u"telaCadastro")
        self.telaCadastro.setGeometry(QRect(30, 30, 441, 591))
        self.telaCadastro.setStyleSheet(u"background-color: rgb(29, 29, 29);")
        self.telaCadastro.setFrameShape(QFrame.Shape.StyledPanel)
        self.telaCadastro.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_check = QCheckBox(self.telaCadastro)
        self.btn_check.setObjectName(u"btn_check")
        self.btn_check.setGeometry(QRect(330, 480, 76, 20))
        self.btn_check.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Times New Roman\";")
        self.input_endereco = QLineEdit(self.telaCadastro)
        self.input_endereco.setObjectName(u"input_endereco")
        self.input_endereco.setGeometry(QRect(20, 340, 391, 22))
        self.input_endereco.setStyleSheet(u"background-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);")
        self.txt_telefone = QLabel(self.telaCadastro)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setGeometry(QRect(20, 390, 61, 16))
        self.txt_telefone.setStyleSheet(u"font: 600 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Times New Roman\";")
        self.txt_formulario = QLabel(self.telaCadastro)
        self.txt_formulario.setObjectName(u"txt_formulario")
        self.txt_formulario.setGeometry(QRect(150, 30, 131, 16))
        self.txt_formulario.setStyleSheet(u"font: 16pt \"Segoe Script\";\n"
"color: rgb(255, 255, 127);")
        self.btn_feminino = QRadioButton(self.telaCadastro)
        self.btn_feminino.setObjectName(u"btn_feminino")
        self.btn_feminino.setGeometry(QRect(20, 240, 89, 20))
        self.btn_feminino.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Times New Roman\";")
        self.txt_nome = QLabel(self.telaCadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(20, 90, 49, 16))
        self.txt_nome.setStyleSheet(u"font: 10pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.input_tefefone = QLineEdit(self.telaCadastro)
        self.input_tefefone.setObjectName(u"input_tefefone")
        self.input_tefefone.setGeometry(QRect(20, 410, 391, 22))
        self.input_tefefone.setStyleSheet(u"background-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);")
        self.input_nome = QLineEdit(self.telaCadastro)
        self.input_nome.setObjectName(u"input_nome")
        self.input_nome.setGeometry(QRect(20, 110, 391, 22))
        self.input_nome.setStyleSheet(u"background-color: rgb(130, 130, 130);\n"
"color: rgb(255, 255, 255);")
        self.txt_endereco = QLabel(self.telaCadastro)
        self.txt_endereco.setObjectName(u"txt_endereco")
        self.txt_endereco.setGeometry(QRect(20, 320, 61, 16))
        self.txt_endereco.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Times New Roman\";")
        self.txt_sexo = QLabel(self.telaCadastro)
        self.txt_sexo.setObjectName(u"txt_sexo")
        self.txt_sexo.setGeometry(QRect(20, 220, 49, 16))
        self.txt_sexo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Times New Roman\";")
        self.btn_masculino = QRadioButton(self.telaCadastro)
        self.btn_masculino.setObjectName(u"btn_masculino")
        self.btn_masculino.setGeometry(QRect(20, 260, 89, 20))
        self.btn_masculino.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 9pt \"Times New Roman\";")
        self.btn_dateEdit = QDateEdit(self.telaCadastro)
        self.btn_dateEdit.setObjectName(u"btn_dateEdit")
        self.btn_dateEdit.setGeometry(QRect(20, 480, 281, 22))
        self.btn_dateEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(130, 130, 130);\n"
"font: 10pt \"Times New Roman\";")
        self.btn_outro = QRadioButton(self.telaCadastro)
        self.btn_outro.setObjectName(u"btn_outro")
        self.btn_outro.setGeometry(QRect(20, 280, 89, 20))
        self.btn_outro.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Times New Roman\";\n"
"")
        self.txt_ddn = QLabel(self.telaCadastro)
        self.txt_ddn.setObjectName(u"txt_ddn")
        self.txt_ddn.setGeometry(QRect(20, 460, 111, 16))
        self.txt_ddn.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_adicionar = QLabel(self.telaCadastro)
        self.txt_adicionar.setObjectName(u"txt_adicionar")
        self.txt_adicionar.setGeometry(QRect(20, 170, 81, 16))
        self.txt_adicionar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 10pt \"Times New Roman\";")
        self.btn_ficheiro = QToolButton(self.telaCadastro)
        self.btn_ficheiro.setObjectName(u"btn_ficheiro")
        self.btn_ficheiro.setGeometry(QRect(210, 170, 22, 22))
        self.btn_ficheiro.setStyleSheet(u"background-color: rgb(130, 130, 130);\n"
"background-color: rgb(255, 255, 255);")
        self.btn_ok_cancel = QDialogButtonBox(self.telaCadastro)
        self.btn_ok_cancel.setObjectName(u"btn_ok_cancel")
        self.btn_ok_cancel.setGeometry(QRect(140, 540, 156, 24))
        self.btn_ok_cancel.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_ok_cancel.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.txt_escolher = QLabel(self.telaCadastro)
        self.txt_escolher.setObjectName(u"txt_escolher")
        self.txt_escolher.setGeometry(QRect(140, 170, 49, 16))
        self.txt_escolher.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_check.setText(QCoreApplication.translate("Form", u"Concluir", None))
        self.input_endereco.setText(QCoreApplication.translate("Form", u"Insira seu endere\u00e7o", None))
        self.txt_telefone.setText(QCoreApplication.translate("Form", u"Telefone:", None))
        self.txt_formulario.setText(QCoreApplication.translate("Form", u"Formul\u00e1rio", None))
        self.btn_feminino.setText(QCoreApplication.translate("Form", u"Feminino", None))
        self.txt_nome.setText(QCoreApplication.translate("Form", u"Nome:", None))
        self.input_tefefone.setText(QCoreApplication.translate("Form", u"Insira seu telefone", None))
        self.input_nome.setText(QCoreApplication.translate("Form", u"Insira seu nome", None))
        self.txt_endereco.setText(QCoreApplication.translate("Form", u"Endere\u00e7o:", None))
        self.txt_sexo.setText(QCoreApplication.translate("Form", u"Sexo:", None))
        self.btn_masculino.setText(QCoreApplication.translate("Form", u"Masculino", None))
        self.btn_outro.setText(QCoreApplication.translate("Form", u"Outro", None))
        self.txt_ddn.setText(QCoreApplication.translate("Form", u"Data de Nascimento:", None))
        self.txt_adicionar.setText(QCoreApplication.translate("Form", u"Adicionar foto ", None))
        self.btn_ficheiro.setText(QCoreApplication.translate("Form", u"...", None))
        self.txt_escolher.setText(QCoreApplication.translate("Form", u"Escolher", None))
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