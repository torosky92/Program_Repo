import serial, time
import numpy as np

from Settings import Settings
from sql.com.SQL_User import SQLUser
from sql.com.SQL_COM import SQLCOM
from PyQt5.QtWidgets import QMessageBox

class Rfid:
    def Rfid_Read(self, PROCESS: str):
        QMessageBox.about(self, "Redepesca", "Favor de Ingresar la tarjeta luego de Aceptar")
        COM = SQLCOM.FindCom(Settings.Dir_CN(), Settings.Var_Find1())
        try:
            Lecture = serial.Serial(str(COM), 9600, timeout=10)
            time.sleep(2)
            rawString = Lecture.readline()
            s, x, y, z = np.fromstring(rawString.decode('ascii', errors='replace'), sep=' ')
            codeU = str(int(s)) + " " + str(int(x)) + " " + str(int(y)) + " " + str(int(z))
            Lecture.close()
            return SQLUser.FindUser(Settings.Dir_OP(),codeU, PROCESS)
        except:
            return SQLUser.FindUser(Settings.Dir_OP(),'0')
    #def Rfid_Permition(self):