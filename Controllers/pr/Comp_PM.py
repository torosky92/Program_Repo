from sql.pr.SQL_PM import *
from Settings import Settings

# Parado de Montaje
class findPM:
    def Check_And_Add_ListPM(NameTable: str):
        Refs, CodeCs, Workers, Machines, Reasons, InitialD, FinalD = SQLFunctionPP.FindALLPM(NameTable, Settings.Dir_BDR())
        Refs2, CodeCs2, Workers2, Machines2, Reasons2, InitialD2, FinalD2 = SQLFunctionPP.FindALLPM(NameTable, Settings.Dir_CBDR())
        New_Refs = []
        New_CodeCs = []
        New_Workers = []
        New_Machines = []
        New_Reasons = []
        New_Initial = []
        New_Final = []
        for x in range(len(Refs)):
            if Refs[x] not in New_Refs:
                New_Refs.append(Refs[x])
                New_Workers.append(Workers[x])
                New_CodeCs.append(CodeCs[x])
                New_Machines.append(Machines[x])
                New_Reasons.append(Reasons[x])
                New_Initial.append(InitialD[x])
                New_Final.append(FinalD[x])
        for x in range(len(Refs2)):
            if Refs2[x] not in New_Refs:
                New_Refs.append(Refs2[x])
                New_Workers.append(Workers2[x])
                New_CodeCs.append(CodeCs2[x])
                New_Machines.append(Machines2[x])
                New_Reasons.append(Reasons2[x])
                New_Initial.append(InitialD2[x])
                New_Final.append(FinalD2[x])
        SQLFunctionPP.DeleteALLPM(NameTable, Settings.Dir_CBDR())
        SQLFunctionPP.DeleteALLPM(NameTable, Settings.Dir_BDR())
        for x in range(len(New_Refs)):
            SQLFunctionPP.AddPM(NameTable, Settings.Dir_CBDR(), New_Refs[x], New_Workers[x], New_CodeCs[x], New_Machines[x], New_Reasons[x], New_Initial[x], New_Final[x])
            SQLFunctionPP.AddPM(NameTable, Settings.Dir_BDR(), New_Refs[x], New_Workers[x], New_CodeCs[x], New_Machines[x], New_Reasons[x], New_Initial[x], New_Final[x])