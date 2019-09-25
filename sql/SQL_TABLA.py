from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLTABLA(Base):
   __tablename__ = 'MATERIAL_FINAL_DE_RETORCIDO'
   Id = Column("ID", Integer, primary_key=True)
   Lote = Column("LOTE", String)
   Ref = Column("REF", String)
   Weight = Column("PESO_NETO", Float)
   Weight_Desp = Column("PESO_DESPERDICION_NETO", Float)

   def FindTABLA(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLTABLA).all()
      session.close()
      for References in ref:
         if References.Ref == REFERENCE:
            return (References.Lote, References.Ref, References.Weight, References.Weight_Desp)

   def FindALLTABLA(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLTABLA).all()
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

   def AddTABLA(TABLA:str, LOTE: str, REF: str, WEIGHT: float, WEIGHT_DESP: float):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLTABLA()
      MP.Lote = LOTE
      MP.Ref = REF
      MP.Weight = WEIGHT
      MP.Weight_Desp = WEIGHT_DESP
      session.add(MP)
      session.commit()
      session.close()

   def DeleteTABLA(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLTABLA).filter_by(Ref=REFERENCE).delete()
      session.commit()
      session.close()

   def DeleteALLTABLA(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLTABLA).delete()
      session.commit()
      session.close()

   def UpdateTABLA(TABLA: str, REMISION: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      ValueLote, valueRef, ValueW, ValueWD = SQLTABLA.FindTABLA(TABLA, REMISION)
      if DATO_MOD == "REFERENCIA":
         session.query(SQLTABLA).filter_by(Ref=valueRef).update({SQLTABLA.Ref: Value})
      elif DATO_MOD == "LOTE":
         session.query(SQLTABLA).filter_by(Lote=ValueLote).update({SQLTABLA.Lote: Value})
      elif DATO_MOD == "PESO NETO":
         session.query(SQLTABLA).filter_by(Weight=ValueW).update({SQLTABLA.Weight: Value})
      elif DATO_MOD == "PESO DESPERDICIO":
         session.query(SQLTABLA).filter_by(Weight_Desp=ValueWD).update({SQLTABLA.Weight_Desp: Value})
      session.commit()
      session.close()