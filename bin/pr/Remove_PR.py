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
            self.Quantity = 0
            self.OP1.clear()
            self.ANO.clear()
            self.MES.clear()
            self.DIA.clear()
            self.HORA.clear()
            self.MAQ_3.clear()
            self.MAQ_2.clear()
            self.CB1_3.clear()
            self.CB1_2.clear()
            self.CB1_4.clear()
            self.REF1.clear()
            self.COB.clear()
            self.PUB.clear()
            self.PT2.clear()
            self.PT.clear()
            self.MAQ.clear()
            self.PF.clear()
            self.PRO.setEnabled(False)
            self.NPRO.setEnabled(False)
            self.BUSCAR_2.setEnabled(False)
            self.BUSCAR.setEnabled(False)
            self.ADIC_caja.setEnabled(False)
            self.IniciarTarar.setEnabled(False)
            self.T1.setEnabled(False)
            self.IMP.setEnabled(False)
            self.STARTMONT.setEnabled(False)
            self.STARTMAQ.setEnabled(False)
            self.PAUSAMONT.setEnabled(False)
            self.PAUSAMAQ.setEnabled(False)
            self.IMP2.setEnabled(False)
            self.T2.setEnabled(False)
            self.Proceso.setEnabled(True)
            self.VAP.close()
        else:
            QMessageBox.about(self, "Redepesca", "!NO TIENES PERMISO PARA ELIMINAR¡")