from sql.pr.SQL_MR import *
from Settings import Settings

# Montaje de retorcido
class findMR:
    def Check_And_Add_ListMR(NameTable: str):
        Refs, CodeCs, Workers, Machines, InitialD, FinalD, Num_works, Steameds, CodeBr = SQLFunctionTime.FindALLMR(NameTable, Settings.Dir_BDR())
        Refs2, CodeCs2, Workers2, Machines2, InitialD2, FinalD2, Num_works2, Steameds2, CodeBr2 = SQLFunctionTime.FindALLMR(NameTable, Settings.Dir_CBDR())
        New_Refs = []
        New_CodeC = []
        New_Worker = []
        New_Machine = []
        New_InitialD = []
        New_FinalD = []
        New_Works = []
        New_Steamed = []
        New_CodeB = []
        for x in range(len(Refs)):
            if Refs[x] not in New_Refs:
                New_Refs.append(Refs[x])
                New_CodeC.append(CodeCs[x])
                New_Worker.append(Workers[x])
                New_Machine.append(Machines[x])
                New_InitialD.append(InitialD[x])
                New_FinalD.append(FinalD[x])
                New_Works.append(Num_works[x])
                New_Steamed.append(Steameds[x])
                New_CodeB.append(CodeBr[x])
        for x in range(len(Refs2)):
            if Refs2[x] not in New_Refs:
                New_Refs.append(Refs2[x])
                New_CodeC.append(CodeCs2[x])
                New_Worker.append(Workers2[x])
                New_Machine.append(Machines2[x])
                New_InitialD.append(InitialD2[x])
                New_FinalD.append(FinalD2[x])
                New_Works.append(Num_works2[x])
                New_Steamed.append(Steameds2[x])
                New_CodeB.append(CodeBr2[x])
        SQLFunctionTime.DeleteALLMR(NameTable, Settings.Dir_CBDR())
        SQLFunctionTime.DeleteALLMR(NameTable, Settings.Dir_BDR())
        for x in range(len(New_Refs)):
            SQLFunctionTime.AddMR(NameTable, Settings.Dir_CBDR(), New_Refs[x], New_CodeC[x], New_Worker[x], New_Machine[x], New_InitialD[x], New_FinalD[x], New_Works[x], New_Steamed[x], New_CodeB[x])
            SQLFunctionTime.AddMR(NameTable, Settings.Dir_BDR(), New_Refs[x], New_CodeC[x], New_Worker[x], New_Machine[x], New_InitialD[x], New_FinalD[x], New_Works[x], New_Steamed[x], New_CodeB[x])