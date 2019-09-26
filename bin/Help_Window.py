from PyQt5 import QtWidgets
from bin.com.Ayuda import Ui_Form

class HelpWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        Ui_Form.__init__(self)
        self.setupUi(self)
        self.LISTA.addItem("")
        conexiones = sqlite3.connect("lib/Inf.db")
        consultas = conexiones.cursor()

        consultas.execute("SELECT * FROM IMAGEN")
        columna = consultas.fetchall()
        for j in columna:
            self.LISTA.addItem(j[0])
        consultas.close()
        conexiones.close()
        self.LISTA.activated.connect(self.BUSCAR)
        self.SALIR.clicked.connect(self.SalirAyuda)

    def BUSCAR(self):
        # Obtener nombre de usuario
        nombre=str(self.LISTA.currentText())
        # Establecer conexión con la base de datos
        conexion = sqlite3.connect("lib/Inf.db")
        cursor = conexion.cursor()
        # Buscar usuario en la base de datos
        cursor.execute("SELECT * FROM IMAGEN WHERE NOMBRE = ?", (nombre,))
        resultado = cursor.fetchone()
        # Validar si se encontro algún resultado
        if resultado:
            # Cargar foto a un QPixmap
            foto = QPixmap()
            foto.loadFromData(resultado[1], "PNG", Qt.AutoColor)
                # Insertar foto en el QLabel
            self.IMAGEN.setPixmap(foto)
        else:
            self.IMAGEN.clear()
        # Cerrar la conexión con la base de datos
        cursor.close()
        conexion.close()

    def SalirAyuda(self):
        self.close()
