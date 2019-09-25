import os, sys
import datetime, time
import numpy as np

from PyQt5 import  QtCore, QtGui, QtWidgets, QtSvg#, uic, QtGui
from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit, QMessageBox#, QPushButton, QApplication
from PyQt5.QtCore import QModelIndex, pyqtSignal, QByteArray, QIODevice, QBuffer, Qt
from PyQt5.QtGui import QIcon, QPixmap

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
from Cont.Upgrade_Data import UpgradeData
from bin.RFID import Rfid
from bin.GENERATOR_CODE import GeneratorCode
from bin.Main import Ui_MainWindow
from bin.Help_Window import HelpWindow
from bin.Conf_COM import ConfCOM
from bin.MadeBy import MadeBy

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #----------------  Data Update  ----------------#
        #UpgradeData.Upgrade(self)
        # ----------------  Block labels ----------------#
        self.CB1_3.setReadOnly(True)
        # ----------------  Hide Vap  ----------------#
        self.VAP.close()
        # ----------------  Check if we want to vaporize  ----------------#
        self.VAP.stateChanged.connect(self.Want_Vap)
        # ----------------  Add Item to the list Proceso  ----------------#
        self.Proceso.addItem("Normal")
        self.Proceso.addItem("Pruebas")
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
        # ----------------  To unlock labels  ----------------#
        self.CB1_3.setReadOnly(False)
        # ----------------  Find to coils and weight  ----------------#
        if self.PROVIDER == "ENKA":
            if self.PRESENTATION == "CAJAS":
                if self.Proc == "NEW PROCESS" and str(self.CB1_2.toPlainText()) != "":
                    self.Num_Coils, self.Num_CoilsR, self.TotalWeight, self.TotalWeightR = findMPECR.FindESMPECR(str(self.Proceso.currentText()), str(self.CB1_2.toPlainText()))
                else:
                    self.Num_Coils, self.Num_CoilsR, self.TotalWeight, self.TotalWeightR = findMPECR.FindESMPECR(str(self.Proceso.currentText()), str(self.MAQ_3.currentText()))
            else:
                if self.Proc == "NEW PROCESS" and str(self.CB1_2.toPlainText()) != "":
                    self.Num_Coils, self.Num_CoilsR, self.TotalWeight, self.TotalWeightR = findMPEER.FindESMPEER(str(self.Proceso.currentText()), str(self.CB1_2.toPlainText()))
                else:
                    self.Num_Coils, self.Num_CoilsR, self.TotalWeight, self.TotalWeightR = findMPEER.FindESMPEER(str(self.Proceso.currentText()), str(self.MAQ_3.currentText()))
        else:
            if self.PRESENTATION == "CAJAS":
                if self.Proc == "NEW PROCESS" and str(self.CB1_2.toPlainText()) != "":
                    self.Num_Coils, self.Num_CoilsR, self.TotalWeight, self.TotalWeightR = findMPICR.FindESMPICR(str(self.Proceso.currentText()), str(self.CB1_2.toPlainText()))
                else:
                    self.Num_Coils, self.Num_CoilsR, self.TotalWeight, self.TotalWeightR = findMPICR.FindESMPICR(str(self.Proceso.currentText()), str(self.MAQ_3.currentText()))
            else:
                if self.Proc == "NEW PROCESS" and str(self.CB1_2.toPlainText()) != "":
                    self.Num_Coils, self.Num_CoilsR, self.TotalWeight, self.TotalWeightR = findMPIER.FindESMPIER(str(self.Proceso.currentText()), str(self.CB1_2.toPlainText()))
                else:
                    self.Num_Coils, self.Num_CoilsR, self.TotalWeight, self.TotalWeightR = findMPIER.FindESMPIER(str(self.Proceso.currentText()), str(self.MAQ_3.currentText()))
        # ----------------  Calculate Weight and it's available  ----------------#
        self.Available = self.Num_Coils - self.Num_CoilsR
        self.Weight = self.TotalWeight / self.Num_Coils
        self.PUB.setText(str(self.Weight))
        if self.Available < 0:
            QMessageBox.about(self, "Redepesca", "¡¡NO HAY BOBINA DISPONIBLE!!")
        else:
            QMessageBox.about(self, "Redepesca", "¡¡SOLO HAY EN ESTA " + str(self.PRESENTATION) + str(self.Available) +" DISPONIBLE!!")

    # ----------------  If you push button find lote  ----------------#
    def FindLote(self):
        # ----------------  Check if you write a text in the box  ----------------#
        if (self.Proc == "NEW PROCESS" and str(self.CB1_2.toPlainText()) != "") or (
                self.Proc == "PROCESS" and str(self.MAQ_3.currentText())):
            # ----------------  Activate push button for find code bar  ----------------#
            self.BUSCAR.setEnabled(True)
            if self.Proc == "NEW PROCESS" and str(self.CB1_2.toPlainText()) != "":
                self.PROVIDER, self.REF, self.PRESENTATION = findMPR.FindObjMPR(str(self.Proceso.currentText()),
                                                                 str(self.CB1_2.toPlainText()))
            else:
                self.PROVIDER, self.REF, self.PRESENTATION = findMPR.FindObjMPR(str(self.Proceso.currentText()),
                                                                 str(self.MAQ_3.currentText()))
            # ----------------  Write Reference box  ----------------#
            self.REF1.setText(str(self.REF))
            # ----------------  Add Item to the list Retiro  ----------------#
            self.COB.addItem(str(self.PRESENTATION))
            self.COB.addItem("Bobina")
            # ----------------  Deactivate push button for find  ----------------#
            self.MAQ_3.setEnabled(False)
            self.CB1_2.setEnabled(False)
            # ----------------  Find Code Bar  ----------------#
            if self.PROVIDER == "ENKA":
                if self.PRESENTATION == "CAJAS":
                    if self.Proc == "NEW PROCESS" and str(self.CB1_2.toPlainText()) != "":
                        self.CodeB = findMPECR.FindObjMPECR(str(self.Proceso.currentText()), str(self.CB1_2.toPlainText()))
                    else:
                        self.CodeB = findMPECR.FindObjMPECR(str(self.Proceso.currentText()), str(self.MAQ_3.currentText()))
                else:
                    if self.Proc == "NEW PROCESS" and str(self.CB1_2.toPlainText()) != "":
                        self.CodeB = findMPEER.FindObjMPEER(str(self.Proceso.currentText()), str(self.CB1_2.toPlainText()))
                    else:
                        self.CodeB = findMPEER.FindObjMPEER(str(self.Proceso.currentText()), str(self.MAQ_3.currentText()))
            else:
                if self.PRESENTATION == "CAJAS":
                    if self.Proc == "NEW PROCESS" and str(self.CB1_2.toPlainText()) != "":
                        self.CodeB = findMPICR.FindObjMPICR(str(self.Proceso.currentText()), str(self.CB1_2.toPlainText()))
                    else:
                        self.CodeB = findMPICR.FindObjMPICR(str(self.Proceso.currentText()), str(self.MAQ_3.currentText()))
                else:
                    if self.Proc == "NEW PROCESS" and str(self.CB1_2.toPlainText()) != "":
                        self.CodeB = findMPIER.FindObjMPIER(str(self.Proceso.currentText()), str(self.CB1_2.toPlainText()))
                    else:
                        self.CodeB = findMPIER.FindObjMPIER(str(self.Proceso.currentText()), str(self.MAQ_3.currentText()))
            # ----------------  Add Item to the list code Bar  ----------------#
            for x in range(len(self.CodeB)):
                self.MAQ_2.addItem(str(self.CodeB))

    # ----------------  If you select vaporize  ----------------#
    def Want_Vap(self):
        # ----------------  If you check change label to say you want  ----------------#
        if self.VAP.isChecked():
            self.VAP.setText("VAPORIZAR")
        # ----------------  If you don't check change label to say you don't want  ----------------#
        else:
            self.VAP.setText("NO VAPORIZAR")

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
        self.Proc = "PROCESS"
        # ----------------  Activate List for lote  ----------------#
        self.MAQ_3.show()
        # ----------------  Activate push button for find Lote ----------------#
        self.BUSCAR_2.setEnabled(True)
        # ----------------  To unlock labels  ----------------#
        self.CB1_3.setReadOnly(False)
        # ----------------  Deactivate List proceso  ----------------#
        self.Proceso.setEnabled(False)
        # ----------------  Deactivate Push button for a Process  ----------------#
        self.NPRO.setEnabled(False)
        self.PRO.setEnabled(False)
        # ----------------  Find all lote and add in a list  ----------------#
        Ref = findMPR.FindAllItemMPR(str(self.Proceso.currentText()),"Numero de Remision")
        for x in range(len(Ref)):
            self.MAQ_3.addItem(str(Ref[x]))

    # ----------------  If you push button for user  ----------------#
    def USER(self):
        if str(self.OP1.toPlainText()) == "":
            User, Permition = Rfid.Rfid_Read(self)
            today = datetime.datetime.today()
            if User != "No encontrado":
                self.OP1.setText(str(User))
                self.ANO.setText(str(today.year))
                self.MES.setText(str(today.month))
                self.DIA.setText(str(today.day))
                self.HORA.setText(str(time.strftime("%H:%M:%S")))
        self.PRO.setEnabled(True)
        self.NPRO.setEnabled(True)

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