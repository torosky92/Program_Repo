from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLMPEC(Base):
   __tablename__ = 'MATERIA_PRIMA_ENKA_CAJA'
   Ref = Column("REF", Integer, primary_key=True)
   CodeB = Column("CODIGO DE BARRAS", String)
   Ref2 = Column("REF2", String)
   Num_Rem = Column("NUMERO_DE_REMISION", String)
   Num_Pre = Column("NUMERO_DE_CAJA", Integer)
   Num_Coils = Column("NUMERO_DE_BOBINAS", Integer)
   Weight = Column("PESO", Float)
   Measurement = Column("UNIDAD_DE_MEDIDA", String)

   def FindMPEC(REFERENCE: str):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLMPEC).all()
      session.close()
      for References in ref:
         if References.Ref2 == REFERENCE:
            return (References.CodeB, References.Ref2, References.Num_Rem, References.Num_Pre,
                    References.Num_Coils, References.Weight, References.Measurement)

   def AddMPEC(CODE: str, REF2: str, NUM_REM: str, NUM_PRE: int,
             NUM_COILS: int, WEIGHT: float, MEASUREMENT: str
             ):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      MPEC = SQLMPEC()
      MPEC.CodeB = CODE
      MPEC.Ref2 = REF2
      MPEC.Num_Rem = NUM_REM
      MPEC.Num_Pre = NUM_PRE
      MPEC.Num_Coils = NUM_COILS
      MPEC.Weight = WEIGHT
      MPEC.Measurement = MEASUREMENT
      session.add(MPEC)
      session.commit()
      session.close()

   def DeleteMPEC(REMISION: str, REFERENCIA: str):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMPEC).filter_by(Ref2=REMISION).filter_by(Reference=REFERENCIA).delete()
      session.commit()
      session.close()

   def UpdateMPEC(REMISION: str, DATO_MOD, Value):
      engine = create_engine('sqlite:///lib/CN.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      valueCodeB, ValueRef2, ValueRem, ValueNumPre, ValueCoils, ValueW, ValueMeasurement = SQLMPEC.FindMPEC(REMISION)
      if DATO_MOD == "REF2":
         session.query(SQLMPEC).filter_by(Ref2=ValueRef2).update({SQLMPEC.Ref2: Value})
      elif DATO_MOD == "CODIGO DE BARRAS":
         session.query(SQLMPEC).filter_by(CodeB=valueCodeB).update({SQLMPEC.CodeB: Value})
      elif DATO_MOD == "NUMERO DE REMISION":
         session.query(SQLMPEC).filter_by(Num_Rem=ValueRem).update({SQLMPEC.Num_Rem: Value})
      elif DATO_MOD == "NUMERO DE PRESENTACION":
         session.query(SQLMPEC).filter_by(Num_Pre=ValueNumPre).update({SQLMPEC.Num_Pre: Value})
      elif DATO_MOD == "PESO":
         session.query(SQLMPEC).filter_by(Weight=ValueW).update({SQLMPEC.Total_Weight: Value})
      elif DATO_MOD == "UNIDAD DE MEDIDA":
         session.query(SQLMPEC).filter_by(Measurement=ValueMeasurement).update({SQLMPEC.Measurement: Value})
      elif DATO_MOD == "NUMERO DE BOBINAS":
         session.query(SQLMPEC).filter_by(Num_Coils=ValueCoils).update({SQLMPEC.Num_Coils: Value})
      session.commit()
      session.close()