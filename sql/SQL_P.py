from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLP(Base):
   __tablename__ = 'PESO'
   Id = Column("ID", Integer, primary_key=True)
   Ref = Column("REFERENCIA", String)
   CodeC = Column("CODIGO_COLOR", String)
   Weight_Tare = Column("PESO_DE_TARA", Float)
   Weight = Column("PESO_NETO", Float)
   Weight_Desp_Tare = Column("PESO_DESPERDICION_TARA", Float)
   Weight_Desp = Column("PESO_DESPERDICION_NETO", Float)

   def FindP(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLP).all()
      session.close()
      for References in ref:
         if References.Ref == REFERENCE:
            return (References.Ref, References.CodeC, References.Weight_Tare, References.Weight, References.Weight_Desp_Tare, References.Weight_Desp)

   def FindALLP(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLP).all()
      session.close()
      Refs = []
      CodeCs = []
      Weight_tare = []
      Weights = []
      WeightD_tare = []
      WeightD = []
      for References in ref:
         Refs.append(References.Ref)
         CodeCs.append(References.CodeC)
         Weight_tare.append(References.Weight_Tare)
         Weights.append(References.Weight)
         WeightD_tare.append(References.Weight_Desp_Tare)
         WeightD.append(References.Weight_Desp)
      return (Refs, CodeCs, Weight_tare, Weights, WeightD_tare, WeightD)

   def AddP(TABLA:str, REF: str, CODEC: str, WEIGHT_TARE: float, WEIGHT: float, WEIGHT_DESP_TARE: float, WEIGHT_DESP: float):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLP()
      MP.Ref = REF
      MP.CodeC = CODEC
      MP.Weight_Tare = WEIGHT_TARE
      MP.Weight = WEIGHT
      MP.Weight_Desp_Tare = WEIGHT_DESP_TARE
      MP.Weight_Desp = WEIGHT_DESP
      session.add(MP)
      session.commit()
      session.close()

   def DeleteP(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLP).filter_by(Ref=REFERENCE).delete()
      session.commit()
      session.close()

   def DeleteALLP(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLP).delete()
      session.commit()
      session.close()

   def UpdateP(TABLA: str, REMISION: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      valueRef, ValueCodeC, ValueWeight_Tare, ValueWeight, ValueWeight_Desp_Tare, ValueWeight_Desp = SQLP.FindP(TABLA, REMISION)
      if DATO_MOD == "REFERENCIA":
         session.query(SQLP).filter_by(Ref=valueRef).update({SQLP.Ref: Value})
      elif DATO_MOD == "CODIGO DE COLORES":
         session.query(SQLP).filter_by(CodeC=ValueCodeC).update({SQLP.CodeC: Value})
      elif DATO_MOD == "PESO DE TARA":
         session.query(SQLP).filter_by(Weight_Tare=ValueWeight_Tare).update({SQLP.Weight_Tare: Value})
      elif DATO_MOD == "PESO NETO":
         session.query(SQLP).filter_by(Weight=ValueWeight).update({SQLP.Weight: Value})
      elif DATO_MOD == "PESO DESPERDICIO":
         session.query(SQLP).filter_by(Weight_Desp=ValueWeight_Desp).update({SQLP.Weight_Desp: Value})
      elif DATO_MOD == "PESO DESPERDICIO TARA":
         session.query(SQLP).filter_by(Weight_Desp_Tare=ValueWeight_Desp_Tare).update({SQLP.Weight_Desp_Tare: Value})
      session.commit()
      session.close()