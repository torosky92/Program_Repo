from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLMT(Base):
   __tablename__ = 'TABLA'
   CodeB = Column("CODIGO_DE_BARRAS", String, primary_key=True)
   Num_Coils = Column("NUMERO_DE_BOBINAS", Integer)
   Weight = Column("PESO_NETO", Float)
   Measurament = Column("UNIDAD_DE_MEDIDA", String)

   def FindMT(CODE: str):
      engine = create_engine(Settings.Dir_BD(), echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLMT).all()
      session.close()
      for References in ref:
         if References.CodeB == CODE:
            return (References.CodeB, References.Num_Coils, References.Weight, References.Measurament)

   def FindALLMT():
      engine = create_engine(Settings.Dir_BD(), echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLMT).all()
      session.close()
      New_CodeB = []
      New_NumCoils = []
      New_Weight = []
      New_Measurament = []
      for References in ref:
         New_CodeB.append(References.Worker)
         New_NumCoils.append(References.Provider)
         New_Weight.append(References.Reference)
         New_Measurament.append(References.Presentation)
      return (New_CodeB, New_NumCoils, New_Weight, New_Measurament)

   def AddMT(CODE: str, NUM_COILS: int, WEIGHT: float, MEASURAMENT: str):
      engine = create_engine(Settings.Dir_BD(), echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MM = SQLMT()
      MM.CodeB = CODE
      MM.Num_Coils = NUM_COILS
      MM.Weight = WEIGHT
      MM.Measurament = MEASURAMENT
      session.add(MM)
      session.commit()
      session.close()

   def DeleteMT(CODE: str):
      engine = create_engine(Settings.Dir_BD(), echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMT).filter_by(CodeB=CODE).delete()
      session.commit()
      session.close()

   def DeleteALLMT():
      engine = create_engine(Settings.Dir_BD(), echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMT).delete()
      session.commit()
      session.close()

   def UpdateMT(CODE: str, DATO_MOD, Value):
      engine = create_engine(Settings.Dir_BD(), echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      ValueCode, ValueNumCoils, ValueWeight, ValueMeasurament = SQLMT.FindMT(CODE)
      if DATO_MOD == Settings.Var_Comp1(): session.query(SQLMT).filter_by(CodeB=ValueCode).update({SQLMT.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp6(): session.query(SQLMT).filter_by(Num_Coils=ValueNumCoils).update({SQLMT.Num_Coils: Value})
      elif DATO_MOD == Settings.Var_Comp8(): session.query(SQLMT).filter_by(Weight=ValueWeight).update({SQLMT.Weight: Value})
      elif DATO_MOD == Settings.Var_Comp32(): session.query(SQLMT).filter_by(Measurament=ValueMeasurament).update({SQLMT.Measurament: Value})
      session.commit()
      session.close()

   def CreateMT():
      engine = create_engine(Settings.Dir_BD(), echo=True)
      Base.metadata.create_all(bind=engine)