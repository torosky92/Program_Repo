from Settings import Settings
from sql.pr.SQL_MPPR import SQLFunction
from sql.pr.SQL_MPR import SQLMPR
from sql.pmp.SQL_MPP import SQLFunctionMPP
from sql.pmp.SQL_MP import SQLMP

class Upgrade:
    def UpgradeMPP(NameTable: str):
        CodeBr2, NumPre2, NumRem2, NumBox2, NumCoils2, TotalW2, Measure2 = SQLFunctionMPP.FindALLMPP(NameTable,Settings.Dir_CBD())
        CodeBr, NumPre, NumRem, NumCoils, NumCoilsR, TotalW, TotalWR, Measure = SQLFunction.FindALLMPPR(NameTable,Settings.Dir_BDR())
        New_CodeB = []
        New_NumPre = []
        New_NumRem = []
        New_NumCoils = []
        New_NumCoilsR = []
        New_TotalW = []
        New_TotalWR = []
        New_Measure = []
        for x in range(len(CodeBr)):
            if CodeBr[x] not in New_CodeB:
                New_CodeB.append(CodeBr[x])
                New_NumPre.append(NumPre[x])
                New_NumRem.append(NumRem[x])
                New_NumCoils.append(NumCoils[x])
                New_NumCoilsR.append(NumCoilsR[x])
                New_TotalW.append(TotalW[x])
                New_TotalWR.append(TotalWR[x])
                New_Measure.append(Measure[x])
        for x in range(len(CodeBr2)):
            if CodeBr2[x] not in New_CodeB:
                New_CodeB.append(CodeBr2[x])
                New_NumPre.append(NumPre2[x])
                New_NumRem.append(NumRem2[x])
                New_NumCoils.append(NumCoils2[x])
                New_NumCoilsR.append(0)
                New_TotalW.append(TotalW2[x])
                New_TotalWR.append(0)
                New_Measure.append(Measure2[x])
        SQLFunction.DeleteALLMPPR(NameTable, Settings.Dir_BDR())
        for x in range(len(New_CodeB)):
            SQLFunction.AddMPPR(NameTable, Settings.Dir_BDR(), New_CodeB[x], New_NumRem[x], New_NumPre[x],
                                New_NumCoils[x], New_NumCoilsR[x], New_TotalW[x], New_TotalWR[x], New_Measure[x])

    def UpgradeMP():
        Ref2, Worker2, Provider2, Reference2, Presentation2, NumRem2, NumPre2, TotalWeight2, InitialD2, FinalD2, CodeB2, NumCoils2 = SQLMP.FindALLMP(Settings.Dir_CBD())
        Refs, Workers, Providers, References, Presentations, NumRems, NumPres, NumCoils, NumCoilsR, TotalWeight, TotalWeightR, InitialDate, FinalDate, CodeBr = SQLMPR.FindALLMPR(Settings.Dir_BDR())
        New_Refs = []
        New_Workers = []
        New_Providers = []
        New_References = []
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
        for x in range(len(Ref2)):
            if Ref2[x] not in New_Refs:
                New_Refs.append(Ref2[x])
                New_Workers.append(Worker2[x])
                New_Providers.append(Provider2[x])
                New_References.append(Reference2[x])
                New_Presentation.append(Presentation2[x])
                New_NumRem.append(NumRem2[x])
                New_NumPre.append(NumPre2[x])
                New_NumCoils.append(NumCoils2[x])
                New_NumCoilsR.append(0)
                New_TotalW.append(TotalWeight2[x])
                New_TotalWR.append(0)
                New_Initial.append(InitialD2[x])
                New_Final.append(FinalD2[x])
                New_CodeB.append(CodeB2[x])
        SQLMPR.DeleteALLMPR(Settings.Dir_BDR())
        for x in range(len(New_Refs)):
            SQLMPR.AddMPR(Settings.Dir_BDR(), New_Refs[x], New_Workers[x], New_Providers[x], New_References[x],
                          New_Presentation[x], New_NumRem[x], New_NumPre[x], New_NumCoils[x], New_NumCoilsR[x],
                          New_TotalW[x], New_TotalWR[x], New_Initial[x], New_Final[x], New_CodeB[x])