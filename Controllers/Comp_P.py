from sql.SQL_P import SQLP
# Peso
class findP:
    def Check_And_Add_ListP():
        Refs, CodeCs, Weight_tare, Weights, WeightD_tare, WeightD = SQLP.FindALLP('sqlite:///lib/CBDR.db')
        Refs2, CodeCs2, Weight_tare2, Weights2, WeightD_tare2, WeightD2 = SQLP.FindALLP('sqlite:///lib/CBDR.db')
        New_Refs = []
        New_CodeC = []
        New_Weight_tare = []
        New_Weight = []
        New_WeightD_tare = []
        New_WeightD = []
        for x in range(len(Refs)):
            if Refs[x] not in New_Refs:
                New_Refs.append(Refs[x])
                New_CodeC.append(CodeCs[x])
                New_Weight_tare.append(Weight_tare[x])
                New_Weight.append(Weights[x])
                New_WeightD_tare.append(WeightD_tare[x])
                New_WeightD.append(WeightD[x])
        for x in range(len(Refs2)):
            if Refs2[x] not in New_Refs:
                New_Refs.append(Refs2[x])
                New_CodeC.append(CodeCs2[x])
                New_Weight_tare.append(Weight_tare2[x])
                New_Weight.append(Weights2[x])
                New_WeightD_tare.append(WeightD_tare2[x])
                New_WeightD.append(WeightD2[x])
        SQLP.DeleteALLP('sqlite:///lib/CBDR.db')
        SQLP.DeleteALLP('sqlite:///lib/BDR.db')
        for x in range(len(New_Refs)):
            SQLP.AddP('sqlite:///lib/CBDR.db', New_Refs[x], New_CodeC[x], New_Weight_tare[x], New_Weight[x], New_WeightD_tare[x], New_WeightD[x])
            SQLP.AddP('sqlite:///lib/CBDR.db', New_Refs[x], New_CodeC[x], New_Weight_tare[x], New_Weight[x], New_WeightD_tare[x], New_WeightD[x])