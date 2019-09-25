from bin.CONEXION import Ui_Form2
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox

class ConfCOM(QtWidgets.QMainWindow, Ui_Form2):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        Ui_Form2.__init__(self)
        self.setupUi(self)

        self.CERRAR.clicked.connect(self.Salir)
        self.BUSCARCOM.clicked.connect(self.BUSCAR)
        self.ACEPTAR.clicked.connect(self.OK)

    def OK(self):
        global contra
        buscarContra()
        text, ok = QInputDialog.getText(None, "Ingresar Contraseña", "Contraseña:",
                                        QLineEdit.Password)
        guardar = 0
        if text == contra:
            if (str(self.SERIAL.currentText()) != ""):
                eliminarsql("lib/CN.db", "CONEXION")
                conexiones = sqlite3.connect("lib/CN.db")
                consultas = conexiones.cursor()
                consultas.execute("INSERT INTO CONEXION VALUES (?, ?)", (str(self.SERIAL.currentText()), 1))
                conexiones.commit()
                consultas.close()
                conexiones.close()
                guardar = 1
            else:
                QMessageBox.about(self, "Redepesca", "No se almaceno conexion")
            if (str(self.TOKEN.toPlainText()) != ""):
                conexiones = sqlite3.connect("lib/PW.db")
                consultas = conexiones.cursor()
                consultas.execute("INSERT INTO LINK VALUES (?)",
                                  (str(self.TOKEN.currentText())))
                conexiones.commit()
                consultas.close()
                conexiones.close()
                if (check.revisar() == True):
                    dbx = dropbox.Dropbox(str(self.TOKEN.currentText()))
                    with open("lib/PW.db", "rb") as f:
                        dbx.files_upload(f.read(), '/Password.db', dropbox.files.WriteMode.overwrite)
                guardar = 1
            else:
                QMessageBox.about(self, "Redepesca", "No se almaceno token")
            if (guardar == 1):
                self.close()
        else:
            QMessageBox.about(self, "Redepesca", "!!ERROR¡¡ Contraseña incorrecta")

    def Salir(self):
        self.close()

    def BUSCAR(self):
        # texto='/dev/ttyACM'
        # texto='/dev/ttyUSB'
        texto = 'COM'
        bEncontrado = False
        self.SERIAL.clear()
        self.SERIAL.addItem("")
        for iPuerto in range(0, 50):
            try:
                # Puerto que vamos a probar
                PUERTO = texto + str(iPuerto)
                # Velocidad
                VELOCIDAD = '9600'
                # Probamos ha abrir el puerto
                Arduino = serial.Serial(PUERTO, VELOCIDAD)
                # si no se ha producido un error, cerramos el puerto
                Arduino.close()
                # cambiamos el estado del la variable para saber si lo hemos encontrado
                bEncontrado = True
                self.SERIAL.addItem(PUERTO)
                # Salimos del bucle
            except:
                # Si hay error, no hacemos nada y continuamos con la busqueda
                pass
        if (bEncontrado == False):
            QMessageBox.about(self, "Redepesca", "No se ha encontrado Conexion")