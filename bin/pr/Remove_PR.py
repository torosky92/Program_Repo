from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from bin.Main import Ui_MainWindow

class RemoveDataPR(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
    def All(self, Access: bool):
        if Access:
            self.OP1.clear()
            self.ANO.clear()
            self.MES.clear()
            self.DIA.clear()
            self.HORA.clear()
            self.PRO.setEnabled(False)
            self.NPRO.setEnabled(False)
        else:
            QMessageBox.about(self, "Redepesca", "!NO TIENES PERMISO PARA ELIMINAR¡")