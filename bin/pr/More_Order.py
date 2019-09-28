from Settings import Settings
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Controllers.pr.Comp_MPR import findMPR
from Controllers.pr.Comp_MPPR import findMPPR
from bin.Main import Ui_MainWindow


class MoreOrderPR(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def Add_More(self, TextBOX: str):
        Accept = QMessageBox.question(self, Settings.Company(), TextBOX, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if Accept == QMessageBox.Yes:
            if self.TypeProcess == Settings.PP2():
                CoilsR, TWeightR = findMPR.Find_MPR(str(self.Proceso.currentText()), str(self.MAQ_3.currentText()))
            else:
                CoilsR, TWeightR = findMPR.Find_MPR(str(self.Proceso.currentText()), str(self.CB1_2.toPlainText()))
            Total_CoilsR = CoilsR + float(self.Num_CoilsR)
            Total_WeightR = TWeightR + float(self.TotalWeightR)
            if self.TypeProcess == Settings.PP2():
                findMPR.UpgradeMPR(str(self.Proceso.currentText()), str(self.MAQ_3.currentText()), Settings.Var_Comp7(), Total_CoilsR)
                findMPR.UpgradeMPR(str(self.Proceso.currentText()), str(self.MAQ_3.currentText()), Settings.Var_Comp5(), Total_WeightR)
            else:
                findMPR.UpgradeMPR(str(self.Proceso.currentText()), str(self.CB1_2.toPlainText()), Settings.Var_Comp7(), Total_CoilsR)
                findMPR.UpgradeMPR(str(self.Proceso.currentText()), str(self.CB1_2.toPlainText()), Settings.Var_Comp5(), Total_WeightR)
            if self.VAP_2.isChecked():
                NC, NCR, TW, TWR = findMPPR.FindESMPPR(self.Provider, self.Presentation,str(self.Proceso.currentText()), str(self.CB1_4.toPlainText()))
            else:
                NC, NCR, TW, TWR = findMPPR.FindESMPPR(self.Provider, self.Presentation, str(self.Proceso.currentText()), str(self.MAQ_2.currentText()))
            Total_CoilsR = NCR + float(self.Num_CoilsR)
            Total_WeightR = TWR + float(self.TotalWeightR)
            if self.TypeProcess == Settings.PP2():
                if self.VAP_2.isChecked():
                    findMPPR.UpgradeMPPR(self.Provider, self.Presentation, str(self.Proceso.currentText()),
                                         str(self.MAQ_3.currentText()), str(self.CB1_4.toPlainText()),
                                         Settings.Var_Comp7(), Total_CoilsR)
                    findMPPR.UpgradeMPPR(self.Provider, self.Presentation, str(self.Proceso.currentText()),
                                         str(self.MAQ_3.currentText()), str(self.CB1_4.toPlainText()),
                                         Settings.Var_Comp5(), Total_WeightR)
                else:
                    findMPPR.UpgradeMPPR(self.Provider, self.Presentation, str(self.Proceso.currentText()),
                                         str(self.MAQ_3.currentText()), str(self.MAQ_2.currentText()),
                                         Settings.Var_Comp7(), Total_CoilsR)
                    findMPPR.UpgradeMPPR(self.Provider, self.Presentation, str(self.Proceso.currentText()),
                                         str(self.MAQ_3.currentText()), str(self.MAQ_2.currentText()),
                                         Settings.Var_Comp5(), Total_WeightR)
            else:
                if self.VAP_2.isChecked():
                    findMPR.UpgradeMPPR(self.Provider, self.Presentation, str(self.Proceso.currentText()),
                                        str(self.CB1_2.toPlainText()), str(self.CB1_4.toPlainText()),
                                        Settings.Var_Comp7(), Total_CoilsR)
                    findMPR.UpgradeMPPR(self.Provider, self.Presentation, str(self.Proceso.currentText()),
                                        str(self.CB1_2.toPlainText()), str(self.CB1_4.toPlainText()),
                                        Settings.Var_Comp5(), Total_WeightR)
                else:
                    findMPR.UpgradeMPPR(self.Provider, self.Presentation, str(self.Proceso.currentText()),
                                        str(self.CB1_2.toPlainText()), str(self.MAQ_2.currentText()),
                                        Settings.Var_Comp7(), Total_CoilsR)
                    findMPR.UpgradeMPPR(self.Provider, self.Presentation, str(self.Proceso.currentText()),
                                        str(self.CB1_2.toPlainText()), str(self.MAQ_2.currentText()),
                                        Settings.Var_Comp5(), Total_WeightR)