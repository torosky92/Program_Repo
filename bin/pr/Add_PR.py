import datetime, time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from bin.Main import Ui_MainWindow
from SettingsUser import SettingsUs
from bin.pr.More_Order import MoreOrderPR

class AddDataPR(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def first(self, User: str, Access: bool):
        if User != SettingsUs.Var_KNOW:
            self.OP1.setText(str(User))
            if Access:
                today = datetime.datetime.today()
                self.ANO.setText(str(today.year))
                self.MES.setText(str(today.month))
                self.DIA.setText(str(today.day))
                self.HORA.setText(str(time.strftime("%H:%M:%S")))
                self.PRO.setEnabled(True)
                self.NPRO.setEnabled(True)
            else:
                QMessageBox.about(self, "Redepesca", "!NO TIENES PERMISO PARA TRABAJAR¡")

    def AddOrder(self):
        MoreOrderPR.Add_More(self, "¿Seguro quieres adicionar este lote y Adicionar mas?")
        REFERENCE = str(self.REF1.toPlainText())
