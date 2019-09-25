from sql.SQL_PP import SQLPP
# Parado de proceso
class findPP:
    def Check_And_Add_ListPP():
        Refs, CodeCs, Workers, Machines, Reasons, InitialD, FinalD = SQLPP.FindALLPP('sqlite:///lib/CBDR.db')
        Refs2, CodeCs2, Workers2, Machines2, Reasons2, InitialD2, FinalD2 = SQLPP.FindALLPP('sqlite:///lib/BDR.db')
        New_Refs = []
        New_CodeC = []
        New_Worker = []
        New_Machine = []
        New_Reason = []
        New_InitialD = []
        New_FinalD = []
        for x in range(len(Refs)):
            if Refs[x] not in New_Refs:
                New_Refs.append(Refs[x])
                New_CodeC.append(CodeCs[x])
                New_Worker.append(Workers[x])
                New_Machine.append(Machines[x])
                New_Reason.append(Reasons[x])
                New_InitialD.append(InitialD[x])
                New_FinalD.append(FinalD[x])
        for x in range(len(Refs2)):
            if Refs2[x] not in New_Refs:
                New_Refs.append(Refs2[x])
                New_CodeC.append(CodeCs2[x])
                New_Worker.append(Workers2[x])
                New_Machine.append(Machines2[x])
                New_Reason.append(Reasons2[x])
                New_InitialD.append(InitialD2[x])
                New_FinalD.append(FinalD2[x])
        SQLPP.DeleteALLPP('sqlite:///lib/CBDR.db')
        SQLPP.DeleteALLPP('sqlite:///lib/BDR.db')
        for x in range(len(New_Refs)):
            SQLPP.AddPP('sqlite:///lib/CBDR.db', New_Refs[x], New_CodeC[x], New_Worker[x], New_Machine[x], New_Reason[x], New_InitialD[x], New_FinalD[x])
            SQLPP.AddPP('sqlite:///lib/BDR.db', New_Refs[x], New_CodeC[x], New_Worker[x], New_Machine[x], New_Reason[x], New_InitialD[x], New_FinalD[x])