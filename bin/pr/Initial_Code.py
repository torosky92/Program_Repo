from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Settings import Settings
from bin.Main import Ui_MainWindow

class InitialCode(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def Inition(self):
        self.CB1_4.close()
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
        # self.RFID_2.clicked.connect(self.Change_User)
        # ----------------  Push button for Time for a process  ----------------#
        # self.RFID_3.clicked.connect(self.TimeWork)
        # ----------------  Push button for New process  ----------------#
        self.NPRO.clicked.connect(self.NPROCESS)
        # ----------------  Push button for Process  ----------------#
        self.PRO.clicked.connect(self.PROCESS)
        # ----------------  Push button for help window  ----------------#
        # self.HELP.clicked.connect(self.Help_Me)
        # self.HELP2.clicked.connect(self.Help_Me)
        # self.HELP3.clicked.connect(self.Help_Me)
        # ___________________ Push button for help user __________________ #
        self.AYUDA_4.clicked.connect(self.Help_Me2)
        self.PHELP.clicked.connect(self.Help_Me3)
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
        # ________________ If Presentation change ________________ #
        self.COB.currentIndexChanged.connect(self.ChangePresentation)
        # ________________ Push button for add lote __________________ #
        self.ADIC_caja.clicked.connect(self.Add_Lote)