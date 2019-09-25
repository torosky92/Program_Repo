from sql.SQL_TABLA import SQLTABLA
# TABLA
class findTABLA:
    def Check_And_Add_ListTALBA(): #Materia prima enka caja retirada
        Lotes, Refs, Weights, WeightD = SQLTABLA.FindALLTABLA('sqlite:///lib/CBDR.db')
        Lotes2, Refs2, Weights2, WeightD2 = SQLTABLA.FindALLTABLA('sqlite:///lib/BDR.db')
        New_Lotes = []
        New_Refs = []
        New_Weight = []
        New_WeightD = []
        for x in range(len(Refs)):
            if Refs[x] not in New_Refs:
                New_Lotes.append(Lotes[x])
                New_Refs.append(Refs[x])
                New_Weight.append(Weights[x])
                New_WeightD.append(WeightD[x])
        for x in range(len(Refs2)):
            if Refs2[x] not in New_Refs:
                New_Lotes.append(Lotes2[x])
                New_Refs.append(Refs2[x])
                New_Weight.append(Weights2[x])
                New_WeightD.append(WeightD2[x])
        SQLTABLA.DeleteALLTABLA('sqlite:///lib/CBDR.db')
        SQLTABLA.DeleteALLTABLA('sqlite:///lib/BDR.db')
        for x in range(len(New_Refs)):
            SQLTABLA.AddTABLA('sqlite:///lib/CBDR.db', New_Lotes[x], New_Refs[x], New_Weight[x], New_WeightD[x])
            SQLTABLA.AddTABLA('sqlite:///lib/BDR.db', New_Lotes[x], New_Refs[x], New_Weight[x], New_WeightD[x])