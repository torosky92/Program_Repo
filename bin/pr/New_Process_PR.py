from PyQt5 import QtWidgets
from Controllers.pr.Comp_MPR import findMPR
from Controllers.pr.Comp_MPPR import findMPPR
from bin.Main import Ui_MainWindow
from Settings import Settings

class NProcessPR(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def first(self):
        # ----------------  Find all lote and add in a list  ----------------#
        Ref = findMPR.FindAllItemMPR(str(self.Proceso.currentText()), Settings.Var_Comp9())
        if Ref != " ":
            # ----------------  Hide Lote Label  ----------------#
            self.MAQ_3.close()
            # ----------------  Activate push button for find Lote ----------------#
            self.BUSCAR_2.setEnabled(True)
            # ----------------  To unlock labels  ----------------#
            self.CB1_3.setReadOnly(False)
            # ----------------  Deactivate List proceso  ----------------#
            self.Proceso.setEnabled(False)
            # ----------------  Deactivate Push button for a Process  ----------------#
            self.PRO.setEnabled(False)
            self.NPRO.setEnabled(False)
            for x in range(len(Ref)): self.MAQ_3.addItem(str(Ref[x]))
            return Settings.PP()
        return " "

    def findLote(self):
        # ______________  Activate push button for find code bar  ______________ #
        self.BUSCAR.setEnabled(True)
        self.CB1_4.setReadOnly(True)
        # ______________  Find Provider, Reference and presentation through Lote  ______________ #
        PRO, REF, PRES = findMPR.FindObjMPR(str(self.Proceso.currentText()), str(self.CB1_2.toPlainText()))
        # ______________  Find code bar in a Base Data  ______________ #
        CB = findMPPR.FindObjMPPR(PRO, PRES, str(self.Proceso.currentText()), str(self.CB1_2.toPlainText()))
        # ______________  Add in a list all Code bar  ______________ #
        if self.VAP_2.isChecked() == False:
            for x in range(len(CB)): self.MAQ_2.addItem(str(CB[x]))
        # ______________  Write Reference box ______________ #
        self.REF1.setText(str(REF))
        # ______________ Add Item to the list Retiro ______________ #
        self.COB.addItem(Settings.PP3())
        self.COB.addItem(str(PRES))
        # ______________ Deactivate push button for find ______________ #
        self.CB1_2.setEnabled(False)
        self.BUSCAR_2.setEnabled(False)
        # ______________ Return ______________ #
        return (CB, PRO, PRES)

    def findBar(self, PROVIDER: str, PRESENTATION: str):
        # ____________ Find Quantity of the coils and total weight and if it's available _______________ #
        if self.VAP_2.isChecked(): NC, NCR, TW, TWR = findMPPR.FindESMPPR(PROVIDER, PRESENTATION, str(self.Proceso.currentText()),str(self.CB1_4.toPlainText()))
        else: NC, NCR, TW, TWR = findMPPR.FindESMPPR(PROVIDER, PRESENTATION, str(self.Proceso.currentText()),str(self.MAQ_2.currentText()))
        # ______________ Calculate ______________ #
        if NC > 0: Weight = TW / NC
        else: Weight = 0
        Quantity = NC - NCR
        if Quantity > 0: Available = True
        else: Available = False
        # ______________ Block Code Bar ________ #
        self.MAQ_2.setEnabled(False)
        self.CB1_4.setEnabled(False)
        self.BUSCAR.setEnabled(False)
        # ______________ Return ______________ #
        return (Available, Quantity, Weight, TW, TWR, NC, NCR)