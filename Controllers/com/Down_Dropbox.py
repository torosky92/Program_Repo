import dropbox
from Controllers.com.check import CHECK
from sql.com.SQL_TOKEN import SQLToken
from Settings import Settings

class DROPBOX_APP:

    def Dropbox_Down():
        if(CHECK.revisar()==True):
            dbx = dropbox.Dropbox(SQLToken.FindToken())
            dbx.files_download_to_file(Settings.Dir_Send5(), Settings.Dir_Dest5())
            dbx.files_download_to_file(Settings.Dir_Send4(), Settings.Dir_Dest4())
            dbx.files_download_to_file(Settings.Dir_Send3(), Settings.Dir_Dest3())
            dbx.files_download_to_file(Settings.Dir_Send2(), Settings.Dir_Dest2())
            dbx.files_download_to_file(Settings.Dir_Send1(), Settings.Dir_Dest1())
            return True
        return False

    def Dropbox_Up(Direction: str, Direction_Des: str):
        if(CHECK.revisar()==True):
            dbx = dropbox.Dropbox(SQLToken.FindToken())
            with open(Direction, "rb") as f:
                dbx.files_upload(f.read(), Direction_Des, dropbox.files.WriteMode.overwrite)
            return True
        return False