from PyQt5.QtWidgets import QMessageBox
from Controllers.com.Down_Dropbox import DROPBOX_APP
from Controllers.pr.Comp_MFR import findMFR
from Controllers.pr.Comp_MPR import findMPR
from Controllers.pr.Comp_MR import findMR
from Data.pr.Upgrade_BD_BDR import Upgrade
from Controllers.pr.Comp_T import findT
from Controllers.pr.Comp_MPPR import findMPPR
from Controllers.pr.Comp_PM import findPM
from Controllers.pr.Comp_P import findP
from Settings import Settings

class UpgradeData:
    def Upgrade(self):
        Date_Down = DROPBOX_APP.Dropbox_Down()
        if Date_Down == False:
            QMessageBox.about(self, "Redepesca", "¡¡NO SE ENCUENTRA RED!! Se almacenara hasta que se encuentre señal")
        #______________ UPGRADE BASE DATA FROM MATERIA PRIMA INGRESADA ___________
        Upgrade.UpgradeMP()
        Upgrade.UpgradeMPP(Settings.Var_EC())
        Upgrade.UpgradeMPP(Settings.Var_EE())
        Upgrade.UpgradeMPP(Settings.Var_IC())
        Upgrade.UpgradeMPP(Settings.Var_IE())
        #________ COMPARATE ALL SQL _____
        findMPPR.Check_And_Add_ListMPPR(Settings.Var_EC())
        findMPPR.Check_And_Add_ListMPPR(Settings.Var_EE())
        findMPPR.Check_And_Add_ListMPPR(Settings.Var_IC())
        findMPPR.Check_And_Add_ListMPPR(Settings.Var_IE())
        findMPR.Check_And_Add_ListMPR()
        findMFR.Check_And_Add_ListMFR()
        findMR.Check_And_Add_ListMR(Settings.Var_MR())
        findMR.Check_And_Add_ListMR(Settings.Var_PR())
        findT.Check_And_Add_ListT()
        findP.Check_And_Add_ListP()
        findPM.Check_And_Add_ListPM(Settings.Var_PP())
        findPM.Check_And_Add_ListPM(Settings.Var_PM())
        QMessageBox.about(self, "Redepesca", "Base de Datos Actualizado")
        DROPBOX_APP.Dropbox_Up(Settings.Dir_Send1(), Settings.Dir_Dest1())
        DROPBOX_APP.Dropbox_Up(Settings.Dir_Send2(), Settings.Dir_Dest2())