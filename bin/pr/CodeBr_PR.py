from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from bin.pr.Process_PR import ProcessPR
from bin.pr.New_Process_PR import NProcessPR

from bin.Main import Ui_MainWindow
from Settings import Settings

class CodeBrPR(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def CodeBr_Push(self):
        if self.TypeProcess == Settings.PP2():
            self.Available, self.Quantity, self.Weight, self.TotalWeight, self.TotalWeightR, self.Num_Coils, self.Num_CoilsR = ProcessPR.findBar(self,self.Provider,self.Presentation)
        else:
            self.Available, self.Quantity, self.Weight, self.TotalWeight, self.TotalWeightR, self.Num_Coils, self.Num_CoilsR = NProcessPR.findBar(self, self.Provider, self.Presentation)
        if self.Num_Coils > 0:
            if self.Available:
                # ______________ Deactivate push button for find ______________ #
                self.VAP_2.setEnabled(False)
                self.PUB.setText("%.2f" % (self.Weight,))
                QMessageBox.about(self, Settings.Company(), "¡¡SOLO HAY EN ESTA " + str(self.Presentation) + " " + str(self.Quantity) + " DISPONIBLE!!")
            else:
                QMessageBox.about(self, Settings.Company(), "¡¡NO HAY BOBINA DISPONIBLE!!")
        else:
            QMessageBox.about(self, Settings.Company(), "¡REFERENCIA NO DISPONIBLE!!")