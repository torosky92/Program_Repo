from sql.SQL_MPIER import SQLMPIER
# Materia prima importado estibas retirada
class findMPIER:
    def Check_And_Add_ListMPIER():
        CodeBr, NumPre, NumRem, NumCoils, NumCoilsR, TotalW, TotalWR, Measure = SQLMPIER.FindALLMPIER(
            'sqlite:///lib/CBDR.db')
        CodeBr2, NumPre2, NumRem2, NumCoils2, NumCoilsR2, TotalW2, TotalWR2, Measure2 = SQLMPIER.FindALLMPIER(
            'sqlite:///lib/BDR.db')
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
        SQLMPIER.DeleteALLMPIER('sqlite:///lib/CBDR.db')
        SQLMPIER.DeleteALLMPIER('sqlite:///lib/BDR.db')
        for x in range(len(New_CodeB)):
            SQLMPIER.AddMPIER('sqlite:///lib/CBDR.db', New_CodeB[x], New_NumRem[x], New_NumPre[x], New_NumCoils[x],
                              New_NumCoilsR[x], New_TotalW[x], New_TotalWR[x], New_Measure[x])
            SQLMPIER.AddMPIER('sqlite:///lib/BDR.db', New_CodeB[x], New_NumRem[x], New_NumPre[x], New_NumCoils[x],
                              New_NumCoilsR[x], New_TotalW[x], New_TotalWR[x], New_Measure[x])

    def FindObjMPIER(Table:str, REF: str):
        if Table == "Normal":
            Type = 'sqlite:///lib/BDR.db'
        else:
            Type ='sqlite:///lib/PBDR.db'
        CodeB, Num_Pre, Num_Rem, Num_Coils, Num_CoilsR, Total_Weight, Total_WeightR, Measurement = SQLMPIER.FindsMPIER(Type, REF)
        return (CodeB)

    def FindESMPIER(Table:str, REF: str):
        if Table == "Normal":
            Type = 'sqlite:///lib/BDR.db'
        else:
            Type ='sqlite:///lib/PBDR.db'
        CodeB, Num_Pre, Num_Rem, Num_Coils, Num_CoilsR, Total_Weight, Total_WeightR, Measurement = SQLMPIER.FindMPIER(Type, REF)
        return (Num_Coils, Num_CoilsR, Total_Weight, Total_WeightR)