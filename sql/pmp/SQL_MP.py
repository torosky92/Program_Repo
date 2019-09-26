from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings
Base = declarative_base()

class SQLMP(Base):
   __tablename__ = 'DATOS_MATERIA_PRIMA'
   Ref = Column("REF", Integer, primary_key=True)
   Ref2 = Column("REF2", String)
   Worker = Column("OPERADOR", String)
   Provider = Column("PROVEEDOR", String)
   Reference = Column("REFERENCIA", String)
   Presentation = Column("PRESENTACION", String)
   Num_Rem = Column("NUMERO DE REMISION", String)
   Num_Pre = Column("NUMERO DE PRESENTACION", Integer)
   Total_Weight = Column("PESO TOTAL", Float)
   Initial_Date = Column("FECHA INICIO", String)
   Final_Date = Column("FECHA FINAL", String)
   Code = Column("CODIGO BARRAS", String)
   Num_Coils = Column("NUMERO DE BOBINAS", Integer)

   def FindMP(TABLA:str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLMP).all()
      session.close()
      for References in ref:
         if References.Ref2 == REFERENCE:
            return (References.Ref2, References.Worker, References.Provider, References.Reference, References.Presentation,
                    References.Num_Rem, References.Num_Pre, References.Total_Weight, References.Initial_Date, References.Final_Date,
                    References.Code, References.Num_Coils)

   def FindALLMP(TABLA:str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLMP).all()
      session.close()
      New_Ref2 = []
      New_Worker = []
      New_Provider = []
      New_Reference = []
      New_Presentation = []
      New_NumRem = []
      New_NumPre = []
      New_WeightT = []
      New_InitialD = []
      New_FinalD = []
      New_CodeB = []
      New_Num_Coils = []
      for References in ref:
         New_Ref2.append(References.Ref2)
         New_Worker.append(References.Worker)
         New_Provider.append(References.Provider)
         New_Reference.append(References.Reference)
         New_Presentation.append(References.Presentation)
         New_NumRem.append(References.Num_Rem)
         New_NumPre.append(References.Num_Pre)
         New_WeightT.append(References.Total_Weight)
         New_InitialD.append(References.Initial_Date)
         New_FinalD.append(References.Final_Date)
         New_CodeB.append(References.Code)
         New_Num_Coils.append(References.Num_Coils)
      return (New_Ref2, New_Worker, New_Provider, New_Reference, New_Presentation, New_NumRem, New_NumPre,
              New_WeightT, New_InitialD, New_FinalD, New_CodeB, New_Num_Coils)

   def AddMP(TABLA: str, ID:int, REF2: str, WORKER: str, PROVIDER: str, REFERENCE: str,
             PRESENTATION: str, NUM_REM: str, NUM_PRE: int, TOTAL_WEIGHT: float,
             INITIAL_DATE: str, FINAL_DATE: str, CODE: str, NUM_COILS: int
             ):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLMP()
      MP.Ref =ID
      MP.Ref2 = REF2
      MP.Worker = WORKER
      MP.Provider = PROVIDER
      MP.Reference = REFERENCE
      MP.Presentation = PRESENTATION
      MP.Num_Rem = NUM_REM
      MP.Num_Pre = NUM_PRE
      MP.Total_Weight = TOTAL_WEIGHT
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      MP.Code = CODE
      MP.Num_Coils = NUM_COILS
      session.add(MP)
      session.commit()
      session.close()

   def DeleteMP(TABLA: str, REMISION: str, REFERENCIA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMP).filter_by(Num_Rem=REMISION).filter_by(Reference=REFERENCIA).delete()
      session.commit()
      session.close()

   def DeleteALLMP(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMP).delete()
      session.commit()
      session.close()

   def UpdateMP(TABLA: str, REMISION: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      valueRef2, ValueWork, ValueProv, ValueReference, ValuePres, ValueRem, ValueNunPre, ValueTotalW, ValueInDate, ValueFinalDate, ValueCode, ValueCoils = SQLMP.FindMP(TABLA, REMISION)
      if DATO_MOD == Settings.Var_Comp26(): session.query(SQLMP).filter_by(Ref2=valueRef2).update({SQLMP.Ref2: Value})
      elif DATO_MOD == Settings.Var_Comp15(): session.query(SQLMP).filter_by(Worker=ValueWork).update({SQLMP.Worker: Value})
      elif DATO_MOD == Settings.Var_Comp14(): session.query(SQLMP).filter_by(Provider=ValueProv).update({SQLMP.Provider: Value})
      elif DATO_MOD == Settings.Var_Comp13(): session.query(SQLMP).filter_by(Reference=ValueReference).update({SQLMP.Reference: Value})
      elif DATO_MOD == Settings.Var_Comp12(): session.query(SQLMP).filter_by(Presentation=ValuePres).update({SQLMP.Presentation: Value})
      elif DATO_MOD == Settings.Var_Comp2(): session.query(SQLMP).filter_by(Num_Rem=ValueRem).update({SQLMP.Num_Rem: Value})
      elif DATO_MOD == Settings.Var_Comp3(): session.query(SQLMP).filter_by(Num_Pre=ValueNunPre).update({SQLMP.Num_Pre: Value})
      elif DATO_MOD == Settings.Var_Comp4(): session.query(SQLMP).filter_by(Total_Weight=ValueTotalW).update({SQLMP.Total_Weight: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(SQLMP).filter_by(Initial_Date=ValueInDate).update({SQLMP.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(SQLMP).filter_by(Final_Date=ValueFinalDate).update({SQLMP.Final_Date: Value})
      elif DATO_MOD == Settings.Var_Comp1(): session.query(SQLMP).filter_by(Code=ValueCode).update({SQLMP.Code: Value})
      elif DATO_MOD == Settings.Var_Comp6(): session.query(SQLMP).filter_by(Num_Coils=ValueCoils).update({SQLMP.Num_Coils: Value})
      session.commit()
      session.close()

   def CreateMP(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)