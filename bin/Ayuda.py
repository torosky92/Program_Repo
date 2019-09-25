# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ayuda.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(798, 600)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_76 = QtWidgets.QLabel(Form)
        self.label_76.setGeometry(QtCore.QRect(0, 0, 191, 101))
        self.label_76.setFrameShape(QtWidgets.QFrame.Box)
        self.label_76.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_76.setLineWidth(2)
        self.label_76.setText("")
        self.label_76.setPixmap(QtGui.QPixmap(":/cct/Imagenes/Logo.png"))
        self.label_76.setScaledContents(True)
        self.label_76.setObjectName("label_76")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 0, 611, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("background-color: rgb(57, 169, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setLineWidth(2)
        self.label.setMidLineWidth(0)
        self.label.setObjectName("label")
        self.IMAGEN = QtWidgets.QLabel(Form)
        self.IMAGEN.setGeometry(QtCore.QRect(10, 110, 771, 421))
        self.IMAGEN.setText("")
        self.IMAGEN.setTextFormat(QtCore.Qt.AutoText)
        self.IMAGEN.setScaledContents(True)
        self.IMAGEN.setObjectName("IMAGEN")
        self.SALIR = QtWidgets.QPushButton(Form)
        self.SALIR.setGeometry(QtCore.QRect(660, 550, 121, 31))
        self.SALIR.setObjectName("SALIR")
        self.LISTA = QtWidgets.QComboBox(Form)
        self.LISTA.setGeometry(QtCore.QRect(20, 550, 631, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.LISTA.setFont(font)
        self.LISTA.setObjectName("LISTA")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "                                           AYUDA"))
        self.SALIR.setText(_translate("Form", "Cerrar"))

import Imagenes_rc
