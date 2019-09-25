import numpy as np
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLMPECR(Base):
   __tablename__ = 'MATERIA_PRIMA_ENKA_CAJA_RETIRADO'
   Id = Column("ID", Integer, primary_key=True)
   CodeB = Column("CODIGO_DE_BARRAS", String)
   Num_Pre = Column("NUMERO_DE_PRESENTACION", Integer)
   Num_Rem = Column("NUMERO_DE_REMISION", String)
   Num_Coils = Column("NUMERO_DE_BOBINAS", Integer)
   Num_CoilsR = Column("NUMERO_DE_BOBINAS_RETIRADAS", Integer)
   Total_Weight = Column("PESO_TOTAL", Float)
   Total_WeightR = Column("PESO_TOTAL_RETIRADO", Float)
   Measurement = Column("UNIDAD_DE_MEDIDA", String)

   def FindMPECR(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLMPECR).all()
      session.close()
      for References in ref:
         if References.CodeB == REFERENCE:
            return (References.CodeB, References.Num_Pre, References.Num_Rem, References.Num_Coils, References.Num_CoilsR,
                    References.Total_Weight, References.Total_WeightR, References.Measurement)

   def FindsMPECR(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLMPECR).all()
      session.close()
      CodeBr = []
      NumPre = []
      NumRem = []
      NumCoils = []
      NumCoilsR = []
      TotalW = []
      TotalWR = []
      Measure = []
      for References in ref:
         if References.Num_Rem == REFERENCE:
            CodeBr.append(References.CodeB)
            NumPre.append(References.Num_Pre)
            NumRem.append(References.Num_Rem)
            NumCoils.append(References.Num_Coils)
            NumCoilsR.append(References.Num_CoilsR)
            TotalW.append(References.Total_Weight)
            TotalWR.append(References.Total_WeightR)
            Measure.append(References.Measurement)
      return (CodeBr, NumPre, NumRem, NumCoils, NumCoilsR, TotalW, TotalWR, Measure)

   def FindALLMPECR(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLMPECR).all()
      session.close()
      CodeBr = []
      NumPre = []
      NumRem = []
      NumCoils = []
      NumCoilsR = []
      TotalW = []
      TotalWR = []
      Measure = []
      for References in ref:
         CodeBr.append(References.CodeB)
         NumPre.append(References.Num_Pre)
         NumRem.append(References.Num_Rem)
         NumCoils.append(References.Num_Coils)
         NumCoilsR.append(References.Num_CoilsR)
         TotalW.append(References.Total_Weight)
         TotalWR.append(References.Total_WeightR)
         Measure.append(References.Measurement)
      return (CodeBr, NumPre, NumRem, NumCoils, NumCoilsR, TotalW, TotalWR, Measure)

   def AddMPECR(TABLA:str, CODEB: str, NUM_REM: str, NUM_PRE: int, NUM_COILS:int, NUM_COILSR: int,
                TOTAL_WEIGHT: float, TOTAL_WEIGHTR: float, MEASUREMENT: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLMPECR()
      MP.CodeB = CODEB
      MP.Num_Rem = NUM_REM
      MP.Num_Pre = NUM_PRE
      MP.Num_Coils = NUM_COILS
      MP.Num_CoilsR = NUM_COILSR
      MP.Total_Weight = TOTAL_WEIGHT
      MP.Total_WeightR = TOTAL_WEIGHTR
      MP.Measurement = MEASUREMENT
      session.add(MP)
      session.commit()
      session.close()

   def DeleteMPECR(TABLA: str, CODEB: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMPECR).filter_by(CodeB=CODEB).delete()
      session.commit()
      session.close()

   def DeleteALLMPECR(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMPECR).delete()
      session.commit()
      session.close()

   def UpdateMPECR(TABLA: str, REMISION: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      valueCodeB, ValueNumPre, ValueNumRem, ValueCoils, ValuerCoilsR, ValueTotalW, ValueTotalWR, ValueMe = SQLMPECR.FindMPECR(TABLA, REMISION)
      if DATO_MOD == "CODIGO DE BARRAS":
         session.query(SQLMPECR).filter_by(CodeB=valueCodeB).update({SQLMPECR.CodeB: Value})
      elif DATO_MOD == "NUMERO DE REMISION":
         session.query(SQLMPECR).filter_by(Num_Rem=ValueNumRem).update({SQLMPECR.Num_Rem: Value})
      elif DATO_MOD == "NUMERO DE PRESENTACION":
         session.query(SQLMPECR).filter_by(Num_Pre=ValueNumPre).update({SQLMPECR.Num_Pre: Value})
      elif DATO_MOD == "PESO TOTAL":
         session.query(SQLMPECR).filter_by(Total_Weight=ValueTotalW).update({SQLMPECR.Total_Weight: Value})
      elif DATO_MOD == "PESO RETIRADO":
         session.query(SQLMPECR).filter_by(Total_WeightR=ValueTotalWR).update({SQLMPECR.Total_WeightR: Value})
      elif DATO_MOD == "NUMERO DE BOBINAS":
         session.query(SQLMPECR).filter_by(Num_Coils=ValueCoils).update({SQLMPECR.Num_Coils: Value})
      elif DATO_MOD == "NUMERO DE BOBINAS RETIRADAS":
         session.query(SQLMPECR).filter_by(Num_CoilsR=ValuerCoilsR).update({SQLMPECR.Num_CoilsR: Value})
      elif DATO_MOD == "UNIDAD DE MEDIDA":
         session.query(SQLMPECR).filter_by(Measurement=ValueMe).update({SQLMPECR.Measurement: Value})
      session.commit()
      session.close()