# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CodigoColor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(756, 229)
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
        self.label.setGeometry(QtCore.QRect(190, 0, 571, 101))
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
        self.FINAL = QtWidgets.QPushButton(Form)
        self.FINAL.setEnabled(False)
        self.FINAL.setGeometry(QtCore.QRect(190, 170, 161, 41))
        self.FINAL.setStyleSheet("background-color: rgb(211, 211, 211);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cct/Imagenes/icons8-bandera-de-llegada-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FINAL.setIcon(icon)
        self.FINAL.setIconSize(QtCore.QSize(32, 32))
        self.FINAL.setAutoRepeat(False)
        self.FINAL.setAutoExclusive(False)
        self.FINAL.setObjectName("FINAL")
        self.HELP3 = QtWidgets.QPushButton(Form)
        self.HELP3.setGeometry(QtCore.QRect(430, 170, 151, 41))
        self.HELP3.setStyleSheet("background-color: rgb(211, 211, 211);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/cct/Imagenes/help_question_1566.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HELP3.setIcon(icon1)
        self.HELP3.setIconSize(QtCore.QSize(32, 32))
        self.HELP3.setObjectName("HELP3")
        self.CC1 = QtWidgets.QComboBox(Form)
        self.CC1.setGeometry(QtCore.QRect(290, 120, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.CC1.setFont(font)
        self.CC1.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.CC1.setEditable(False)
        self.CC1.setDuplicatesEnabled(False)
        self.CC1.setObjectName("CC1")
        self.label_33 = QtWidgets.QLabel(Form)
        self.label_33.setGeometry(QtCore.QRect(70, 120, 211, 41))
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
        self.label_33.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_33.setToolTip("")
        self.label_33.setStyleSheet("background-color: rgb(57, 169, 255);")
        self.label_33.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_33.setLineWidth(2)
        self.label_33.setMidLineWidth(0)
        self.label_33.setObjectName("label_33")
        self.CC2 = QtWidgets.QComboBox(Form)
        self.CC2.setGeometry(QtCore.QRect(420, 120, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.CC2.setFont(font)
        self.CC2.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.CC2.setEditable(False)
        self.CC2.setDuplicatesEnabled(False)
        self.CC2.setObjectName("CC2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "                                            LOTE:"))
        self.FINAL.setText(_translate("Form", "ACEPTAR"))
        self.HELP3.setText(_translate("Form", "Ayuda"))
        self.label_33.setText(_translate("Form", "Codigo de Colores:"))
import Imagenes_rc