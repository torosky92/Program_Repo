import sys
import datetime, time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Settings import Settings
from SettingsUser import SettingsUs

from bin.pr.Initial_Code import InitialCode
from bin.pr.Change_PR import ChangePR
from bin.pr.CodeBr_PR import CodeBrPR
from bin.pr.Remove_PR import RemoveDataPR
from bin.pr.Add_PR import AddDataPR
from bin.pr.Process_PR import ProcessPR
from bin.pr.New_Process_PR import NProcessPR
from bin.pr.Want_CodePR import WantCodePR
from bin.pr.Want_VapPR import WantVapPR

from bin.Main import Ui_MainWindow
from bin.MadeBy import MadeBy

from Controllers.port.RFID import Rfid

# ________ This code is dedicated to a great man
# ________ and a great friend Christian Spiess to your memory
# ________ Thanks for all 18/09/2019

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # ________________ Action for options from interfaces _______________ #
        InitialCode.Inition(self)
        # _______________ Data Update _____________________ #
        #UpgradeData.Upgrade(self)

    def Add_Lote(self):
        AddDataPR.AddOrder(self)

    def ChangePresentation(self):
        if self.COB.currentText() == Settings.Var_P1() or self.COB.currentText() == Settings.Var_P2():
            self.CB1_3.setText(str(self.Quantity))

    # ----------------  If you change text in the coils box   ----------------#
    def ChangeCoils(self):
        ChangePR.ChangePre(self)

    # ----------------  If you push button find code bar  ----------------#
    def FindCodeBar(self):
        CodeBrPR.CodeBr_Push(self)

    # ----------------  If you push button find lote  ----------------#
    def FindLote(self):
        if self.TypeProcess == Settings.PP2():
            self.CodeB, self.Provider, self.Presentation = ProcessPR.findLote(self)
        else:
            self.CodeB, self.Provider, self.Presentation = NProcessPR.findLote(self)

    # ----------------  If you push button for New process  ----------------#
    def NPROCESS(self):
        self.TypeProcess = NProcessPR.first(self)
        if self.TypeProcess == " ":
            QMessageBox.about(self, Settings.Company(), Settings.Disavalible())

    # ----------------  If you push button for process  ----------------#
    def PROCESS(self):
        self.TypeProcess = ProcessPR.first(self)

    def Want_to_find(self):
        WantCodePR.find(self)

    # ----------------  If you select vaporize  ----------------#
    def Want_Vap(self):
        WantVapPR.Select(self)

    # ----------------  If you push button for user  ----------------#
    def USER(self):
        # ----------------  First time to add correct user  ----------------#
        if str(self.OP1.toPlainText()) == "" or str(self.OP1.toPlainText()) == SettingsUs.Var_KNOW():
            User, Permition, Access = Rfid.Rfid_Read(self, Settings.PRO3(),Settings.ACC2())
            AddDataPR.first(self, User, Access)
        # ----------------  If you want to delet all, first find a user permition  ----------------#
        else:
            User, Permition, Access = Rfid.Rfid_Read(self, Settings.PRO3(), Settings.ACC())
            RemoveDataPR.All(self, Access)

    # ----------------  If you push button for configure PORT  ----------------#
    #def Configure_PORT(self):
        #self.child_win = ConfCOM(self)
        #self.child_win.show()

    def Help_Me2(self):
        QMessageBox.about(self, Settings.Company(), Settings.HELP())

    def Help_Me3(self):
        QMessageBox.about(self, Settings.Company(), Settings.HELP2())

    # ----------------  If you push button for Help windows  ----------------#
    #def Help_Me(self):
        #self.child_win = HelpWindow(self)
        #self.child_win.show()

    # ----------------  If you push button for Made by David Toro  ----------------#
    def MADE(self):
        self.child_win = MadeBy(self)
        self.child_win.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())