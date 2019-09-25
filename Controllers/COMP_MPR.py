from sql.SQL_MPR import SQLMPR
# Datos de materia prima retirada
class findMPR:
    def Check_And_Add_ListMPR():
        Refs, Workers, Providers, References, Presentations, NumRems, NumPres, NumCoils, NumCoilsR, TotalWeight, TotalWeightR, InitialDate, FinalDate, CodeBr = \
            SQLMPR.FindALLMPR('sqlite:///lib/CBDR.db')
        Refs2, Workers2, Providers2, References2, Presentations2, NumRems2, NumPres2, NumCoils2, NumCoilsR2, TotalWeight2, TotalWeightR2, InitialDate2, FinalDate2, CodeBr2 = \
            SQLMPR.FindALLMPR('sqlite:///lib/BDR.db')
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
        SQLMPR.DeleteALLMPR('sqlite:///lib/CBDR.db')
        SQLMPR.DeleteALLMPR('sqlite:///lib/BDR.db')
        for x in range(len(New_Refs)):
            SQLMPR.AddMPR('sqlite:///lib/CBDR.db', New_Refs[x], New_Workers[x], New_Providers[x], New_References[x],
                          New_Presentation[x], New_NumRem[x], New_NumPre[x], New_NumCoils[x], New_NumCoilsR[x],
                          New_TotalWR[x], New_TotalWR[x], New_Initial[x], New_Final[x], New_CodeB[x])
            SQLMPR.AddMPR('sqlite:///lib/BDR.db', New_Refs[x], New_Workers[x], New_Providers[x], New_References[x],
                          New_Presentation[x], New_NumRem[x], New_NumPre[x], New_NumCoils[x], New_NumCoilsR[x],
                          New_TotalWR[x], New_TotalWR[x], New_Initial[x], New_Final[x], New_CodeB[x])

    def FindAllItemMPR(Table: str, ItemToFind: str):
        if Table == "Normal":
            Type = 'sqlite:///lib/BDR.db'
        else:
            Type ='sqlite:///lib/PBDR.db'
        Refs, Workers, Providers, References, Presentations, NumRems, NumPres, NumCoils, NumCoilsR, TotalWeight, TotalWeightR, InitialDate, FinalDate, CodeBr = \
            SQLMPR.FindALLMPR(Type)
        if ItemToFind == "REF":
            return Refs
        elif ItemToFind == "Trabajador":
            return Workers
        elif ItemToFind == "Proveedor":
            return Providers
        elif ItemToFind == "Referencia":
            return References
        elif ItemToFind == "Presentacion":
            return Presentations
        elif ItemToFind == "Numero de Remision":
            return NumRems
        elif ItemToFind == "Numero de Presentacion":
            return NumPres
        elif ItemToFind == "Numero de Bobinas":
            return NumCoils
        elif ItemToFind == "Numero de Bobinas Reitradas":
            return NumCoilsR
        elif ItemToFind == "Peso total de las bobinas":
            return TotalWeight
        elif ItemToFind == "Peso total retirado de las bobinas":
            return TotalWeightR
        elif ItemToFind == "Fecha Inicial":
            return InitialDate
        elif ItemToFind == "Fecha Final":
            return FinalDate
        elif ItemToFind == "Codigo de Barras":
            return CodeBr

    def FindObjMPR(Table:str, REF: str):
        if Table == "Normal":
            Type = 'sqlite:///lib/BDR.db'
        else:
            Type ='sqlite:///lib/PBDR.db'
        Ref, Worker, Provider, Reference, Presentation, Num_Rem, Num_Pre, Num_Coils, Num_CoilsR, Total_Weight, Total_WeightR, Initial_Date, Final_Date, CodeB = \
            SQLMPR.FindMPR(Type, REF)
        return (Provider, Reference, Presentation)