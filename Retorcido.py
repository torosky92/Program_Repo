import sys
import datetime, time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Settings import Settings
from SettingsUser import SettingsUs

from bin.pr.Remove_PR import RemoveDataPR
from bin.pr.Add_PR import AddDataPR
from bin.pr.Process_PR import ProcessPR
from bin.pr.Want_CodePR import WantCodePR
from bin.pr.Want_VapPR import WantVapPR
from bin.Main import Ui_MainWindow
from bin.MadeBy import MadeBy

from Controllers.pr.Comp_MPR import findMPR
from Controllers.pr.Comp_MPPR import findMPPR
from Controllers.port.RFID import Rfid


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.CB1_4.close()
        #----------------  Data Update  ----------------#
        #UpgradeData.Upgrade(self)
        # ----------------  Hide Vap  ----------------#
        self.VAP.close()
        # ----------------  Check if we want to vaporize  ----------------#
        self.VAP_2.stateChanged.connect(self.Want_to_find)
        # ----------------  Check if we want to vaporize  ----------------#
        self.VAP.stateChanged.connect(self.Want_Vap)
        # ----------------  Add Item to the list Proceso  ----------------#
        self.Proceso.addItem(Settings.Var_Process1())
        self.Proceso.addItem(Settings.Var_Process2())
        # ----------------  Push button for find User  ----------------#
        self.RFID.clicked.connect(self.USER)
        # ----------------  Push button for Change User  ----------------#
        #self.RFID_2.clicked.connect(self.Change_User)
        # ----------------  Push button for Time for a process  ----------------#
        #self.RFID_3.clicked.connect(self.TimeWork)
        # ----------------  Push button for New process  ----------------#
        self.NPRO.clicked.connect(self.NPROCESS)
        # ----------------  Push button for Process  ----------------#
        self.PRO.clicked.connect(self.PROCESS)
        # ----------------  Push button for help window  ----------------#
        #self.HELP.clicked.connect(self.Help_Me)
        #self.HELP2.clicked.connect(self.Help_Me)
        #self.HELP3.clicked.connect(self.Help_Me)
        # ----------------  Push button for New process  ----------------#
        self.HECHO.clicked.connect(self.MADE)
        # ----------------  Push button for Find Lote  ----------------#
        self.BUSCAR_2.clicked.connect(self.FindLote)
        # ----------------  Push button for Find Code Bar  ----------------#
        self.BUSCAR.clicked.connect(self.FindCodeBar)
        # ----------------  Push button for New process  ----------------#
        # self.ITEM.textChanged.connect(self.CANTIDADES)
        # ----------------  Push button for Configure PORT window  ----------------#
        # self.CONECT.clicked.connect(self.Configure_PORT)
        # ----------------  If label change Coils  ----------------#
        self.CB1_3.textChanged.connect(self.ChangeCoils)

    # ----------------  If you change text in the coils box   ----------------#
    def ChangeCoils(self):
        # ----------------  Check if you have Coils  ----------------#
        if self.Available < self.CB1_3.toPlainText():
            QMessageBox.about(self, "Redepesca",
                              "¡¡SOLO HAY EN ESTA " + str(self.PRESENTATION) + str(self.Available) + " DISPONIBLE!!")
        else:
            self.PT2.setText(str(int(self.CB1_3.toPlainText())+float(self.PUB.toPlainText())))
            # ----------------  Activate push button for add box and start tare  ----------------#
            self.ADIC_caja.setEnabled(True)
            self.IniciarTarar.setEnabled(True)

    # ----------------  If you push button find code bar  ----------------#
    def FindCodeBar(self):
        if self.TypeProcess == Settings.PP2():
            self.Available, self.Quantity, self.Weight, self.TotalWeight, self.TotalWeightR, self.Num_Coils, self.Num_CoilsR = ProcessPR.findBar(self,self.Provider,self.Presentation)
        if self.Num_Coils > 0:
            if self.Available:
                # ______________ Deactivate push button for find ______________ #
                self.VAP_2.setEnabled(False)
                self.PUB.setText("%.2f" % (self.Weight,))
                QMessageBox.about(self, "Redepesca", "¡¡SOLO HAY EN ESTA " + str(self.Presentation) + " " + str(Quantity) + " DISPONIBLE!!")
            else:
                QMessageBox.about(self, "Redepesca", "¡¡NO HAY BOBINA DISPONIBLE!!")
        else:
            QMessageBox.about(self, "Redepesca", "¡REFERENCIA NO DISPONIBLE!!")

    # ----------------  If you push button find lote  ----------------#
    def FindLote(self):
        if self.TypeProcess == Settings.PP2():
            self.CodeB, self.Provider, self.Presentation = ProcessPR.findLote(self)

    # ----------------  If you push button for New process  ----------------#
    def NPROCESS(self):
        self.Proc = "NEW PROCESS"
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