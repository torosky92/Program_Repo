from sql.SQL_PM import SQLPM
# Parado de Montaje
class findPM:
    def Check_And_Add_ListPM():
        Refs, CodeCs, Workers, Machines, Reasons, InitialD, FinalD = SQLPM.FindALLPM('sqlite:///lib/CBDR.db')
        Refs2, CodeCs2, Workers2, Machines2, Reasons2, InitialD2, FinalD2 = SQLPM.FindALLPM('sqlite:///lib/BDR.db')
        New_Refs = []
        New_CodeCs = []
        New_Workers = []
        New_Machines = []
        New_Initial = []
        New_Final = []
        for x in range(len(Refs)):
            if Refs[x] not in New_Refs:
                New_Refs.append(Refs[x])
                New_Workers.append(Workers[x])
                New_CodeCs.append(CodeCs[x])
                New_Machines.append(Machines[x])
                New_Initial.append(InitialD[x])
                New_Final.append(FinalD[x])
        for x in range(len(Refs2)):
            if Refs2[x] not in New_Refs:
                New_Refs.append(Refs2[x])
                New_Workers.append(Workers2[x])
                New_CodeCs.append(CodeCs2[x])
                New_Machines.append(Machines2[x])
                New_Initial.append(InitialD2[x])
                New_Final.append(FinalD2[x])
        SQLPM.DeleteALLPM('sqlite:///lib/CBDR.db')
        SQLPM.DeleteALLPM('sqlite:///lib/BDR.db')
        for x in range(len(New_Refs)):
            SQLPM.AddPM('sqlite:///lib/CBDR.db', New_Refs[x], New_Workers[x], New_CodeCs[x], New_Machines[x], New_Initial[x], New_Final[x])
            SQLPM.AddPM('sqlite:///lib/BDR.db', New_Refs[x], New_Workers[x], New_CodeCs[x], New_Machines[x], New_Initial[x], New_Final[x])