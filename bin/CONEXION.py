# -*- coding: utf-8 -*-

# Form2 implementation generated from reading ui file 'CONEXION.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form2(object):
    def setupUi(self, Form2):
        Form2.setObjectName("Form2")
        Form2.resize(491, 352)
        Form2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Form2)
        self.label.setGeometry(QtCore.QRect(190, 0, 301, 101))
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
        self.label_76 = QtWidgets.QLabel(Form2)
        self.label_76.setGeometry(QtCore.QRect(0, 0, 191, 101))
        self.label_76.setFrameShape(QtWidgets.QFrame.Box)
        self.label_76.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_76.setLineWidth(2)
        self.label_76.setText("")
        self.label_76.setPixmap(QtGui.QPixmap(":/cct/Imagenes/Logo.png"))
        self.label_76.setScaledContents(True)
        self.label_76.setObjectName("label_76")
        self.label_25 = QtWidgets.QLabel(Form2)
        self.label_25.setGeometry(QtCore.QRect(10, 110, 161, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 142, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 142, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 142, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        self.label_25.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_25.setToolTip("")
        self.label_25.setStyleSheet("background-color: rgb(57, 169, 255);")
        self.label_25.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_25.setLineWidth(2)
        self.label_25.setMidLineWidth(0)
        self.label_25.setObjectName("label_25")
        self.SERIAL = QtWidgets.QComboBox(Form2)
        self.SERIAL.setGeometry(QtCore.QRect(170, 110, 91, 41))
        self.SERIAL.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.SERIAL.setEditable(False)
        self.SERIAL.setDuplicatesEnabled(False)
        self.SERIAL.setObjectName("SERIAL")
        self.label_26 = QtWidgets.QLabel(Form2)
        self.label_26.setGeometry(QtCore.QRect(10, 160, 161, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 142, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 142, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 142, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        self.label_26.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_26.setToolTip("")
        self.label_26.setStyleSheet("background-color: rgb(57, 169, 255);")
        self.label_26.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_26.setLineWidth(2)
        self.label_26.setMidLineWidth(0)
        self.label_26.setObjectName("label_26")
        self.SERIAL_2 = QtWidgets.QComboBox(Form2)
        self.SERIAL_2.setGeometry(QtCore.QRect(170, 160, 91, 41))
        self.SERIAL_2.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.SERIAL_2.setEditable(False)
        self.SERIAL_2.setDuplicatesEnabled(False)
        self.SERIAL_2.setObjectName("SERIAL_2")
        self.radioButton = QtWidgets.QRadioButton(Form2)
        self.radioButton.setGeometry(QtCore.QRect(330, 170, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.ACEPTAR = QtWidgets.QPushButton(Form2)
        self.ACEPTAR.setGeometry(QtCore.QRect(170, 280, 141, 41))
        self.ACEPTAR.setStyleSheet("background-color: rgb(211, 211, 211);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cct/Imagenes/accept.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ACEPTAR.setIcon(icon)
        self.ACEPTAR.setIconSize(QtCore.QSize(32, 32))
        self.ACEPTAR.setObjectName("ACEPTAR")
        self.CERRAR = QtWidgets.QPushButton(Form2)
        self.CERRAR.setGeometry(QtCore.QRect(330, 280, 141, 41))
        self.CERRAR.setStyleSheet("background-color: rgb(211, 211, 211);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/cct/Imagenes/1486564399-close_81512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CERRAR.setIcon(icon1)
        self.CERRAR.setIconSize(QtCore.QSize(32, 32))
        self.CERRAR.setObjectName("CERRAR")
        self.BUSCARCOM = QtWidgets.QPushButton(Form2)
        self.BUSCARCOM.setGeometry(QtCore.QRect(10, 280, 141, 41))
        self.BUSCARCOM.setStyleSheet("background-color: rgb(211, 211, 211);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/cct/Imagenes/embleminsyncsyncing_103746.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BUSCARCOM.setIcon(icon2)
        self.BUSCARCOM.setIconSize(QtCore.QSize(32, 32))
        self.BUSCARCOM.setObjectName("BUSCARCOM")
        self.label_27 = QtWidgets.QLabel(Form2)
        self.label_27.setGeometry(QtCore.QRect(10, 210, 161, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 142, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 142, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 142, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 169, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        self.label_27.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_27.setToolTip("")
        self.label_27.setStyleSheet("background-color: rgb(57, 169, 255);")
        self.label_27.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_27.setLineWidth(2)
        self.label_27.setMidLineWidth(0)
        self.label_27.setObjectName("label_27")
        self.TOKEN = QtWidgets.QTextEdit(Form2)
        self.TOKEN.setGeometry(QtCore.QRect(170, 210, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.TOKEN.setFont(font)
        self.TOKEN.setFrameShape(QtWidgets.QFrame.Box)
        self.TOKEN.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TOKEN.setLineWidth(2)
        self.TOKEN.setReadOnly(False)
        self.TOKEN.setObjectName("TOKEN")

        self.retranslateUi(Form2)
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form2", "CONFIGURACION Y CONEXION"))
        self.label.setText(_translate("Form2", "               CONEXIÓN"))
        self.label_25.setText(_translate("Form2", "LECTOR TARJETA:"))
        self.label_26.setText(_translate("Form2", "<html><head/><body><p align=\"center\">PESA:</p></body></html>"))
        self.radioButton.setText(_translate("Form2", "Desactivar pesa"))
        self.ACEPTAR.setText(_translate("Form2", "ACEPTAR"))
        self.CERRAR.setText(_translate("Form2", "CERRAR"))
        self.BUSCARCOM.setText(_translate("Form2", "BUSCAR"))
        self.label_27.setText(_translate("Form2", "<html><head/><body><p align=\"right\">TOKEN:</p></body></html>"))

import Imagenes_rc
