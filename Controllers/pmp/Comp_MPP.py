from sql.pmp.SQL_MPP import *
from Settings import Settings

#______________ CONTROL SQL Materia Prima con distintas Presentaciones Retorcido _________________#
class findMPP:
    def Check_And_Add_ListMPP(NameTable: str):
        CodeBr, NumRec, NumRem, NumBox, NumCoils, TotalW, Measure = SQLFunctionMPP.FindALLMPP(NameTable, Settings.Dir_BD())
        CodeBr2, NumRec2, NumRem2, NumBox2, NumCoils2, TotalW2, Measure2 = SQLFunctionMPP.FindALLMPP(NameTable, Settings.Dir_CBD())
        New_ID = []
        New_CodeB = []
        New_NumRec = []
        New_NumRem = []
        New_NumBox = []
        New_NumCoils = []
        New_TotalW = []
        New_Measure = []
        for x in range(len(CodeBr)):
            if CodeBr[x] not in New_CodeB:
                    New_CodeB.append(CodeBr[x])
                    New_NumRec.append(NumRec[x])
                    New_NumRem.append(NumRem[x])
                    New_NumBox.append(NumBox[x])
                    New_NumCoils.append(NumCoils[x])
                    New_TotalW.append(TotalW[x])
                    New_Measure.append(Measure[x])
        for x in range(len(CodeBr2)):
            if CodeBr2[x] not in New_CodeB:
                New_CodeB.append(CodeBr2[x])
                New_NumRec.append(NumRec2[x])
                New_NumRem.append(NumRem2[x])
                New_NumBox.append(NumBox2[x])
                New_NumCoils.append(NumCoils2[x])
                New_TotalW.append(TotalW2[x])
                New_Measure.append(Measure2[x])
        for x in range(len(New_NumBox)):
            New_ID.append(x+1)
        SQLFunctionMPP.DeleteALLMPP(NameTable, Settings.Dir_CBD())
        SQLFunctionMPP.DeleteALLMPP(NameTable, Settings.Dir_BD())
        for x in range(len(New_CodeB)):
            SQLFunctionMPP.AddMPP(NameTable, Settings.Dir_CBD(), New_ID[x], New_CodeB[x], New_NumRec[x], New_NumRem[x], New_NumBox[x], New_NumCoils[x], New_TotalW[x], New_Measure[x])
            SQLFunctionMPP.AddMPP(NameTable, Settings.Dir_BD(), New_ID[x], New_CodeB[x], New_NumRec[x], New_NumRem[x], New_NumBox[x], New_NumCoils[x], New_TotalW[x], New_Measure[x])

    def FindObjMPP(Provider: str, Presentation: str, Table:str, REF: str):
        if Provider == Settings.Var_Provider1():
            if Presentation == Settings.Var_P1():
                NameTable = Settings.Var_EC()
            else:
                NameTable = Settings.Var_EE()
        else:
            if Presentation == Settings.Var_P1():
                NameTable = Settings.Var_IC()
            else:
                NameTable = Settings.Var_IE()
        if Table == Settings.Var_Process1():
            Type = Settings.Dir_BD()
        else:
            Type = Settings.Dir_PBD()
        CodeB, Num_Pre, Num_Rem, Num_Coils, Num_CoilsR, Total_Weight, Total_WeightR, Measurement = SQLFunctionMPP.FindsMPP(NameTable, Type, REF)
        return (CodeB)

    def FindESMPP(Provider: str, Presentation: str, Table:str, REF: str):
        if Provider == Settings.Var_Provider1():
            if Presentation == Settings.Var_P1():
                NameTable = Settings.Var_EC()
            else:
                NameTable = Settings.Var_EE()
        else:
            if Presentation == Settings.Var_P1():
                NameTable = Settings.Var_IC()
            else:
                NameTable = Settings.Var_IE()
        if Table == Settings.Var_Process1():
            Type = Settings.Dir_BD()
        else:
            Type = Settings.Dir_PBD()
        CodeB, Num_Pre, Num_Rem, Num_Coils, Num_CoilsR, Total_Weight, Total_WeightR, Measurement = SQLFunctionMPP.FindMPP(NameTable, Type, REF)
        return (Num_Coils, Num_CoilsR, Total_Weight, Total_WeightR)