from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLMPR(Base):
   __tablename__ = 'DATOS_MATERIA_PRIMA_RETIRADO'
   Id = Column("ID", Integer, primary_key=True)
   Ref = Column("REF", String)
   Worker = Column("OPERADOR", String)
   Provider = Column("PROVEEDOR", String)
   Reference = Column("REFERENCIA", String)
   Presentation = Column("PRESENTACION", String)
   Num_Rem = Column("NUMERO_DE_REMISION", String)
   Num_Pre = Column("NUMERO_DE_PRESENTACION", Integer)
   Num_Coils = Column("NUMERO_DE_BOBINAS", Integer)
   Num_CoilsR = Column("NUMERO_DE_BOBINAS_RETIRADAS", Integer)
   Total_Weight = Column("PESO_TOTAL", Float)
   Total_WeightR = Column("PESO_TOTAL_RETIRADO", Float)
   Initial_Date = Column("FECHA_DE_INICIO", String)
   Final_Date = Column("FECHA_FINAL", String)
   CodeB = Column("CODIGO_DE_BARRAS", String)

   def FindMPR(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLMPR).all()
      session.close()
      for References in ref:
         if References.Ref == REFERENCE:
            return (References.Ref, References.Worker, References.Provider, References.Reference, References.Presentation,
                    References.Num_Rem, References.Num_Pre, References.Num_Coils, References.Num_CoilsR, References.Total_Weight,
                    References.Total_WeightR, References.Initial_Date, References.Final_Date, References.CodeB)

   def FindALLMPR(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLMPR).all()
      session.close()
      Refs = []
      Workers = []
      Providers = []
      References2 = []
      Presentations = []
      NumRems = []
      NumPres = []
      NumCoils = []
      NumCoilsR = []
      TotalWeight = []
      TotalWeightR = []
      InitialDate = []
      FinalDate = []
      CodeBr = []
      for References in ref:
         Refs.append(References.Ref)
         Workers.append(References.Worker)
         Providers.append(References.Provider)
         References2.append(References.Reference)
         Presentations.append(References.Presentation)
         NumRems.append(References.Num_Rem)
         NumPres.append(References.Num_Pre)
         NumCoils.append(References.Num_Coils)
         NumCoilsR.append(References.Num_CoilsR)
         TotalWeight.append(References.Total_Weight)
         TotalWeightR.append(References.Total_WeightR)
         InitialDate.append(References.Initial_Date)
         FinalDate.append(References.Final_Date)
         CodeBr.append(References.CodeBr)
      return (Refs, Workers, Providers, References2, Presentations, NumRems, NumPres, NumCoils, NumCoilsR, TotalWeight, TotalWeightR, InitialDate, FinalDate, CodeBr)

   def AddMPR(TABLA:str, REF: str, WORKER: str, PROVIDER: str, REFERENCE: str, PRESENTATION: str,
             NUM_REM: str, NUM_PRE: int, NUM_COILS:int, NUM_COILSR: int, TOTAL_WEIGHT: float,
             TOTAL_WEIGHTR: float, INITIAL_DATE: str, FINAL_DATE: str, CODEB: str
             ):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLMPR()
      MP.Ref = REF
      MP.Worker = WORKER
      MP.Provider = PROVIDER
      MP.Reference = REFERENCE
      MP.Presentation = PRESENTATION
      MP.Num_Rem = NUM_REM
      MP.Num_Pre = NUM_PRE
      MP.Num_Coils = NUM_COILS
      MP.Num_CoilsR = NUM_COILSR
      MP.Total_Weight = TOTAL_WEIGHT
      MP.Total_WeightR = TOTAL_WEIGHTR
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      MP.CodeB = CODEB
      session.add(MP)
      session.commit()
      session.close()

   def DeleteMPR(TABLA: str, REMISION: str, REFERENCIA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMPR).filter_by(Ref=REMISION).filter_by(Reference=REFERENCIA).delete()
      session.commit()
      session.close()

   def DeleteALLMPR(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMPR).delete()
      session.commit()
      session.close()

   def UpdateMPR(TABLA: str, REMISION: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      valueRef, ValueWork, ValueProv, ValueReference, ValuePres, ValueRem, ValueNunPre, ValueCoils, ValuerCoilsR, ValueTotalW, ValueTotalWR, ValueInDate, ValueFinalDate, ValueCode = SQLMPR.FindMPR(TABLA, REMISION)
      if DATO_MOD == "REF":
         session.query(SQLMPR).filter_by(Ref2=valueRef).update({SQLMPR.Ref2: Value})
      elif DATO_MOD == "OPERADOR":
         session.query(SQLMPR).filter_by(Worker=ValueWork).update({SQLMPR.Worker: Value})
      elif DATO_MOD == "PROVEEDOR":
         session.query(SQLMPR).filter_by(Provider=ValueProv).update({SQLMPR.Provider: Value})
      elif DATO_MOD == "REFERENCIA":
         session.query(SQLMPR).filter_by(Reference=ValueReference).update({SQLMPR.Reference: Value})
      elif DATO_MOD == "PRESENTACION":
         session.query(SQLMPR).filter_by(Presentation=ValuePres).update({SQLMPR.Presentation: Value})
      elif DATO_MOD == "NUMERO DE REMISION":
         session.query(SQLMPR).filter_by(Num_Rem=ValueRem).update({SQLMPR.Num_Rem: Value})
      elif DATO_MOD == "NUMERO DE PRESENTACION":
         session.query(SQLMPR).filter_by(Num_Pre=ValueNunPre).update({SQLMPR.Num_Pre: Value})
      elif DATO_MOD == "PESO TOTAL":
         session.query(SQLMPR).filter_by(Total_Weight=ValueTotalW).update({SQLMPR.Total_Weight: Value})
      elif DATO_MOD == "PESO RETIRADO":
         session.query(SQLMPR).filter_by(Total_WeightR=ValueTotalWR).update({SQLMPR.Total_WeightR: Value})
      elif DATO_MOD == "FECHA DE INICIO":
         session.query(SQLMPR).filter_by(Initial_Date=ValueInDate).update({SQLMPR.Initial_Date: Value})
      elif DATO_MOD == "FECHA FINAL":
         session.query(SQLMPR).filter_by(Final_Date=ValueFinalDate).update({SQLMPR.Final_Date: Value})
      elif DATO_MOD == "CODIGO DE BARRAS":
         session.query(SQLMPR).filter_by(Code=ValueCode).update({SQLMPR.Code: Value})
      elif DATO_MOD == "NUMERO DE BOBINAS":
         session.query(SQLMPR).filter_by(Num_Coils=ValueCoils).update({SQLMPR.Num_Coils: Value})
      elif DATO_MOD == "NUMERO DE BOBINAS RETIRADAS":
         session.query(SQLMPR).filter_by(Num_CoilsR=ValuerCoilsR).update({SQLMPR.Num_CoilsR: Value})
      session.commit()
      session.close()