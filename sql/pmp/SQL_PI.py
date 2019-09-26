from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLPI(Base):
   __tablename__ = 'PROCESO_INGRESO'
   Ref = Column("REF", Integer, primary_key=True)
   CodeB = Column("CODIGO_DE_BARRAS", String)
   Ref2 = Column("NUMERO_RECEPCION", String)
   Num_Rem = Column("NUMERO_REMISION", String)
   Num_Pre = Column("NUMERO_PEDIDO", Integer)
   Num_Coils = Column("NUMERO_BOBINAS", Integer)
   Weight = Column("PESO_PEDIDO", Float)
   Measurement = Column("UNIDAD_MEDIDA", String)

   def FindALLPI():
      engine = create_engine(Settings.Dir_BD(), echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLPI).all()
      session.close()
      New_CodeB = []
      New_Ref2 = []
      New_NumRem = []
      New_NumPre = []
      New_NumCoils = []
      New_Weight = []
      New_Measurement = []
      for References in ref:
         New_CodeB.append(References.CodeB)
         New_Ref2.append(References.Ref2)
         New_NumRem.append(References.Num_Rem)
         New_NumPre.append(References.Num_Pre)
         New_NumCoils.append(References.Num_Coils)
         New_Weight.append(References.Weight)
         New_Measurement.append(References.Measurement)
      return (New_CodeB, New_Ref2, New_NumRem, New_NumPre, New_NumCoils, New_Weight, New_Measurement)

   def FindPI(REFERENCE: str):
      engine = create_engine(Settings.Dir_BD(), echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLPI).all()
      session.close()
      for References in ref:
         if References.Ref2 == REFERENCE:
            return (References.CodeB, References.Ref2, References.Num_Rem, References.Num_Pre,
                    References.Num_Coils, References.Weight, References.Measurement)

   def AddPI(REF:int, CODE: str, NUM_REC: str, NUM_REM: str, NUM_PRE: int,
             NUM_COILS: int, WEIGHT: float, MEASUREMENT: str):
      engine = create_engine(Settings.Dir_BD(), echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      PI = SQLPI()
      PI.Ref = REF
      PI.CodeB = CODE
      PI.Ref2 = NUM_REC
      PI.Num_Rem = NUM_REM
      PI.Num_Pre = NUM_PRE
      PI.Num_Coils = NUM_COILS
      PI.Weight = WEIGHT
      PI.Measurement = MEASUREMENT
      session.add(PI)
      session.commit()
      session.close()

   def DeletePI(REMISION: str):
      engine = create_engine(Settings.Dir_BD(), echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLPI).filter_by(Ref2=REMISION).delete()
      session.commit()
      session.close()

   def DeleteALLPI():
      engine = create_engine(Settings.Dir_BD(), echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLPI).delete()
      session.commit()
      session.close()

   def UpdatePI(REMISION: str, DATO_MOD, Value):
      engine = create_engine(Settings.Dir_BD(), echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      valueCodeB, ValueRef2, ValueRem, ValueNumPre, ValueCoils, ValueW, ValueMeasurement = SQLPI.FindPI(REMISION)
      if DATO_MOD == Settings.Var_Comp9(): session.query(SQLPI).filter_by(Ref2=ValueRef2).update({SQLPI.Ref2: Value})
      elif DATO_MOD == Settings.Var_Comp1(): session.query(SQLPI).filter_by(CodeB=valueCodeB).update({SQLPI.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp2(): session.query(SQLPI).filter_by(Num_Rem=ValueRem).update({SQLPI.Num_Rem: Value})
      elif DATO_MOD == Settings.Var_Comp3(): session.query(SQLPI).filter_by(Num_Pre=ValueNumPre).update({SQLPI.Num_Pre: Value})
      elif DATO_MOD == Settings.Var_Comp8(): session.query(SQLPI).filter_by(Weight=ValueW).update({SQLPI.Total_Weight: Value})
      elif DATO_MOD == Settings.Var_Comp32(): session.query(SQLPI).filter_by(Measurement=ValueMeasurement).update({SQLPI.Measurement: Value})
      elif DATO_MOD == Settings.Var_Comp6(): session.query(SQLPI).filter_by(Num_Coils=ValueCoils).update({SQLPI.Num_Coils: Value})
      session.commit()
      session.close()

   def CreatePI():
      engine = create_engine(Settings.Dir_BD(), echo=True)
      Base.metadata.create_all(bind=engine)