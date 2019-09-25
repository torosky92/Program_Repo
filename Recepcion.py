#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Añadir libreria
import sqlite3, datetime, time, serial
import os, sys
import numpy as np
#from bin.Imagenes_rc import Imagenes_rc
import barcode
import dropbox
import tempfile
from barcode.writer import ImageWriter
#Libreria de PyQt para la visualizacion
from PyQt5 import  QtWidgets, QtCore, QtGui, QtWidgets, QtSvg#, uic, QtGui
from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit, QMessageBox#, QPushButton, QApplication
from PyQt5.QtCore import QModelIndex, pyqtSignal, QByteArray, QIODevice, QBuffer, Qt
from PyQt5.QtGui import QIcon, QPixmap

#LandingProveDe, LandingProveBase = uic.loadUiType("Ayuda.ui")
from bin.Main import Ui_MainWindow
from bin.Ayuda import Ui_Form
from bin.CONEXION import Ui_Form2
from bin.QUIEN import Ui_Form3
from bin.check import revisar

def PWtoken(self):
    global token
    conexiones = sqlite3.connect("lib/PW.db")
    consultas = conexiones.cursor()
    consultas.execute("SELECT * FROM LINK")
    columna = consultas.fetchall()
    for j in columna:
        token=(j[0])
    consultas.close()
    conexiones.close()

def tablaNueva(self):
    eliminarsql("lib/CBD.db", "TABLA")
    self.TABLARECEPCION.clear()
    self.TABLARECEPCION.setHorizontalHeaderLabels(['Codigo de barras.', 'Numero de Bobinas', 'Peso neto', 'U. Medida'])
        
    conexiones = sqlite3.connect("lib/CBD.db")
    consultas = conexiones.cursor()
    consultas.execute("SELECT * FROM PROCESO_INGRESO")
    columna = consultas.fetchall()
    for j in columna:
        consultas.execute("INSERT INTO TABLA VALUES (?, ?, ?, ?)",(str(j[1]), float(j[5]), float(j[6]), str(j[7])))
    conexiones.commit()
    consultas.close()
    conexiones.close()

    conexiones = sqlite3.connect("lib/CBD.db")
    consultas = conexiones.cursor()
    consultas.execute("SELECT * FROM TABLA")
    for fila_numero, fila_data in enumerate(consultas):
        self.TABLARECEPCION.insertRow(fila_numero)
        for columna_numero, data in enumerate(fila_data):
              self.TABLARECEPCION.setItem(fila_numero, columna_numero, QtWidgets.QTableWidgetItem(str(data)))
    
    consultas.close()
    conexiones.close()

