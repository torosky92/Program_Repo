#from sql.SQL_User import SQLUser
#from sql.SQL_COM import SQLCOM
#from sql.SQL_Token import SQLToken
#from sql.SQL_EXAMPLE import *


#Forms.AddEX("P", 'sqlite:///lib/EXAMPLE.db', "93232323", 1022320)
#print(Forms.Find("Pe", 'sqlite:///lib/EXAMPLE.db'))
#print(Forms.Find("p", 'sqlite:///lib/EXAMPLE.db'))
#Forms.Delete("Pe", 'sqlite:///lib/EXAMPLE.db', "93232323")
#Forms.DeleteALL("P", 'sqlite:///lib/EXAMPLE.db')

#from Controllers.pr.Comp_MPPR import findMPPR
#findMPPR.Check_And_Add_ListMPPR("ENKA CAJA")
#findMPPR.Check_And_Add_ListMPPR("ENKA ESTIBAS")
#findMPPR.Check_And_Add_ListMPPR("IMPORTADOS CAJA")
#findMPPR.Check_And_Add_ListMPPR("IMPORTADOS ESTIBAS")

#from sql.pmp.SQL_MPP import *
#SQLFunctionMPP.CreateTable("ENKA CAJA",'sqlite:///lib/CBD.db')

#from sql.pr.SQL_CC import SQLCC
#print(SQLCC.UpdateCC("Negro","Rojo"))

#from sql.pr.SQL_ST import SQLST
#print(SQLST.FindALLST())
#SQLST.DeleteST("109")

#from sql.pr.SQL_MAQ import SQLMAQ
#print(SQLMAQ.FindALLMAQ())
#SQLMAQ.AddMAQ("Mackings2", "Destruida")
#SQLMAQ.DeleteMAQ("STR2")

#from Controllers.pr.Comp_MPPR import *
#findMPPR.Check_And_Add_ListMPPR(Settings.Var_EC())
#findMPPR.Check_And_Add_ListMPPR(Settings.Var_EE())
#findMPPR.Check_And_Add_ListMPPR(Settings.Var_IC())
#findMPPR.Check_And_Add_ListMPPR(Settings.Var_IE())
#from Controllers.pr.Comp_MR import *
#from Controllers.pr.Comp_PM import findPM
from Settings import Settings
#findPM.Check_And_Add_ListPM(Settings.Var_PP())
#findPM.Check_And_Add_ListPM(Settings.Var_PM())

#from sql.com.SQL_COM import SQLCOM
#print(SQLCOM.UpdateCom(Settings.Var_Find1(),"COM2"))

#from sql.com.SQL_PASS import SQLPERMITION
#print(SQLPERMITION.FindPermition(Settings.Var_Comp15()))

#from sql.com.SQL_PW import SQLPW
#print(SQLPW.FindPW())

#from sql.com.SQL_TOKEN import SQLToken
#print(SQLToken.FindToken())

#from sql.com.SQL_User import SQLUser
#print(SQLUser.FindAll())

#from sql.com.SQL_INF import SQLINF
#print(SQLINF.FindALLInf())

#from sql.com.SQL_REFE import SQLREFE
#SQLREFE.CreateRef()
#print(SQLREFE.FindALLRef())

#from Controllers.pmp.Comp_MPP import *
#from Controllers.pmp.Comp_MP import *
#SQLFunctionMPP.CreateTable(Settings.Var_EC(),Settings.Dir_CBD())
#findMP.Check_And_Add_ListMP()

#from sql.pmp.SQL_MEM import SQLMM
#SQLMM.AddMM(Settings.Dir_CBD(),"JUAN RESTREPO", "ENKA", "940/2", "CAJAS", "98788233",15,324.43,"9328443","1-3244432")
#SQLMM.DeleteMM(Settings.Dir_CBD(),"98788233")
#SQLMM.DeleteALL(Settings.Dir_CBD())


#SQLPI.AddPI(Settings.Dir_CBD(),"3","23445233","324","3245",234,12,32.5,"kg")
#SQLPI.DeletePI(Settings.Dir_CBD(),"3244")
#SQLMT.AddMT("343828",6,24.16,"kg")
#SQLMT.DeleteALL()

from Data.pr.Upgrade_BD_BDR import Upgrade
Upgrade.UpgradeMP()
Upgrade.UpgradeMPP(Settings.Var_EC())
Upgrade.UpgradeMPP(Settings.Var_EE())
Upgrade.UpgradeMPP(Settings.Var_IC())
Upgrade.UpgradeMPP(Settings.Var_IE())