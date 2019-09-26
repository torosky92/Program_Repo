from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLT(Base):
   __tablename__ = 'TABLA DE LOTE'
   Id = Column("ID", Integer, primary_key=True)
   Lote = Column("LOTE", String)
   Ref = Column("REF", String)
   Weight = Column("PESO_NETO", Float)
   Weight_Desp = Column("PESO_DESPERDICION_NETO", Float)

   def FindT(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLT).all()
      session.close()
      for References in ref:
         if References.Ref == REFERENCE:
            return (References.Lote, References.Ref, References.Weight, References.Weight_Desp)

   def FindALLT(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLT).all()
      session.close()
      Lotes = []
      Refs = []
      Weights = []
      WeightD = []
      for References in ref:
         Lotes.append(References.Lote)
         Refs.append(References.Ref)
         Weights.append(References.Weight)
         WeightD.append(References.Weight_Desp)
      return (Lotes, Refs, Weights, WeightD)

   def AddT(TABLA:str, LOTE: str, REF: str, WEIGHT: float, WEIGHT_DESP: float):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLT()
      MP.Lote = LOTE
      MP.Ref = REF
      MP.Weight = WEIGHT
      MP.Weight_Desp = WEIGHT_DESP
      session.add(MP)
      session.commit()
      session.close()

   def DeleteT(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLT).filter_by(Ref=REFERENCE).delete()
      session.commit()
      session.close()

   def DeleteALLT(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLT).delete()
      session.commit()
      session.close()

   def UpdateT(TABLA: str, REMISION: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      ValueLote, valueRef, ValueW, ValueWD = SQLT.FindTABLA(TABLA, REMISION)
      if DATO_MOD == Settings.Var_Comp13(): session.query(SQLT).filter_by(Ref=valueRef).update({SQLT.Ref: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(SQLT).filter_by(Lote=ValueLote).update({SQLT.Lote: Value})
      elif DATO_MOD == Settings.Var_Comp8(): session.query(SQLT).filter_by(Weight=ValueW).update({SQLT.Weight: Value})
      elif DATO_MOD == Settings.Var_Comp28(): session.query(SQLT).filter_by(Weight_Desp=ValueWD).update({SQLT.Weight_Desp: Value})
      session.commit()
      session.close()

   def CreateT(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)