def procesoIng(self,insertar):
    global Numero_pedido   
    conexiones = sqlite3.connect("lib/CBD.db")
    consultas = conexiones.cursor()
    if (str(self.PRESENTACION.currentText())=="ESTIBAS"):
        if (str(self.PROVEEDOR.currentText())=="ENKA"):
            consultas.execute("SELECT * FROM MATERIA_PRIMA_ENKA_ESTIBAS")
        else:
            consultas.execute("SELECT * FROM MATERIA_PRIMA_IMPORTADO_ESTIBAS")
    else:
        if (str(self.PROVEEDOR.currentText())=="ENKA"):
            consultas.execute("SELECT * FROM MATERIA_PRIMA_ENKA_CAJA")
        else:
            consultas.execute("SELECT * FROM MATERIA_PRIMA_IMPORTADO_CAJA")
    columna = consultas.fetchall()
    Ref=0
    for j in columna:
        Ref=int(j[0])+1
    if(Ref==0):
        Ref=1
    consultas.close()
    conexiones.close()
    codigoviejo=[]
    if(insertar==True):
        conexiones = sqlite3.connect("lib/CBD.db")
        consultas = conexiones.cursor()
        consultas.execute("SELECT * FROM PROCESO_INGRESO")
        Numero_pedido=0
        columna = consultas.fetchall()
        for j in columna:
            Ref=int(j[0])+1
            Numero_pedido+=1
        consultas.execute("INSERT INTO PROCESO_INGRESO VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (Ref, str(self.BARRAS.toPlainText()), str(self.N_REP.toPlainText()), str(self.REMISION.toPlainText()), Numero_pedido, str(self.BOBINAS.toPlainText()), float(self.PESO_2.toPlainText()),str(self.UNIDAD.currentText())))
        conexiones.commit()
        consultas.close()
        conexiones.close()

        conexiones = sqlite3.connect("lib/CBD.db")
        consultas = conexiones.cursor()
        consultas.execute("SELECT * FROM PROCESO_INGRESO")
        columna = consultas.fetchall()
        for j in columna:
            codigoviejo.append(str(j[1]))
        pasar=0
        for j in columna:
            pasar+=1
            Ref+=1
            consultas = conexiones.execute("UPDATE PROCESO_INGRESO SET NUMERO_PEDIDO=? WHERE CODIGO_DE_BARRAS=?", 
                                            (pasar, codigoviejo[pasar-1]))
            consultas = conexiones.execute("UPDATE PROCESO_INGRESO SET REF=? WHERE CODIGO_DE_BARRAS=?", 
                                            (Ref, codigoviejo[pasar-1]))
    else:
        conexiones = sqlite3.connect("lib/CBD.db")
        consultas = conexiones.cursor()
        consultas.execute("SELECT * FROM PROCESO_INGRESO")
        columna = consultas.fetchall()
        for j in columna:
            codigoviejo.append(int(j[1]))
        pasar=0
        for j in columna:
            pasar+=1
            Ref+=1
            consultas = conexiones.execute("UPDATE PROCESO_INGRESO SET NUMERO_PEDIDO=? WHERE CODIGO_DE_BARRAS=?", 
                                            (pasar, codigoviejo[pasar-1]))
            consultas = conexiones.execute("UPDATE PROCESO_INGRESO SET REF=? WHERE CODIGO_DE_BARRAS=?", 
                                            (Ref, codigoviejo[pasar-1]))
    conexiones.commit()
    consultas.close()
    conexiones.close()
    tablaNueva(self)

def ingresarMateria(self):
    global Numero_pedido   
    conexiones = sqlite3.connect("lib/CBD.db")
    consultas = conexiones.cursor()
    if (str(self.PRESENTACION.currentText())=="ESTIBAS"):
        if (str(self.PROVEEDOR.currentText())=="ENKA"):
            consultas.execute("SELECT * FROM MATERIA_PRIMA_ENKA_ESTIBAS")
        else:
            consultas.execute("SELECT * FROM MATERIA_PRIMA_IMPORTADO_ESTIBAS")
    else:
        if (str(self.PROVEEDOR.currentText())=="ENKA"):
            consultas.execute("SELECT * FROM MATERIA_PRIMA_ENKA_CAJA")
        else:
            consultas.execute("SELECT * FROM MATERIA_PRIMA_IMPORTADO_CAJA")
    columna = consultas.fetchall()
    Ref=0
    for j in columna:
        Ref=int(j[0])
    if(Ref==0):
        Ref+=1
    consultas.close()
    conexiones.close()

    RefC=[]
    CBC=[]
    NDREC=[]
    NDRC=[]
    NDPC=[]
    NDBC=[]
    PEC=[]
    UDMC=[]

    conexiones = sqlite3.connect("lib/CBD.db")
    consultas = conexiones.cursor()
    consultas.execute("SELECT * FROM PROCESO_INGRESO")
    columna = consultas.fetchall()
    for j in columna:
        RefC.append(int(j[0]))
        CBC.append(str(j[1]))
        NDREC.append(str(j[2]))
        NDRC.append(str(j[3]))
        NDPC.append(float(j[4]))
        NDBC.append(int(j[5]))
        PEC.append(float(j[6]))
        UDMC.append(str(j[7]))
    consultas.close()
    conexiones.close()

    conexiones = sqlite3.connect("lib/CBD.db")
    consultas = conexiones.cursor()
    tama=len(RefC)
    tama2=Ref+tama
    imp=0
    for j in range(Ref, tama2):
        if (str(self.PRESENTACION.currentText())=="ESTIBAS"):
            if (str(self.PROVEEDOR.currentText())=="ENKA"):
                consultas.execute("INSERT INTO MATERIA_PRIMA_ENKA_ESTIBAS VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(RefC[imp], CBC[imp], NDREC[imp], NDRC[imp], NDPC[imp], NDBC[imp], PEC[imp], UDMC[imp]))
            else:
                consultas.execute("INSERT INTO MATERIA_PRIMA_IMPORTADO_ESTIBAS VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(RefC[imp], CBC[imp], NDREC[imp], NDRC[imp], NDPC[imp], NDBC[imp], PEC[imp], UDMC[imp]))
        else:
            if (str(self.PROVEEDOR.currentText())=="ENKA"):
                consultas.execute("INSERT INTO MATERIA_PRIMA_ENKA_CAJA VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(RefC[imp], CBC[imp], NDREC[imp], NDRC[imp], NDPC[imp], NDBC[imp], PEC[imp], UDMC[imp]))
            else:
                consultas.execute("INSERT INTO MATERIA_PRIMA_IMPORTADO_CAJA VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(RefC[imp], CBC[imp], NDREC[imp], NDRC[imp], NDPC[imp], NDBC[imp], PEC[imp], UDMC[imp]))  
        imp+=1
    conexiones.commit()
    consultas.close()
    conexiones.close()

def AgregarInfo(self, opciones):
    global token
    PWtoken(self)
    RefO=[]
    NumeroRCO=[]
    if(int(opciones)==1):
        if(check.revisar()==True):
            dbx = dropbox.Dropbox(token)
            dbx.files_download_to_file("lib/CBD.db",'/BaseDatosRecepcionMateriaPrima.db')
        conexion = sqlite3.connect("lib/CBD.db")
    else:
        if(check.revisar()==True):
            dbx = dropbox.Dropbox(token)
            dbx.files_download_to_file("lib/BD.db",'/BaseDatosRecepcionMateriaPrima.db')
        conexion = sqlite3.connect("lib/BD.db")
    consultas = conexion.cursor()
    consultas.execute("SELECT * FROM DATOS_MATERIA_PRIMA")
    columna = consultas.fetchall()

    for j in columna:
        RefO.append(int(j[0]))
        NumeroRCO.append(str(j[6]))

    consultas.close()
    conexion.close()

    tama=len(RefO)
    RefC=[]
    RefC2=[]
    OperadorC=[]
    ProveedorC=[]
    ReferenciaC=[]
    PresentacionC=[]
    NumeroRC=[]
    NumeroPC=[]
    PesoTC=[]
    FechaIC=[]
    FechaFC=[]
    NumeroBC=[]
    Nuevo=[]

    if(int(opciones)==1):
        conexion = sqlite3.connect("lib/BD.db")
    else:
        conexion = sqlite3.connect("lib/CBD.db")
    consultas = conexion.cursor()
    consultas.execute("SELECT * FROM DATOS_MATERIA_PRIMA")
    columna = consultas.fetchall()

    for j in columna:
        RefC.append(int(j[0]))
        mem=1
        for i in range(0,tama):
            if(str(j[6])==str(NumeroRCO[i])):
                mem=0    
        if(mem==1):
            Nuevo.append(j)
            RefC2.append(str(j[1]))
            OperadorC.append(str(j[2]))
            ProveedorC.append(str(j[3]))
            ReferenciaC.append(str(j[4]))
            PresentacionC.append(str(j[5]))
            NumeroRC.append(str(j[6]))
            NumeroPC.append(int(j[7]))
            PesoTC.append(float(j[8]))
            FechaIC.append(str(j[9]))
            FechaFC.append(str(j[10]))
            NumeroBC.append(int(j[12]))
    tama2=len(RefC)
    tama3=len(Nuevo)
    consultas.close()
    conexion.close()

    memoria=tama+tama3
    interno=0
      
    if tama != memoria:
        if(int(opciones)==1):
            conexion = sqlite3.connect("lib/CBD.db")
        else:
            conexion = sqlite3.connect("lib/BD.db")
        consultas = conexion.cursor()
        for j in range(tama,memoria):
            image = barcode.get_barcode_class('code128') 
            Ref2=(str(j+1)+"-"+str(NumeroRC[interno]))
            ean = image(Ref2, writer=ImageWriter())
            fullname = ean.save('Img/Code/Codigo'+str(int(j)+1))
            consultas.execute("INSERT INTO DATOS_MATERIA_PRIMA VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(int(j+1), Ref2, OperadorC[interno], ProveedorC[interno], ReferenciaC[interno], PresentacionC[interno], NumeroRC[interno], NumeroPC[interno], PesoTC[interno], FechaIC[interno], FechaFC[interno], "Codigo "+str(j+1), NumeroBC[interno]))
            interno+=1    
        conexion.commit()
        consultas.close()
        conexion.close()

    RefO=[]
    NumeroRCO=[]
    selecionar=0

    for x in range(0,3):
        if(x==0):
            opcs="MATERIA_PRIMA_IMPORTADO_ESTIBAS"
        elif(x==1):
            opcs="MATERIA_PRIMA_ENKA_ESTIBAS"
        elif(x==2):
            opcs="MATERIA_PRIMA_ENKA_CAJA"
        elif(x==3):
            opcs="MATERIA_PRIMA_IMPORTADO_CAJA"    
        
        if(int(opciones)==1):
            conexion = sqlite3.connect("lib/CBD.db")
        else:
            conexion = sqlite3.connect("lib/BD.db")
        consultas = conexion.cursor()
        consultas.execute("SELECT * FROM " + opcs)
        columna = consultas.fetchall()

        for j in columna:
            RefO.append(int(j[0]))
            NumeroRCO.append(str(j[3]))

        consultas.close()
        conexion.close()

        tamas=len(RefO)
        RefC=[]
        CBC=[]
        NDREC=[]
        NDRC=[]
        NDCC=[]
        NDBC=[]
        PEC=[]
        UDMC=[]
        Nuevo2=[]

        if(int(opciones)==1):
            conexion = sqlite3.connect("lib/BD.db")
        else:
            conexion = sqlite3.connect("lib/CBD.db")
        consultas = conexion.cursor()
        consultas.execute("SELECT * FROM " + opcs)
        columna = consultas.fetchall()

        for j in columna:
            RefC.append(int(j[0]))
            mem=1
            for i in range(0,tamas):
                if(str(j[3])==str(NumeroRCO[i])):
                    mem=0    
            if(mem==1):
                Nuevo2.append(j)
                CBC.append(str(j[1]))
                NDREC.append(str(j[2]))
                NDRC.append(str(j[3]))
                NDCC.append(int(j[4]))
                NDBC.append(int(j[5]))
                PEC.append(float(j[6]))
                UDMC.append(str(j[7]))

        consultas.close()
        conexion.close()

        tamas2=len(RefC)
        tamas3=len(Nuevo2)
        memoria=tamas+tamas3
        interno=0
        if(int(opciones)==1):
            conexion = sqlite3.connect("lib/CBD.db")
        else:
            conexion = sqlite3.connect("lib/BD.db")
        consultas = conexion.cursor()

        for j in range(tamas,memoria):
            consultas.execute("INSERT INTO "+opcs+ " VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (int(j+1), CBC[interno], NDREC[interno], NDRC[interno], NDCC[interno], NDBC[interno], PEC[interno], UDMC[interno]))
            interno+=1

        conexion.commit()
        consultas.close()
        conexion.close()

    if(check.revisar()==True):
        dbx = dropbox.Dropbox(token)
        if(int(opciones)==1):
            with open("lib/BD.db", "rb") as f:
                dbx.files_upload(f.read(), '/BaseDatosRecepcionMateriaPrima.db', dropbox.files.WriteMode.overwrite)
        else:
            with open("lib/CBD.db", "rb") as f:
                dbx.files_upload(f.read(), '/BaseDatosRecepcionMateriaPrima.db', dropbox.files.WriteMode.overwrite)

        if(int(opciones)==1):
            conexion = sqlite3.connect("lib/BD.db")
        else:
            conexion = sqlite3.connect("lib/CBD.db")
        consultas = conexion.cursor()
        consultas.execute("SELECT * FROM DATOS_MATERIA_PRIMA")
        columna = consultas.fetchall()
        MEP=[]
        for j in columna:
            MEP.append(j[0])

        numerofoto=len(MEP)
        consultas.close()
        conexion.close()
        for j in range(tama, numerofoto):
            nc=j+1
            with open("Img/Code/Codigo"+str(nc)+".png", 'rb') as f:
                dbx.files_upload(f.read(), '/Img/Codigo de Barras Materia Prima/Codigo'+str(nc)+'.png', dropbox.files.WriteMode.overwrite)

def Autorizaciones(self):
    global P_OP
    global P_ALL
    conexiones = sqlite3.connect("lib/PW.db")
    consultas = conexiones.cursor()
    consultas.execute("SELECT * FROM AUTORIZACION")
    columna = consultas.fetchall()
    for j in columna:
        P_OP=(j[0])
        P_ALL=(j[1])
    consultas.close()
    conexiones.close()

def AdquirirBasedeDatos(self):
    global token
    if(check.revisar()==True):
        PWtoken(self)
        dbx = dropbox.Dropbox(token)
        dbx.files_download_to_file("lib/REFE.db", '/ReferenciaMateriaPrima.db')
        dbx.files_download_to_file("lib/Op.db", '/Operarios.db')
        dbx.files_download_to_file("lib/PW.db", '/Password.db')
    else:
        QMessageBox.about(self, "Redepesca", "¡¡NO SE ENCUENTRA RED!! Se almacenara hasta que se encuentre señal")

def Mensajes(self, Tipo, TextoM, forma):
    if(int(forma)==1):
        QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! falta poner "+ str(TextoM) +" de la "+ str(Tipo) + " En NUMERO")
    else:
        QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! falta poner "+ str(TextoM) +" por "+ str(Tipo) + " En NUMERO")

def presentacionREF(self):
    if (str(self.PRESENTACION.currentText())=="ESTIBAS"):
        self.label_17.setText("Bobinas por Estiba:")
        self.label_16.setText("Numero de Estibas:")
        self.label_20.setText("Numero de Estibas:")
        self.label_21.setText("Numero de Estiba:")   
    else:
        self.label_17.setText("Bobinas por Caja:")
        self.label_16.setText("Numero de Cajas:")
        self.label_20.setText("Numero de Cajas:")
        self.label_21.setText("Numero de Caja:")

def proveedorREF(self):
    self.REFERENCIA.clear()
    conexiones = sqlite3.connect("lib/REFE.db")
    consultas = conexiones.cursor()
    consultas.execute("SELECT * FROM REFERENCIA")
    columna = consultas.fetchall()
    for j in columna:
        if (str(self.PROVEEDOR.currentText())==j[0]):
            self.REFERENCIA.addItem(j[1])        
    consultas.close()
    conexiones.close()

def limpieza(self):
    self.GENERAR.clear()
    self.PRESENTACION.clear()
    self.PRESENTACION.addItem("CAJAS")
    self.PRESENTACION.addItem("ESTIBAS")
    self.PROVEEDOR.clear()
    busquedasql(self,"lib/REFE.db", "REFERENCIA",1)
    proveedorREF(self)
    presentacionREF(self)
    self.TABLARECEPCION.clear()
    self.TABLARECEPCION.setHorizontalHeaderLabels(['Codigo de barras.', 'Numero de Bobinas', 'Peso neto', 'U. Medida'])
    self.NUMERO.clear()
    self.NUMERO_2.clear()
    self.PESO_2.clear()
    self.PESOS_3.clear()
    self.PESOT.clear()
    self.REMISION.clear()
    self.EMPLEADO.clear()
    self.DIA.clear()
    self.MES.clear()
    self.ANO.clear()
    self.HORA.clear()
    self.BARRAS.clear()
    self.BOBINAS.clear()
    self.N_REP.clear()
    
        
def eliminarsql(BaseDatos, ListaEliminar):
    conexiones = sqlite3.connect(str(BaseDatos))
    consultas = conexiones.cursor()
    consultas = conexiones.execute("DELETE FROM " + str(ListaEliminar))
    conexiones.commit()
    consultas.close()
    conexiones.close()

def busquedasql(self,BaseDatos, ListaComparar,Opcion):
    global paso
    global interes
    global arduino
    global pesaje
    global conector_PESO
    global Usuario
    global Bobinastotal
    global permiso
    global imp
    global ANTIGUO
    global cd
    global repetido
    global Num_recepcion
    global cant_prod
    global conexionArduino
    global cant_prod2
    conexion = sqlite3.connect(str(BaseDatos))
    consultas = conexion.cursor()
    consultas.execute("SELECT * FROM " + str(ListaComparar))
    
    if(int(Opcion)==1):
        columna = consultas.fetchall()
        ANTIGUO=""
        for j in columna:
            if(j[0]!=ANTIGUO):
                self.PROVEEDOR.addItem(j[0])
                ANTIGUO=j[0]
        for j in columna:
            if (str(self.PROVEEDOR.currentText())==j[0]):
                self.REFERENCIA.addItem(j[1]) 
    
    elif(int(Opcion)==2):
        interes=0
        columna = consultas.fetchall()
        conexionArduino=0
        for j in columna:
            interes=int(j[2])
            if(interes==1):
                try:
                    arduino = serial.Serial(str(j[1]), 9600, timeout=10)
                    conexionArduino=1
                except:
                    pass
                 
    elif(int(Opcion)==3):
        columna = consultas.fetchall()
        conexionArduino=0
        for j in columna:
            try:
                arduino = serial.Serial(str(j[0]), 9600, timeout=10)
                conexionArduino=1
            except:
                pass
                    
    elif(int(Opcion)==5):
        Bobinastotal=0
        columna = consultas.fetchall()
        for j in columna:
            Bobinastotal=Bobinastotal+int(j[5])

    elif(int(Opcion)==6):
        Usuario=""
        try:
            time.sleep(2)
            rawString= arduino.readline()#[:-2]
            s, x, y, z= np.fromstring(rawString.decode('ascii', errors='replace'),sep=' ')
            per=str(int(s))+" "+str(int(x))+" "+str(int(y))+" "+str(int(z))
            columna = consultas.fetchall()
            
            for j in columna:
                if(str(j[0])==per):
                    permiso=int(j[3])
                    Usuario=str(j[2])
            arduino.close()
        except:
            pass

    elif(int(Opcion)==7):
        ANTIGUO=0
        columna = consultas.fetchall()
        for j in columna:
            if(int(j[0])!=ANTIGUO):
              ANTIGUO=float(j[0])
              Num_recepcion=int(j[0])+1

    elif(int(Opcion)==8):
        self.TABLARECEPCION.clear()
        self.TABLARECEPCION.setRowCount(0)
        self.TABLARECEPCION.setHorizontalHeaderLabels(['Codigo de barras.', 'Numero de Bobinas', 'Peso neto', 'U. Medida'])
        for fila_numero, fila_data in enumerate(consultas):
            self.TABLARECEPCION.insertRow(fila_numero)
            for columna_numero, data in enumerate(fila_data):
                  self.TABLARECEPCION.setItem(fila_numero, columna_numero, QtWidgets.QTableWidgetItem(str(data)))

    elif(int(Opcion)==9):
        ANTIGUO=0
        imp=1
        columna = consultas.fetchall()
        for j in columna:
            imp+=1
            ANTIGUO=ANTIGUO+float(j[6])

    elif(int(Opcion)==11):
        cd=1
        columna = consultas.fetchall()
        for j in columna:
            cd=int(j[0])+1

    elif(int(Opcion)==12):
        ANTIGUO=0
        columna = consultas.fetchall()
        for j in columna:
            if(str(self.REMISION.toPlainText())==str(j[6])):
                ANTIGUO=1

    elif(int(Opcion)==13):
        columna = consultas.fetchall()
        for j in columna:
            self.REMISION.addItem(str(j[6]))

    elif(int(Opcion)==14):
        repetido=0
        cant_prod2=0
        columna = consultas.fetchall()
        for j in columna:
            cant_prod2+=1
            if(str(self.BARRAS.toPlainText())==str(j[0])):
                repetido=1
        if(cant_prod2==0):
            cant_prod2=1

    conexion.commit()
    consultas.close()
    conexion.close()


def AgregarNuevoDatosql(self, BaseDatos, ListaAgregar):
    global Num_recepcion
    global cd
    global Bobinastotal
    today = datetime.datetime.today()
    conexiones = sqlite3.connect(str(BaseDatos))
    consultas = conexiones.cursor()
    if(str(ListaAgregar)=="DATOS_MATERIA_PRIMA"):
        consultas.execute("INSERT INTO " + str(ListaAgregar) + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(Num_recepcion, str(self.N_REP.toPlainText()), str(self.EMPLEADO.toPlainText()), str(self.PROVEEDOR.currentText()), str(self.REFERENCIA.currentText()), str(self.PRESENTACION.currentText()), str(self.REMISION.toPlainText()),int(self.NUMERO.toPlainText()),float(self.PESOT.toPlainText()),str(self.DIA.toPlainText())+"/"+str(self.MES.toPlainText())+"/"+str(self.ANO.toPlainText())+"-"+str(self.HORA.toPlainText()),str(today.day)+"/"+str(today.month)+"/"+str(today.year)+"-"+str(time.strftime("%H:%M:%S")), "Codigo "+str(cd), Bobinastotal))      
    if(str(ListaAgregar)=="MEMORIA"):
        consultas.execute("INSERT INTO " + str(ListaAgregar) + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",(str(self.EMPLEADO.toPlainText()), str(self.PROVEEDOR.currentText()), str(self.REFERENCIA.currentText()), str(self.PRESENTACION.currentText()), str(self.REMISION.toPlainText()), int(self.NUMERO.toPlainText()), float(self.PESOT.toPlainText()), str(self.N_REP.toPlainText()), "Codigo "+str(cd)))
    conexiones.commit()
    consultas.close()
    conexiones.close()

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.REMISION.setReadOnly(False)
        self.NUMERO.setReadOnly(False)
        self.PESOT.setReadOnly(False)
        global paso
        global cant_prod
        global Num_recepcion
        global tini
        global tact
        global trel
        global interes
        global pesaje
        global Numero_pedido
        global cant_prod
        global token
        cant_prod2=1 
        Numero_pedido=0
        pesaje=0
        interes=0
        tini=time.time()
        paso=0
        cant_prod=1
        self.TABLARECEPCION.clear()
        self.TABLARECEPCION.setHorizontalHeaderLabels(['Codigo de barras.', 'Numero de Bobinas', 'Peso neto', 'U. Medida'])
        self.NUMERO_3.setText(str(1))
        self.PRESENTACION.addItem("CAJAS")
        self.PRESENTACION.addItem("ESTIBAS")
        self.UNIDAD.addItem("kg")
        self.UNIDAD.addItem("Unidad")
        AdquirirBasedeDatos(self)
        busquedasql(self,"lib/REFE.db", "REFERENCIA",1)
                
        self.PROVEEDOR.currentIndexChanged.connect(self.REFDEPRO) #Si se selecciona un proveedor realice una modificacion
        self.PRESENTACION.currentIndexChanged.connect(self.TIPOPRE) #Si se selecciona un proveedor realice una modificacion
        self.RFID.clicked.connect(self.USUARIO)
        self.NUEVO.clicked.connect(self.ADIC)
        self.PESOS_2.clicked.connect(self.PESAR)
        self.FINALIZAR.clicked.connect(self.TERMINAR)
        self.INGRESAR.clicked.connect(self.INICIAR)
        self.ELIMINAR.clicked.connect(self.SELEC)
        self.TARAR.clicked.connect(self.CEROPESA)
        self.AYUDA.clicked.connect(self.AYUDAR)
        self.AYUDA2.clicked.connect(self.AYUDAR)
        self.CONECTAR.clicked.connect(self.C_Serial)
        self.CONECTAR_2.clicked.connect(self.C_Serial)
        self.HECHO.clicked.connect(self.PORQUIEN)
        self.NUMERO.textChanged.connect(self.CANT)
        self.REMISION.textChanged.connect(self.REM)

    def PORQUIEN(self):
        self.child_win = DESARROLLADOR(self)
        self.child_win.show() 

    def C_Serial(self):
        self.child_win = SERIAL(self)
        self.child_win.show()

    def AYUDAR(self):
        self.child_win = VentanaAyuda(self)
        self.child_win.show()

    def CEROPESA(self):
        global paso
        global interes
        global arduino
        global pesaje
        global conexionArduino
        if(pesaje==0):
            if(paso==2):
                busquedasql(self,"lib/CN.db", "CONEXION",2)
                if(interes==1):
                    conexionArduino=0
                    pesaje=0
                    try:
                        arduino = serial.Serial(conector_PESO, 9600)
                        conexionArduino=1
                        interes=2
                        pesaje=1
                    except:
                        pass
            else:
                QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! Complete el ingreso de la pestaña anterior") 
             
    def PESAR(self):
        global paso
        global interes
        global arduino
        global pesaje
        if(pesaje==1):
            if(paso==2):
                if(interes==2):
                    try:
                        arduino.write(b'5')
                        time.sleep(2)
                        rawString= arduino.readline()#[:-2]
                        s, y= np.fromstring(rawString.decode('ascii', errors='replace'),sep=' ')
                        per=str(int(s))
                        self.PESO_2.setText(per)
                    except:
                        pass
        else:
           QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! TARAR PRIMERO")

    def TERMINAR(self):
        global cant_prod
        global Num_recepcion
        global paso
        global pesaje
        global Usuario
        global Bobinastotal
        global conexionArduino
        if(paso==3):
            QMessageBox.about(self, "Redepesca", "¡¡Ingresar el mismo usuario por medio de la tarjeta!!")
            busquedasql(self,"lib/CN.db", "CONEXION",3)
            if(conexionArduino==1):
                busquedasql(self,"lib/Op.db", "OPERADORES",6)
                if(Usuario==str(self.EMPLEADO.toPlainText())):   
                    busquedasql(self,"lib/CBD.db", "PROCESO_INGRESO",5)
                    ingresarMateria(self)
                    #ELIMINAR TABLA DE PROCESO INGRESO
                    eliminarsql("lib/CBD.db", "PROCESO_INGRESO")
                    eliminarsql("lib/CBD.db", "TABLA")
                    #INSERTAR DATOS
                    AgregarNuevoDatosql(self, "lib/CBD.db", "DATOS_MATERIA_PRIMA")
                    #LIMPIEZA DE VARIABLES
                    AgregarInfo(self, 2)
                    cant_prod=1
                    paso=0
                    self.REMISION.setReadOnly(False)
                    self.NUMERO.setReadOnly(False)
                    self.PESOT.setReadOnly(False)
                    limpieza(self)
                    self.NUMERO_3.setText(str(cant_prod))
                    QMessageBox.about(self, "Redepesca", "¡¡FINALIZADO!!")
                else:
                    QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! Tiene que ser el mismo usuario que comenzo")
            else:
                QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! Configure la conexion del puerto Serial") 
        else:
            QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! Todavia no cumple todo el pedido para ingresar")

    def SELEC(self):
        global cant_prod
        global Num_recepcion
        global paso
        global arduino
        global pesaje
        global Usuario
        global codigobarrasn
        global permiso
        global imp
        global ANTIGUO
        global P_ALL
        global conexionArduino
        if(pesaje==1):
            arduino.close()
            pesaje=0
        Ref=0
        codigobarrasn=0
        c=0
        Autorizaciones(self)
        if(paso>=2):
            busquedasql(self,"lib/CN.db", "CONEXION",3)
            if(conexionArduino==1):
                QMessageBox.about(self, "Redepesca", "Presione Aceptar e ingrese la tarjeta")
                busquedasql(self,"lib/Op.db", "OPERADORES",6)
                if(Usuario!=""):
                    if(permiso>=P_ALL):
                        buttonReply = QMessageBox.question(self, 'Redepesca', "¿Seguro quieres eliminar la fila seleccionada?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if buttonReply == QMessageBox.Yes:
                            for item in self.TABLARECEPCION.selectedItems():
                                if c == 0:
                                    codigobarrasn = item.text()
                                c=c+1
                            if(codigobarrasn!=0):
                                conexion = sqlite3.connect("lib/CBD.db")
                                consultas = conexion.execute("DELETE FROM PROCESO_INGRESO WHERE CODIGO_DE_BARRAS=?", (codigobarrasn,))   
                                conexion.commit()
                                consultas.close()
                                conexion.close()
                                procesoIng(self, False)
                                
                                busquedasql(self,"lib/CBD.db", "PROCESO_INGRESO",5)
                                busquedasql(self,"lib/CBD.db", "PROCESO_INGRESO",9)
                                self.NUMERO_3.setText(str(imp))
                                self.PESOS_3.setText("%.2f" % (ANTIGUO, ))
                                if(float(self.NUMERO_3.toPlainText())<=float(self.NUMERO.toPlainText())):
                                    paso=2
                            else:
                                QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! No se selecciono la fila a eliminar")
                    else:
                        QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! No tienes permiso para eliminar la fila seleccionada, buscar persona con autorizacion")
                else:
                    QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! Paso el tiempo para pasar la tarjeta Vuelva presionar el boton para ingresar la tarjeta")
            else:
                QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! Configure la conexion del puerto Serial") 
                
        
    def USUARIO(self):
        global Num_recepcion
        global paso
        global arduino
        global pesaje
        global Usuario
        global permiso
        global P_OP
        global P_ALL
        global token
        global Usuario
        global conexionArduino
        if(pesaje==1):
            arduino.close()
            pesaje=0
        Autorizaciones(self)
        permiso=0
        if(paso==0):
            #if(check.revisar()==True):
            #    dbx = dropbox.Dropbox(token)
            PWtoken(self)
            AgregarInfo(self, 1)
            #PagoEfec, esver = QInputDialog.getText(self, "Redepesca", "¿A nombre de quien es la factura?:")
            #if(PagoEfec=="Redepesca" or PagoEfec=="redepesca" or PagoEfec=="REDEPESCA"):
            QMessageBox.about(self, "Redepesca", "Presione Aceptar e ingrese la tarjeta")
            Num_recepcion=0
            busquedasql(self,"lib/CN.db", "CONEXION",3)
            if(conexionArduino==1):
                busquedasql(self,"lib/Op.db", "OPERADORES",6)
                if(Usuario!=""):
                    if(permiso>=P_OP):
                        eliminarsql("lib/CBD.db", "TABLA")
                        self.EMPLEADO.setText(Usuario)
                        today = datetime.datetime.today()
                        busquedasql(self,"lib/CBD.db", "DATOS_MATERIA_PRIMA",7)
                        if(Num_recepcion==0):
                            Num_recepcion=Num_recepcion+1
                        eliminarsql("lib/CBD.db", "PROCESO_INGRESO")
                        self.N_REP.setText(str(Num_recepcion))
                        self.ANO.setText(str(today.year))
                        self.MES.setText(str(today.month))
                        self.DIA.setText(str(today.day))
                        self.HORA.setText(str(time.strftime("%H:%M:%S")))
                        self.PESOT.clear()
                        self.NUMERO.clear()
                        self.NUMERO_2.clear()
                        self.PESOS_3.clear()
                        self.REMISION.clear()
                        self.BARRAS.clear()
                        self.BOBINAS.clear()
                        self.PESO_2.clear()
                        paso=1
                    else:
                        QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! No tiene autorizacion para manejar el sistema, buscar personal autorizado") 
                else:
                    QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! Paso el tiempo para pasar la tarjeta Vuelva presionar el boton para ingresar la tarjeta")
            else:
                QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! Configure la conexion del puerto Serial") 
            #else:
                #QMessageBox.about(self, "Redepesca", "El pedido no es para nosotros, favor devolver o hablar con el jefe de planta")
        else:
            QMessageBox.about(self, "Redepesca", "Presione Aceptar e ingrese la tarjeta")
            busquedasql(self,"lib/CN.db", "CONEXION",3)
            if(conexionArduino==1):
                busquedasql(self,"lib/Op.db", "OPERADORES",6)
                if(Usuario!=""):
                    if(permiso>=P_ALL):
                        buttonReply = QMessageBox.question(self, 'Redepesca', "¿Seguro quieres eliminar TODO LO INGRESADO?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if buttonReply == QMessageBox.Yes:
                            eliminarsql("lib/CBD.db", "PROCESO_INGRESO")
                            if(paso==2):
                                eliminarsql("lib/CBD.db", "PROCESO_INGRESO")
                                eliminarsql("lib/CBD.db", "MEMORIA")
                            paso=0
                            cant_prod=1
                            self.REMISION.setReadOnly(False)
                            self.NUMERO.setReadOnly(False)
                            self.PESOT.setReadOnly(False)
                            limpieza(self)
                            self.NUMERO_3.setText(str(cant_prod))
                        else:
                            return
                    else:
                         QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! No tienes permiso para eliminar todo el ingreso, buscar persona con autorizacion")
                else:
                    QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! Paso el tiempo para pasar la tarjeta Vuelva presionar el boton para ingresar la tarjeta")
            else:
                QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! Configure la conexion del puerto Serial") 
           

    def INICIAR(self):
        global paso
        global Num_recepcion
        global cd
        if(paso==1):
            if(str(self.EMPLEADO.toPlainText())!=""):
                if(str(self.REMISION.toPlainText())!=""):
                    try:
                        if (self.NUMERO.toPlainText().isdigit()):
                            try:
                                if (float(self.PESOT.toPlainText())>0):
                                    #['code39', 'code128', 'ean', 'ean13', 'ean8', 'gs1', 'gtin',  'isbn', 'isbn10', 'isbn13', 'issn', 'jan', 'pzn', 'upc', 'upca']
                                    self.REMISION.setReadOnly(True)
                                    self.NUMERO.setReadOnly(True)
                                    self.PESOT.setReadOnly(True)
                                    image = barcode.get_barcode_class('code128')
                                    image_bar = str(Num_recepcion)+str(self.N_REP.toPlainText())
                                    ean = image(image_bar, writer=ImageWriter())
                                    busquedasql(self,"lib/CBD.db", "DATOS_MATERIA_PRIMA",11)
                                    fullname = ean.save('Img/Code/Codigo'+str(cd))
                                    pixmapImagen = QPixmap(fullname)
                                    self.GENERAR.setPixmap(pixmapImagen)
                                    # Convertir la foto al tipo de dato adecuado
                                    foto = self.GENERAR.pixmap()
                                    eliminarsql("lib/CBD.db", "MEMORIA")
                                    AgregarNuevoDatosql(self, "lib/CBD.db", "MEMORIA")
                                    paso=2
                                    #NUEVO TEXTO
                                    conexiones = sqlite3.connect("lib/CBD.db")
                                    consultas = conexiones.cursor()
                                    consultas.execute("SELECT * FROM MEMORIA")
                                    columna = consultas.fetchall()
                                    for j in columna:
                                        prop=str(j[1])
                                        refer=str(j[2])
                                        prese=str(j[3])
                                    consultas.close()
                                    conexiones.close()
                                    self.PROVEEDOR.clear()
                                    self.PROVEEDOR.addItem(prop)
                                    self.REFERENCIA.clear()
                                    self.REFERENCIA.addItem(refer)
                                    self.PRESENTACION.clear()
                                    self.PRESENTACION.addItem(prese)
                                    #FINAL DEL NUEVO TEXTO
                                else:
                                    Mensajes(self, str(self.PRESENTACION.currentText()), "El peso",1)
                                    return
                            except:
                                QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! debe ser numerico el peso")
                                pass
                        else:
                            Mensajes(self, str(self.PRESENTACION.currentText()), "La cantidad debe ser entero (Sin decimales)",1)
                            return
                    except:
                        QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! debe ser numerico y entero (ejemplo: 1, 2, 3, ...) la cantidad de items")
                        pass
                else:
                    QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! falta poner el codigo de remision")
        else:
            QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! falta ingresar la tarjeta")

    def REM(self):
        global Num_recepcion
        global paso
        global tini
        global tact
        global trel
        global codigobarras
        tact=time.time()
        trel=tact-tini
        Num_recepcion=0
        if(paso==1):
            busquedasql(self,"lib/CBD.db", "DATOS_MATERIA_PRIMA",7)
            if(Num_recepcion==0):
                Num_recepcion=1
            self.N_REP.setText(str(Num_recepcion)+"-"+str(self.REMISION.toPlainText()))
        elif(paso==2):
            busquedasql(self,"lib/CBD.db", "DATOS_MATERIA_PRIMA",13)
            QMessageBox.about(self, "Redepesca", "Si desea modificar solicite al jefe de produccion autorizacion")
            return
        tini=time.time()

    def ADIC(self):
        global cant_prod
        global Num_recepcion
        global paso
        global arduino
        global pesaje
        global repetido
        global Numero_pedido
        global cant_prod2
        Ref=0
        if(paso==2):
            if (self.NUMERO.toPlainText().isdigit()):
                if(str(self.BARRAS.toPlainText())!=""):
                    try:
                        if (int(self.BOBINAS.toPlainText())>0):
                            try:
                                if (float(self.PESO_2.toPlainText())>0):
                                    repetido=0
                                    busquedasql(self,"lib/CBD.db", "TABLA",14)
                                    if(repetido==0):
                                        if(pesaje==1):
                                            arduino.close()
                                            pesaje=0
                                        if(float(self.NUMERO.toPlainText())>float(cant_prod2)):
                                            procesoIng(self, True)
                                        conexion = sqlite3.connect("lib/CBD.db")
                                        consultas = conexion.cursor()
                                        consultas.execute("SELECT * FROM PROCESO_INGRESO")
                                        columna = consultas.fetchall()
                                        ANTIGUO=0
                                        Numero_pedido=0
                                        for j in columna:
                                            Numero_pedido+=1
                                            ANTIGUO=ANTIGUO+float(j[6])
                                        consultas.close()
                                        conexion.close()
                                        self.PESOS_3.setText("%.2f" % (ANTIGUO, ))
                                        self.NUMERO_3.setText(str(Numero_pedido+1))
                                        if(float(self.NUMERO.toPlainText())<float(self.NUMERO_3.toPlainText())):
                                            self.NUMERO_3.setText(str(self.NUMERO.toPlainText()))
                                            if(float(self.PESOS_3.toPlainText())==float(self.PESOT.toPlainText())):
                                                QMessageBox.about(self, "Redepesca", "¡¡TERMINO LA RECEPCION DE LA MATERIA PRIMA!!")
                                                paso=paso+1
                                            else:
                                                if(float(self.PESOS_3.toPlainText())<float(self.PESOT.toPlainText())):
                                                    QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! el peso es inferior al pedido")
                                                else:
                                                    QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! el peso es superior al pedido")
                                                return
                                        self.BARRAS.clear()
                                        self.BOBINAS.clear()
                                        self.PESO_2.clear()
                                    else:
                                        QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! Codigo de barras repetido")
                                else:
                                    Mensajes(self, str(self.PRESENTACION.currentText()), "El peso",1)
                                    return
                            except:
                                QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! debe ser numerico el peso")
                                pass
                        else:
                            Mensajes(self, str(self.PRESENTACION.currentText()), "El numero de bobinas",2)
                            return
                    except:
                        QMessageBox.about(self, "Redepesca Error", "¡¡ERROR!! debe ser numerico la cantidad de bobinas")
                        pass
                else:
                    Mensajes(self, str(self.PRESENTACION.currentText()), "El codigo de barras",1)
                    return
            else:
                Mensajes(self, str(self.PRESENTACION.currentText()), "cantidad de",1)
                return
        else:
             QMessageBox.about(self, "Redepesca Error", "¡¡Error!! termine de completar los primeros datos de la pagina anterior")
        

    def CANT(self):
        self.NUMERO_2.setText(str(self.NUMERO.toPlainText()))
        
    def TIPOPRE(self):
        presentacionREF(self)

    def REFDEPRO(self):
        proveedorREF(self)

class VentanaAyuda(QtWidgets.QMainWindow, Ui_Form):
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
        self.LISTA.currentIndexChanged.connect(self.BUSCAR)
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

class DESARROLLADOR(QtWidgets.QMainWindow, Ui_Form3):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        Ui_Form3.__init__(self)
        self.setupUi(self)
        self.CERRAR.clicked.connect(self.Salir)

    def Salir(self):
        self.close()

class SERIAL(QtWidgets.QMainWindow, Ui_Form2):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        Ui_Form2.__init__(self)
        self.setupUi(self)
        self.CERRAR.clicked.connect(self.Salir)
        self.ACEPTAR.clicked.connect(self.OK)
        self.BUSCARCOM.clicked.connect(self.BUSCAR)
        self.radioButton.toggled.connect(self.Cone)
        self.SERIAL.addItem("")
        self.SERIAL_2.addItem("")
    
    def Cone(self):
        if(self.radioButton.isChecked() == True):
            self.radioButton.setText("Activar pesa")
        else:
            self.radioButton.setText("Desactivar pesa")

    def OK(self):
        conexiones = sqlite3.connect("lib/PW.db")
        consultas = conexiones.cursor()
        consultas.execute("SELECT * FROM PASSWORD")
        columna = consultas.fetchall()
        for j in columna:
            contra=(j[0])
        consultas.close()
        conexiones.close()
        text, ok = QInputDialog.getText(None, "Ingresar Contraseña", "Contraseña:", 
                                        QLineEdit.Password)
        guardar=0
        if text == contra:
            if(str(self.SERIAL.currentText())!=str(self.SERIAL_2.currentText()) or (str(self.SERIAL_2.currentText())=="" and str(self.SERIAL.currentText())!="")):
                if(self.radioButton.isChecked() == True):
                    interes = 1
                else:
                    interes = 0
                eliminarsql("lib/CN.db","CONEXION")
                conexiones = sqlite3.connect("lib/CN.db")
                consultas = conexiones.cursor()
                consultas.execute("INSERT INTO CONEXION VALUES (?, ?, ?)",
                                (str(self.SERIAL.currentText()),str(self.SERIAL_2.currentText()),str(interes)))
                conexiones.commit()
                consultas.close()
                conexiones.close()
                guardar=1
            else:
                QMessageBox.about(self, "Redepesca", "No se almaceno conexion")  
            if(str(self.TOKEN.toPlainText())!=""):
                conexiones = sqlite3.connect("lib/PW.db")
                consultas = conexiones.cursor()
                consultas.execute("INSERT INTO LINK VALUES (?)",
                                (str(self.TOKEN.currentText())))
                conexiones.commit()
                consultas.close()
                conexiones.close()
                if(check.revisar()==True):
                    dbx = dropbox.Dropbox(str(self.TOKEN.currentText()))
                    with open("lib/PW.db", "rb") as f:
                        dbx.files_upload(f.read(), '/Password.db', dropbox.files.WriteMode.overwrite)
                guardar=1
            else:
                QMessageBox.about(self, "Redepesca", "No se almaceno token")
            if (guardar == 1):
                self.close()
        else:
            QMessageBox.about(self, "Redepesca", "!!ERROR¡¡ Contraseña incorrecta")

    def BUSCAR(self):
        texto='/dev/ttyACM'
        texto2='/dev/ttyUSB'
        texto3='/dev/ttyAMA'
        #texto='COM'
        bEncontrado = False
        self.SERIAL.clear()
        self.SERIAL_2.clear()
        self.SERIAL.addItem("")
        self.SERIAL_2.addItem("")
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
                self.SERIAL_2.addItem(PUERTO)
                # Salimos del bucle
            except:
                # Si hay error, no hacemos nada y continuamos con la busqueda
                pass
            try:
                # Puerto que vamos a probar
                PUERTO = texto2 + str(iPuerto)
                # Velocidad 
                VELOCIDAD = '9600'
                # Probamos ha abrir el puerto
                Arduino = serial.Serial(PUERTO, VELOCIDAD)
                # si no se ha producido un error, cerramos el puerto
                Arduino.close()
                # cambiamos el estado del la variable para saber si lo hemos encontrado
                bEncontrado = True
                self.SERIAL.addItem(PUERTO)
                self.SERIAL_2.addItem(PUERTO)
                # Salimos del bucle
            except:
                # Si hay error, no hacemos nada y continuamos con la busqueda
                pass
            try:
                # Puerto que vamos a probar
                PUERTO = texto3 + str(iPuerto)
                # Velocidad 
                VELOCIDAD = '9600'
                # Probamos ha abrir el puerto
                Arduino = serial.Serial(PUERTO, VELOCIDAD)
                # si no se ha producido un error, cerramos el puerto
                Arduino.close()
                # cambiamos el estado del la variable para saber si lo hemos encontrado
                bEncontrado = True
                self.SERIAL.addItem(PUERTO)
                self.SERIAL_2.addItem(PUERTO)
                # Salimos del bucle
            except:
                # Si hay error, no hacemos nada y continuamos con la busqueda
                pass
        if (bEncontrado==False):
            QMessageBox.about(self, "Redepesca", "No se ha encontrado Conexion")      

    def Salir(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
