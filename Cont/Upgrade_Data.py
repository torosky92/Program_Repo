from bin.Down_Dropbox import DROPBOX_APP
from PyQt5.QtWidgets import QMessageBox
from Controllers.Comp_MFR import findMFR
from Controllers.COMP_MPR import findMPR
from Controllers.Comp_MR import findMONT
from Controllers.Comp_PP import findPP
from Controllers.Comp_TABLA import findTABLA
from Controllers.Comp_MPECR import findMPECR
from Controllers.Comp_MPEER import findMPEER
from Controllers.Comp_MPICR import findMPICR
from Controllers.Comp_MPIER import findMPIER
from Controllers.Comp_PM import findPM
from Controllers.Comp_P import findP

class UpgradeData:
    def Upgrade(self):
        Date_Down = DROPBOX_APP.Dropbox_Down()
        if Date_Down == False:
            QMessageBox.about(self, "Redepesca", "¡¡NO SE ENCUENTRA RED!! Se almacenara hasta que se encuentre señal")
        findMPIER.Check_And_Add_ListMPIER()
        findMPICR.Check_And_Add_ListMPICR()
        findMPEER.Check_And_Add_ListMPEER()
        findMPECR.Check_And_Add_ListMPECR()
        findTABLA.Check_And_Add_ListTALBA()
        findPP.Check_And_Add_ListPP()
        findMONT.Check_And_Add_ListMR()
        findMPR.Check_And_Add_ListMPR()
        findMFR.Check_And_Add_ListMFR()
        findP.Check_And_Add_ListP()
        findPM.Check_And_Add_ListPM()
        DROPBOX_APP.Dropbox_Up_doc("lib/CBDR.db",'/BaseDatosRetorcido.db')
        DROPBOX_APP.Dropbox_Up_doc("lib/RMAQ.db", '/RefereneciaMaquinas.db')
        return True