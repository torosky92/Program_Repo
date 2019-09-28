from sql.pr.SQL_MPR import SQLMPR
from Settings import Settings
# Datos de materia prima retirada
class findMPR:
    def Check_And_Add_ListMPR():
        Refs, Workers, Providers, References, Presentations, NumRems, NumPres, NumCoils, NumCoilsR, TotalWeight, TotalWeightR, InitialDate, FinalDate, CodeBr = SQLMPR.FindALLMPR(Settings.Dir_BDR())
        Refs2, Workers2, Providers2, References2, Presentations2, NumRems2, NumPres2, NumCoils2, NumCoilsR2, TotalWeight2, TotalWeightR2, InitialDate2, FinalDate2, CodeBr2 = SQLMPR.FindALLMPR(Settings.Dir_CBDR())
        New_Refs = []
        New_Workers = []
        New_Providers = []
        New_References =[]
        New_Presentation = []
        New_NumRem = []
        New_NumPre = []
        New_NumCoils = []
        New_NumCoilsR = []
        New_TotalW = []
        New_TotalWR = []
        New_Initial = []
        New_Final = []
        New_CodeB = []
        for x in range(len(Refs)):
            if Refs[x] not in New_Refs:
                New_Refs.append(Refs[x])
                New_Workers.append(Workers[x])
                New_Providers.append(Providers[x])
                New_References.append(References[x])
                New_Presentation.append(Presentations[x])
                New_NumRem.append(NumRems[x])
                New_NumPre.append(NumPres[x])
                New_NumCoils.append(NumCoils[x])
                New_NumCoilsR.append(NumCoilsR[x])
                New_TotalW.append(TotalWeight[x])
                New_TotalWR.append(TotalWeightR[x])
                New_Initial.append(InitialDate[x])
                New_Final.append(FinalDate[x])
                New_CodeB.append(CodeBr[x])
        for x in range(len(Refs2)):
            if Refs2[x] not in New_Refs:
                New_Refs.append(Refs2[x])
                New_Workers.append(Workers2[x])
                New_Providers.append(Providers2[x])
                New_References.append(References2[x])
                New_Presentation.append(Presentations2[x])
                New_NumRem.append(NumRems2[x])
                New_NumPre.append(NumPres2[x])
                New_NumCoils.append(NumCoils2[x])
                New_NumCoilsR.append(NumCoilsR2[x])
                New_TotalW.append(TotalWeight2[x])
                New_TotalWR.append(TotalWeightR2[x])
                New_Initial.append(InitialDate2[x])
                New_Final.append(FinalDate2[x])
                New_CodeB.append(CodeBr2[x])
        SQLMPR.DeleteALLMPR(Settings.Dir_CBDR())
        SQLMPR.DeleteALLMPR(Settings.Dir_BDR())
        for x in range(len(New_Refs)):
            SQLMPR.AddMPR(Settings.Dir_CBDR(), New_Refs[x], New_Workers[x], New_Providers[x], New_References[x],
                          New_Presentation[x], New_NumRem[x], New_NumPre[x], New_NumCoils[x], New_NumCoilsR[x],
                          New_TotalW[x], New_TotalWR[x], New_Initial[x], New_Final[x], New_CodeB[x])
            SQLMPR.AddMPR(Settings.Dir_BDR(), New_Refs[x], New_Workers[x], New_Providers[x], New_References[x],
                          New_Presentation[x], New_NumRem[x], New_NumPre[x], New_NumCoils[x], New_NumCoilsR[x],
                          New_TotalW[x], New_TotalWR[x], New_Initial[x], New_Final[x], New_CodeB[x])

    def FindAllItemMPR(Table: str, ItemToFind: str):
        if Table == Settings.Var_Process1():
            Type = Settings.Dir_BDR()
        else:
            Type = Settings.Dir_PBDR()
        Refs, Workers, Providers, References, Presentations, NumRems, NumPres, NumCoils, NumCoilsR, TotalWeight, TotalWeightR, InitialDate, FinalDate, CodeBr = SQLMPR.FindALLMPR(Type)
        if ItemToFind == Settings.Var_Comp26(): return Refs
        elif ItemToFind == Settings.Var_Comp15(): return Workers
        elif ItemToFind == Settings.Var_Comp14(): return Providers
        elif ItemToFind == Settings.Var_Comp13(): return References
        elif ItemToFind == Settings.Var_Comp12(): return Presentations
        elif ItemToFind == Settings.Var_Comp9(): return NumRems
        elif ItemToFind == Settings.Var_Comp3(): return NumPres
        elif ItemToFind == Settings.Var_Comp6(): return NumCoils
        elif ItemToFind == Settings.Var_Comp7(): return NumCoilsR
        elif ItemToFind == Settings.Var_Comp4(): return TotalWeight
        elif ItemToFind == Settings.Var_Comp28(): return TotalWeightR
        elif ItemToFind == Settings.Var_Comp19(): return InitialDate
        elif ItemToFind == Settings.Var_Comp20(): return FinalDate
        elif ItemToFind == Settings.Var_Comp1(): return CodeBr

    def FindObjMPR(Table:str, REF: str):
        if Table == Settings.Var_Process1():
            Type = Settings.Dir_BDR()
        else:
            Type = Settings.Dir_PBDR()
        Refs, Workers, Providers, References2, Presentations, NumRems, NumPres, NumCoils, NumCoilsR, TotalWeight, TotalWeightR, InitialDate, FinalDate, CodeBr = SQLMPR.FindMPR(Type, REF)
        return (Providers, References2, Presentations)

    def Find_MPR(Table:str, REF: str):
        if Table == Settings.Var_Process1():
            Type = Settings.Dir_BDR()
        else:
            Type = Settings.Dir_PBDR()
        Refs, Workers, Providers, References2, Presentations, NumRems, NumPres, NumCoils, NumCoilsR, TotalWeight, TotalWeightR, InitialDate, FinalDate, CodeBr = SQLMPR.FindMPR(Type, REF)
        return (NumCoilsR, TotalWeightR)

    def UpgradeMPR(Table:str, REMISION: str, DATO_MOD, Value):
        if Table == Settings.Var_Process1():
            Type = Settings.Dir_BDR()
        else:
            Type = Settings.Dir_PBDR()
        SQLMPR.UpdateMPR(Type, REMISION, DATO_MOD, Value)