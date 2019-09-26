from sql.pr.SQL_T import SQLT
from Settings import Settings

# TABLA
class findT:
    def Check_And_Add_ListT():
        Lotes, Refs, Weights, WeightD = SQLT.FindALLT(Settings.Dir_CBDR())
        Lotes2, Refs2, Weights2, WeightD2 = SQLT.FindALLT(Settings.Dir_BDR())
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
        SQLT.DeleteALLT(Settings.Dir_CBDR())
        SQLT.DeleteALLT(Settings.Dir_BDR())
        for x in range(len(New_Refs)):
            SQLT.AddT(Settings.Dir_CBDR(), New_Lotes[x], New_Refs[x], New_Weight[x], New_WeightD[x])
            SQLT.AddT(Settings.Dir_BDR(), New_Lotes[x], New_Refs[x], New_Weight[x], New_WeightD[x])