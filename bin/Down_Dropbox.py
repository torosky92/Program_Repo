import dropbox
from bin.check import CHECK
from sql.SQL_Token import SQLToken

class DROPBOX_APP:

    def Dropbox_Down():
        if(CHECK.revisar()==True):
            dbx = dropbox.Dropbox(SQLToken.FindToken())
            dbx.files_download_to_file("lib/CBD.db",'/BaseDatosRecepcionMateriaPrima.db')
            dbx.files_download_to_file("lib/REFE.db", '/ReferenciaMateriaPrima.db')
            dbx.files_download_to_file("lib/OP.db", '/Operarios.db')
            dbx.files_download_to_file("lib/PW.db", '/Password.db')
            dbx.files_download_to_file("lib/RMAQ.db", '/RefereneciaMaquinas.db')
            dbx.files_download_to_file("lib/CBDR.db", '/BaseDatosRetorcido.db')
            return True
        return False

    def Dropbox_Up_doc(Direction: str, Direction_Des: str):
        if(CHECK.revisar()==True):
            dbx = dropbox.Dropbox(SQLToken.FindToken())
            with open(Direction, "rb") as f:
                dbx.files_upload(f.read(), Direction_Des, dropbox.files.WriteMode.overwrite)
            return True
        return False

    def Dropbox_Up_pic(Direction: str, Direction_Des: str):
        if (CHECK.revisar() == True):
            dbx = dropbox.Dropbox(SQLToken.FindToken())
            with open(Direction, 'rb') as f:
                dbx.files_upload(f.read(), Direction_Des, dropbox.files.WriteMode.overwrite)
            return True
        return False