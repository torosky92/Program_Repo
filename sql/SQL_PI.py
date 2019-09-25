from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLPI(Base):
   __tablename__ = 'PROCESO_INGRESO'
   Ref = Column("REF", Integer, primary_key=True)
   CodeB = Column("CODIGO DE BARRAS", String)
   Ref2 = Column("REF2", String)
   Num_Rem = Column("NUMERO_DE_REMISION", String)
   Num_Pre = Column("NUMERO_DE_CAJA", Integer)
   Num_Coils = Column("NUMERO_DE_BOBINAS", Integer)
   Weight = Column("PESO", Float)
   Measurement = Column("UNIDAD_DE_MEDIDA", String)

   def FindPI(REFERENCE: str):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLPI).all()
      session.close()
      for References in ref:
         if References.Ref2 == REFERENCE:
            return (References.CodeB, References.Ref2, References.Num_Rem, References.Num_Pre,
                    References.Num_Coils, References.Weight, References.Measurement)

   def AddPI(CODE: str, REF2: str, NUM_REM: str, NUM_PRE: int,
             NUM_COILS: int, WEIGHT: float, MEASUREMENT: str
             ):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      PI = SQLPI()
      PI.CodeB = CODE
      PI.Ref2 = REF2
      PI.Num_Rem = NUM_REM
      PI.Num_Pre = NUM_PRE
      PI.Num_Coils = NUM_COILS
      PI.Weight = WEIGHT
      PI.Measurement = MEASUREMENT
      session.add(PI)
      session.commit()
      session.close()

   def DeletePI(REMISION: str, REFERENCIA: str):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLPI).filter_by(Ref2=REMISION).filter_by(Reference=REFERENCIA).delete()
      session.commit()
      session.close()

   def DeleteALL(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLPI).delete()
      session.commit()
      session.close()

   def UpdatePI(REMISION: str, DATO_MOD, Value):
      engine = create_engine('sqlite:///lib/CN.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      valueCodeB, ValueRef2, ValueRem, ValueNumPre, ValueCoils, ValueW, ValueMeasurement = SQLPI.FindPI(REMISION)
      if DATO_MOD == "REF2":
         session.query(SQLPI).filter_by(Ref2=ValueRef2).update({SQLPI.Ref2: Value})
      elif DATO_MOD == "CODIGO DE BARRAS":
         session.query(SQLPI).filter_by(CodeB=valueCodeB).update({SQLPI.CodeB: Value})
      elif DATO_MOD == "NUMERO DE REMISION":
         session.query(SQLPI).filter_by(Num_Rem=ValueRem).update({SQLPI.Num_Rem: Value})
      elif DATO_MOD == "NUMERO DE PRESENTACION":
         session.query(SQLPI).filter_by(Num_Pre=ValueNumPre).update({SQLPI.Num_Pre: Value})
      elif DATO_MOD == "PESO":
         session.query(SQLPI).filter_by(Weight=ValueW).update({SQLPI.Total_Weight: Value})
      elif DATO_MOD == "UNIDAD DE MEDIDA":
         session.query(SQLPI).filter_by(Measurement=ValueMeasurement).update({SQLPI.Measurement: Value})
      elif DATO_MOD == "NUMERO DE BOBINAS":
         session.query(SQLPI).filter_by(Num_Coils=ValueCoils).update({SQLPI.Num_Coils: Value})
      session.commit()
      session.close()