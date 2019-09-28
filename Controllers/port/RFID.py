import serial, time
import numpy as np

from Settings import Settings
from SettingsUser import SettingsUs
from sql.com.SQL_User import SQLUser
from sql.com.SQL_COM import SQLCOM
from PyQt5.QtWidgets import QMessageBox
from sql.com.SQL_PASS import SQLPERMITION

class Rfid:

    def Rfid_Read(self, PROCESS: str, TYPEACCESS: str):
        if TYPEACCESS == Settings.ACC2():
            Accept = QMessageBox.question(self, Settings.Company(), "Favor de Ingresar la tarjeta luego de Aceptar",
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        else:
            Accept = QMessageBox.question(self, Settings.Company(), "¿Seguro quieres Cancelar TODO LO INGRESADO? (Si se acepta favor de ingresar la tarjeta)",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        COM = SQLCOM.FindCom(Settings.Dir_CN(), Settings.Var_Find1())
        if Accept == QMessageBox.Yes:
            try:
                Lecture = serial.Serial(str(COM), 9600, timeout=10)
                time.sleep(2)
                rawString = Lecture.readline()
                s, x, y, z = np.fromstring(rawString.decode('ascii', errors='replace'), sep=' ')
                codeU = str(int(s)) + " " + str(int(x)) + " " + str(int(y)) + " " + str(int(z))
                Lecture.close()
                User, Permition = SQLUser.FindUser(Settings.Dir_OP(),codeU, PROCESS)
                if TYPEACCESS == Settings.ACC2():
                    Access = SQLPERMITION.FindPermition(Settings.Dir_PW(),Settings.Var_Comp15())
                elif TYPEACCESS == Settings.ACC():
                    Access = SQLPERMITION.FindPermition(Settings.Dir_PW(), Settings.Var_Comp31())
                if Permition >= Access:
                    return (User, Permition, True)
                else:
                    return (User, Permition, False)
            except:
                return (SettingsUs.Var_KNOW(), 0, False)
        else:
            return (SettingsUs.Var_KNOW(), 0, False)

    #def Rfid_Permition(self):