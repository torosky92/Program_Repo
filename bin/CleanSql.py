import sqlite3
def eliminarsql(BaseDatos, ListaEliminar):
	conexiones = sqlite3.connect(str(BaseDatos))
    consultas = conexiones.cursor()
    consultas = conexiones.execute("DELETE FROM " + str(ListaEliminar))
    conexiones.commit()
    consultas.close()
    conexiones.close()