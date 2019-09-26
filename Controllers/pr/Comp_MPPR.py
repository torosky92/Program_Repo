from sql.pr.SQL_MPPR import *
from Settings import Settings

#______________ CONTROL SQL Materia Prima con distintas Presentaciones Retorcido _________________#
class findMPPR:
    def Check_And_Add_ListMPPR(NameTable: str):
        CodeBr, NumPre, NumRem, NumCoils, NumCoilsR, TotalW, TotalWR, Measure = SQLFunction.FindALLMPPR(NameTable, Settings.Dir_BDR())
        CodeBr2, NumPre2, NumRem2, NumCoils2, NumCoilsR2, TotalW2, TotalWR2, Measure2 = SQLFunction.FindALLMPPR(NameTable, Settings.Dir_CBDR())
        New_CodeB = []
        New_NumPre = []
        New_NumRem = []
        New_NumCoils = []
        New_NumCoilsR = []
        New_TotalW = []
        New_TotalWR = []
        New_Measure = []
        for x in range(len(CodeBr)):
            if CodeBr[x] not in New_CodeB:
                    New_CodeB.append(CodeBr[x])
                    New_NumPre.append(NumPre[x])
                    New_NumRem.append(NumRem[x])
                    New_NumCoils.append(NumCoils[x])
                    New_NumCoilsR.append(NumCoilsR[x])
                    New_TotalW.append(TotalW[x])
                    New_TotalWR.append(TotalWR[x])
                    New_Measure.append(Measure[x])
        for x in range(len(CodeBr2)):
            if CodeBr2[x] not in New_CodeB:
                    New_CodeB.append(CodeBr2[x])
                    New_NumPre.append(NumPre2[x])
                    New_NumRem.append(NumRem2[x])
                    New_NumCoils.append(NumCoils2[x])
                    New_NumCoilsR.append(NumCoilsR2[x])
                    New_TotalW.append(TotalW2[x])
                    New_TotalWR.append(TotalWR2[x])
                    New_Measure.append(Measure2[x])
        SQLFunction.DeleteALLMPPR(NameTable, Settings.Dir_CBDR())
        SQLFunction.DeleteALLMPPR(NameTable, Settings.Dir_BDR())
        for x in range(len(New_CodeB)):
            SQLFunction.AddMPPR(NameTable, Settings.Dir_CBDR(), New_CodeB[x], New_NumRem[x], New_NumPre[x], New_NumCoils[x],
                              New_NumCoilsR[x], New_TotalW[x], New_TotalWR[x], New_Measure[x])
            SQLFunction.AddMPPR(NameTable, Settings.Dir_BDR(), New_CodeB[x], New_NumRem[x], New_NumPre[x], New_NumCoils[x],
                              New_NumCoilsR[x], New_TotalW[x], New_TotalWR[x], New_Measure[x])

    def FindObjMPPR(Provider: str, Presentation: str, Table:str, REF: str):
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
            Type = Settings.Dir_BDR()
        else:
            Type = Settings.Dir_PBDR()
        CodeB, Num_Pre, Num_Rem, Num_Coils, Num_CoilsR, Total_Weight, Total_WeightR, Measurement = SQLFunction.FindsMPPR(NameTable, Type, REF)
        return (CodeB)

    def FindESMPPR(Provider: str, Presentation: str, Table:str, REF: str):
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
            Type = Settings.Dir_BDR()
        else:
            Type = Settings.Dir_PBDR()
        CodeB, Num_Pre, Num_Rem, Num_Coils, Num_CoilsR, Total_Weight, Total_WeightR, Measurement = SQLFunction.FindMPPR(NameTable, Type, REF)
        return (Num_Coils, Num_CoilsR, Total_Weight, Total_WeightR)