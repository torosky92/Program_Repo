#from sql.SQL_User import SQLUser
#from sql.SQL_COM import SQLCOM
#from sql.SQL_Token import SQLToken
from sql.SQL_EXAMPLE import *
from sql.SQL_EXA import *

Forms.AddEX("P", 'sqlite:///lib/EXAMPLE.db', "93232323", 1022320)
print(Forms.Find("Pe", 'sqlite:///lib/EXAMPLE.db'))
print(Forms.Find("p", 'sqlite:///lib/EXAMPLE.db'))
Forms.Delete("Pe", 'sqlite:///lib/EXAMPLE.db', "93232323")
#Forms.DeleteALL("P", 'sqlite:///lib/EXAMPLE.db')
#from Controllers.pr.Comp_MPPR import findMPPR
#findMPPR.Check_And_Add_ListMPPR("ENKA CAJA")
#findMPPR.Check_And_Add_ListMPPR("ENKA ESTIBAS")
