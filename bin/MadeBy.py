from bin.QUIEN import Ui_Form3
from PyQt5 import  QtWidgets, QtCore, QtGui, QtWidgets

class MadeBy(QtWidgets.QMainWindow, Ui_Form3):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        Ui_Form3.__init__(self)
        self.setupUi(self)
        self.CERRAR.clicked.connect(self.Salir)

    def Salir(self):
        self.close()