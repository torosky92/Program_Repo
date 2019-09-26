from sql.pr.SQL_MFR import SQLMFR
from Settings import Settings

# Materia Final de Retorcido
class findMFR:
    def Check_And_Add_ListMFR():
        Lotes, Refs, CodeCs, References, Workers, Providers, Bottles, Weights, WeightDeps, Steameds, InitialD, FinalD = SQLMFR.FindALLMFR(Settings.Dir_BDR())
        Lotes2, Refs2, CodeCs2, References2, Workers2, Providers2, Bottles2, Weights2, WeightDeps2, Steameds2, InitialD2, FinalD2 = SQLMFR.FindALLMFR(Settings.Dir_CBDR())
        New_Lotes = []
        New_Refs = []
        New_CodeC = []
        New_References = []
        New_Worker = []
        New_Provider = []
        New_Bottles = []
        New_Weight = []
        New_WeightD = []
        New_Steamed = []
        New_InitialD = []
        New_FinalD = []
        for x in range(len(Refs)):
            if Refs[x] not in New_Refs:
                New_Lotes.append(Lotes[x])
                New_Refs.append(Refs[x])
                New_CodeC.append(CodeCs[x])
                New_References.append(References[x])
                New_Worker.append(Workers[x])
                New_Provider.append(Providers[x])
                New_Bottles.append(Bottles[x])
                New_Weight.append(Weights[x])
                New_WeightD.append(WeightDeps[x])
                New_Steamed.append(Steameds[x])
                New_InitialD.append(InitialD[x])
                New_FinalD.append(FinalD[x])
        for x in range(len(Refs2)):
            if Refs2[x] not in New_Refs:
                New_Lotes.append(Lotes2[x])
                New_Refs.append(Refs2[x])
                New_CodeC.append(CodeCs2[x])
                New_References.append(References2[x])
                New_Worker.append(Workers2[x])
                New_Provider.append(Providers2[x])
                New_Bottles.append(Bottles2[x])
                New_Weight.append(Weights2[x])
                New_WeightD.append(WeightDeps2[x])
                New_Steamed.append(Steameds2[x])
                New_InitialD.append(InitialD2[x])
                New_FinalD.append(FinalD2[x])
        SQLMFR.DeleteALLMFR(Settings.Dir_CBDR())
        SQLMFR.DeleteALLMFR(Settings.Dir_BDR())
        for x in range(len(New_Refs)):
            SQLMFR.AddMFR(Settings.Dir_CBDR(), New_Lotes[x], New_Refs[x], New_CodeC[x], New_References[x], New_Worker[x], New_Provider[x], New_Bottles[x], New_Weight[x], New_WeightD[x], New_Steamed[x], New_InitialD[x], New_FinalD[x])
            SQLMFR.AddMFR(Settings.Dir_BDR(), New_Lotes[x], New_Refs[x], New_CodeC[x], New_References[x], New_Worker[x], New_Provider[x], New_Bottles[x], New_Weight[x], New_WeightD[x], New_Steamed[x], New_InitialD[x], New_FinalD[x])