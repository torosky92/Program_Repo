from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLMM(Base):
   __tablename__ = 'MEMORIA'
   Worker = Column("OPERADOR", String, primary_key=True)
   Provider = Column("PROVEEDOR", String)
   Reference = Column("REFERENCIA", String)
   Presentation = Column("PRESENTACION", String)
   Num_Rem = Column("NUMERO_DE_REMISION", String)
   Num_Pre = Column("NUMERO DE PRESENTACION", Integer)
   Total_Weight = Column("PESO TOTAL", Float)
   Ref2 = Column("NUMERO DE RECEPCION", String)
   Code = Column("CODIGO", String)

   def FindMM(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLMM).all()
      session.close()
      for References in ref:
         if References.Num_Rem == REFERENCE:
            return (References.Worker, References.Provider, References.Reference, References.Presentation,
                    References.Num_Rem, References.Num_Pre, References.Total_Weight, References.Ref2, References.Code)

   def FindALLMM(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLMM).all()
      session.close()
      New_Worker = []
      New_Provider = []
      New_Ref = []
      New_Presentation = []
      New_NumRem = []
      New_NumPre = []
      New_WeightT = []
      New_NumRec = []
      New_CodeB = []
      for References in ref:
         New_Worker.append(References.Worker)
         New_Provider.append(References.Provider)
         New_Ref.append(References.Reference)
         New_Presentation.append(References.Presentation)
         New_NumRem.append(References.Num_Rem)
         New_NumPre.append(References.Num_Pre)
         New_WeightT.append(References.Total_Weight)
         New_NumRec.append(References.Ref2)
         New_CodeB.append(References.Code)
      return (New_Worker, New_Provider, New_Ref, New_Presentation, New_NumRem, New_NumPre, New_WeightT, New_NumRec, New_CodeB)

   def AddMM(TABLA: str, WORKER: str, PROVIDER: str, REFERENCE: str, PRESENTATION: str,
             NUM_REM: str, NUM_PRE: int, TOTAL_WEIGHT: float, NUM_REC: str, CODE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MM = SQLMM()
      MM.Worker = WORKER
      MM.Provider = PROVIDER
      MM.Reference = REFERENCE
      MM.Presentation = PRESENTATION
      MM.Num_Rem = NUM_REM
      MM.Num_Pre = NUM_PRE
      MM.Total_Weight = TOTAL_WEIGHT
      MM.Ref2 = NUM_REC
      MM.Code = CODE
      session.add(MM)
      session.commit()
      session.close()

   def DeleteMM(TABLA: str, REMISION: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMM).filter_by(Num_Rem=REMISION).delete()
      session.commit()
      session.close()

   def DeleteALLMM(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMM).delete()
      session.commit()
      session.close()

   def UpdateMM(TABLA: str, REMISION: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      ValueWork, ValueProv, ValueReference, ValuePres, ValueRem, ValueNunPre, ValueTotalW, valueRef2, ValueCode = SQLMM.FindMM(TABLA, REMISION)
      if DATO_MOD == Settings.Var_Comp9(): session.query(SQLMM).filter_by(Ref2=valueRef2).update({SQLMM.Ref2: Value})
      elif DATO_MOD == Settings.Var_Comp15(): session.query(SQLMM).filter_by(Worker=ValueWork).update({SQLMM.Worker: Value})
      elif DATO_MOD == Settings.Var_Comp14(): session.query(SQLMM).filter_by(Provider=ValueProv).update({SQLMM.Provider: Value})
      elif DATO_MOD == Settings.Var_Comp13(): session.query(SQLMM).filter_by(Reference=ValueReference).update({SQLMM.Reference: Value})
      elif DATO_MOD == Settings.Var_Comp12(): session.query(SQLMM).filter_by(Presentation=ValuePres).update({SQLMM.Presentation: Value})
      elif DATO_MOD == Settings.Var_Comp2(): session.query(SQLMM).filter_by(Num_Rem=ValueRem).update({SQLMM.Num_Rem: Value})
      elif DATO_MOD == Settings.Var_Comp3(): session.query(SQLMM).filter_by(Num_Pre=ValueNunPre).update({SQLMM.Num_Pre: Value})
      elif DATO_MOD == Settings.Var_Comp8(): session.query(SQLMM).filter_by(Total_Weight=ValueTotalW).update({SQLMM.Total_Weight: Value})
      elif DATO_MOD == Settings.Var_Comp1(): session.query(SQLMM).filter_by(Code=ValueCode).update({SQLMM.Code: Value})
      session.commit()
      session.close()

   def CreateMM(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)