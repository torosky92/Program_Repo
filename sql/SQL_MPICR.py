from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLMPICR(Base):
   __tablename__ = 'DATOS_MATERIA_PRIMA_IMPORTADO_CAJA_RETIRADO'
   Id = Column("ID", Integer, primary_key=True)
   CodeB = Column("CODIGO_DE_BARRAS", String)
   Num_Pre = Column("NUMERO_DE_PRESENTACION", Integer)
   Num_Rem = Column("NUMERO_DE_REMISION", String)
   Num_Coils = Column("NUMERO_DE_BOBINAS", Integer)
   Num_CoilsR = Column("NUMERO_DE_BOBINAS_RETIRADAS", Integer)
   Total_Weight = Column("PESO_TOTAL", Float)
   Total_WeightR = Column("PESO_TOTAL_RETIRADO", Float)
   Measurement = Column("UNIDAD_DE_MEDIDA", String)

   def FindMPICR(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLMPICR).all()
      session.close()
      for References in ref:
         if References.CodeB == REFERENCE:
            return (References.CodeB, References.Num_Pre, References.Num_Rem, References.Num_Coils, References.Num_CoilsR,
                    References.Total_Weight, References.Total_WeightR, References.Measurement)

   def FindsMPICR(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLMPICR).all()
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

   def FindALLMPICR(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLMPICR).all()
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

   def AddMPICR(TABLA:str, CODEB: str, NUM_REM: str, NUM_PRE: int, NUM_COILS:int, NUM_COILSR: int,
                TOTAL_WEIGHT: float, TOTAL_WEIGHTR: float, MEASUREMENT: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLMPICR()
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

   def DeleteMPICR(TABLA: str, CODEB: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMPICR).filter_by(CodeB=CODEB).delete()
      session.commit()
      session.close()

   def DeleteALLMPICR(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMPICR).delete()
      session.commit()
      session.close()

   def UpdateMPICR(TABLA: str, REMISION: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      valueCodeB, ValueNumPre, ValueNumRem, ValueCoils, ValuerCoilsR, ValueTotalW, ValueTotalWR, ValueMe = SQLMPICR.FindMPICR(TABLA, REMISION)
      if DATO_MOD == "CODIGO DE BARRAS":
         session.query(SQLMPICR).filter_by(CodeB=valueCodeB).update({SQLMPICR.CodeB: Value})
      elif DATO_MOD == "NUMERO DE REMISION":
         session.query(SQLMPICR).filter_by(Num_Rem=ValueNumRem).update({SQLMPICR.Num_Rem: Value})
      elif DATO_MOD == "NUMERO DE PRESENTACION":
         session.query(SQLMPICR).filter_by(Num_Pre=ValueNumPre).update({SQLMPICR.Num_Pre: Value})
      elif DATO_MOD == "PESO TOTAL":
         session.query(SQLMPICR).filter_by(Total_Weight=ValueTotalW).update({SQLMPICR.Total_Weight: Value})
      elif DATO_MOD == "PESO RETIRADO":
         session.query(SQLMPICR).filter_by(Total_WeightR=ValueTotalWR).update({SQLMPICR.Total_WeightR: Value})
      elif DATO_MOD == "NUMERO DE BOBINAS":
         session.query(SQLMPICR).filter_by(Num_Coils=ValueCoils).update({SQLMPICR.Num_Coils: Value})
      elif DATO_MOD == "NUMERO DE BOBINAS RETIRADAS":
         session.query(SQLMPICR).filter_by(Num_CoilsR=ValuerCoilsR).update({SQLMPICR.Num_CoilsR: Value})
      elif DATO_MOD == "UNIDAD DE MEDIDA":
         session.query(SQLMPICR).filter_by(Measurement=ValueMe).update({SQLMPICR.Measurement: Value})
      session.commit()
      session.close()