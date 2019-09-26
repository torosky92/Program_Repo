from sql.pmp.SQL_MP import SQLMP
from Settings import Settings

# Datos de materia prima
class findMP:
    def Check_And_Add_ListMP():
        Ref, Worker, Provider, Reference, Presentation, NumRem, NumPre, WeightT, InitialD, FinalD, CodeB, Num_Coils = SQLMP.FindALLMP(Settings.Dir_BD())
        Ref2, Worker2, Provider2, Reference2, Presentation2, NumRem2, NumPre2, WeightT2, InitialD2, FinalD2, CodeB2, Num_Coils2 = SQLMP.FindALLMP(Settings.Dir_CBD())
        New_ID = []
        New_Refs = []
        New_Workers = []
        New_Providers = []
        New_References =[]
        New_Presentation = []
        New_NumRem = []
        New_NumPre = []
        New_TotalW = []
        New_Initial = []
        New_Final = []
        New_CodeB = []
        New_NumCoils = []
        for x in range(len(Ref)):
            if Ref[x] not in New_Refs:
                New_Refs.append(Ref[x])
                New_Workers.append(Worker[x])
                New_Providers.append(Provider[x])
                New_References.append(Reference[x])
                New_Presentation.append(Presentation[x])
                New_NumRem.append(NumRem[x])
                New_NumPre.append(NumPre[x])
                New_TotalW.append(WeightT[x])
                New_Initial.append(InitialD[x])
                New_Final.append(FinalD[x])
                New_CodeB.append(CodeB[x])
                New_NumCoils.append(Num_Coils[x])
        for x in range(len(Ref2)):
            if Ref2[x] not in New_Refs:
                New_Refs.append(Ref2[x])
                New_Workers.append(Worker2[x])
                New_Providers.append(Provider2[x])
                New_References.append(Reference2[x])
                New_Presentation.append(Presentation2[x])
                New_NumRem.append(NumRem2[x])
                New_NumPre.append(NumPre2[x])
                New_TotalW.append(WeightT2[x])
                New_Initial.append(InitialD2[x])
                New_Final.append(FinalD2[x])
                New_CodeB.append(CodeB2[x])
                New_NumCoils.append(Num_Coils2[x])
        for x in range(len(Num_Coils)):
            New_ID.append(x+1)
        SQLMP.DeleteALLMP(Settings.Dir_CBD())
        SQLMP.DeleteALLMP(Settings.Dir_BD())
        for x in range(len(New_Refs)):
            SQLMP.AddMP(Settings.Dir_CBD(), New_ID[x], New_Refs[x], New_Workers[x], New_Providers[x], New_References[x], New_Presentation[x], New_NumRem[x], New_NumPre[x], New_TotalW[x], New_Initial[x], New_Final[x], New_CodeB[x], New_NumCoils[x])
            SQLMP.AddMP(Settings.Dir_BD(), New_ID[x], New_Refs[x], New_Workers[x], New_Providers[x], New_References[x], New_Presentation[x], New_NumRem[x], New_NumPre[x], New_TotalW[x], New_Initial[x], New_Final[x], New_CodeB[x], New_NumCoils[x])

    def FindAllItemMP(Table: str, ItemToFind: str):
        if Table == Settings.Var_Process1():
            Type = Settings.Dir_BD()
        else:
            Type = Settings.Dir_PBD()
        Refs, Workers, Providers, References, Presentations, NumRems, NumPres, TotalWeight, InitialDate, FinalDate, CodeBr, NumCoils = \
            SQLMP.FindALLMP(Type)
        if ItemToFind == Settings.Var_Comp26(): return Refs
        elif ItemToFind == Settings.Var_Comp15(): return Workers
        elif ItemToFind == Settings.Var_Comp14(): return Providers
        elif ItemToFind == Settings.Var_Comp13(): return References
        elif ItemToFind == Settings.Var_Comp12(): return Presentations
        elif ItemToFind == Settings.Var_Comp9(): return NumRems
        elif ItemToFind == Settings.Var_Comp3(): return NumPres
        elif ItemToFind == Settings.Var_Comp6(): return NumCoils
        elif ItemToFind == Settings.Var_Comp4(): return TotalWeight
        elif ItemToFind == Settings.Var_Comp19(): return InitialDate
        elif ItemToFind == Settings.Var_Comp20(): return FinalDate
        elif ItemToFind == Settings.Var_Comp1(): return CodeBr

    def FindObjMP(Table:str, REF: str):
        if Table == Settings.Var_Process1():
            Type = Settings.Dir_BD()
        else:
            Type = Settings.Dir_PBD()
        Ref, Worker, Provider, Reference, Presentation, Num_Rem, Num_Pre, Total_Weight, Initial_Date, Final_Date, CodeB, Num_Coils = \
            SQLMP.FindMP(Type, REF)
        return (Provider, Reference, Presentation)