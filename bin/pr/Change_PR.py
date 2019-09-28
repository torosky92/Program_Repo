from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Settings import Settings
from bin.Main import Ui_MainWindow

class ChangePR(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def ChangePre(self):
        # ----------------  Check if you have Coils  ---------------- #
        try:
            if self.Quantity < int(self.CB1_3.toPlainText()):
                QMessageBox.about(self, Settings.Company(), "¡¡SOLO HAY EN ESTA " + str(self.Presentation) + " " + str(self.Quantity) + " DISPONIBLE!!")
            elif int(self.CB1_3.toPlainText()) > 0:
                self.WT = self.Weight * int(self.CB1_3.toPlainText())
                self.PT2.setText("%.2f" % (self.WT, ))
                # ----------------  Activate push button for add box and start tare  ----------------#
                self.VAP.show()
                self.ADIC_caja.setEnabled(True)
                self.IniciarTarar.setEnabled(True)
        except:
            return