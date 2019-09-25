from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine, Table, MetaData, inspect, Numeric
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Template(object):
   Id = Column("ID", Integer, primary_key=True)
   CodeB = Column("CODIGO_DE_BARRAS", String)
   Num_Pre = Column("NUMERO_DE_PRESENTACION", Integer)
   Num_Rem = Column("NUMERO_DE_REMISION", String)
   Num_Coils = Column("NUMERO_DE_BOBINAS", Integer)
   Num_CoilsR = Column("NUMERO_DE_BOBINAS_RETIRADAS", Integer)
   Total_Weight = Column("PESO_TOTAL", Float)
   Total_WeightR = Column("PESO_TOTAL_RETIRADO", Float)
   Measurement = Column("UNIDAD_DE_MEDIDA", String)

class MPECR(Template, Base):
   __tablename__ = "DATOS_MATERIA_PRIMA_ENKA_CAJA_RETIRADO"

class MPEER(Template, Base):
   __tablename__ = "DATOS_MATERIA_PRIMA_ENKA_ESTIBAS_RETIRADO"

class MPICR(Template, Base):
   __tablename__ = "DATOS_MATERIA_PRIMA_IMPORTADO_CAJA_RETIRADO"

class MPIER(Template, Base):
   __tablename__ = "DATOS_MATERIA_PRIMA_IMPORTADO_ESTIBAS_RETIRADO"

class SQLFunction:
   def FindMPPR(NameTable: str, TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      if NameTable == "ENKA CAJA":
         ref = session.query(MPECR()).all()
      elif NameTable == "ENKA ESTIBAS":
         ref = session.query(MPECR()).all()
      elif NameTable == "IMPORTADO CAJA":
         ref = session.query(MPICR()).all()
      else:
         ref = session.query(MPIER()).all()
      session.close()
      for References in ref:
         if References.CodeB == REFERENCE:
            return (References.CodeB, References.Num_Pre, References.Num_Rem, References.Num_Coils, References.Num_CoilsR,
                    References.Total_Weight, References.Total_WeightR, References.Measurement)

   def FindsMPPR(NameTable: str, TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      if NameTable == "ENKA CAJA":
         ref = session.query(MPECR()).all()
      elif NameTable == "ENKA ESTIBAS":
         ref = session.query(MPECR()).all()
      elif NameTable == "IMPORTADO CAJA":
         ref = session.query(MPICR()).all()
      else:
         ref = session.query(MPIER()).all()
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
      session.close()
      return (CodeBr, NumPre, NumRem, NumCoils, NumCoilsR, TotalW, TotalWR, Measure)

   def FindALLMPPR(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      if NameTable == "ENKA CAJA":
         ref = session.query(MPECR).all()
      elif NameTable == "ENKA ESTIBAS":
         ref = session.query(MPEER).all()
      elif NameTable == "IMPORTADO CAJA":
         ref = session.query(MPICR).all()
      else:
         ref = session.query(MPIER).all()
      print(ref)
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
      session.close()
      return (CodeBr, NumPre, NumRem, NumCoils, NumCoilsR, TotalW, TotalWR, Measure)

   def AddMPPR(NameTable: str, TABLA:str, CODEB: str, NUM_REM: str, NUM_PRE: int, NUM_COILS:int, NUM_COILSR: int,
                TOTAL_WEIGHT: float, TOTAL_WEIGHTR: float, MEASUREMENT: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      if NameTable == "ENKA CAJA":
         MP = MPECR()
      elif NameTable == "ENKA ESTIBAS":
         MP = MPECR()
      elif NameTable == "IMPORTADO CAJA":
         MP = MPICR()
      else:
         MP = MPIER()
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

   def DeleteMPPR(NameTable: str, TABLA: str, CODEB: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if NameTable == "ENKA CAJA":
         session.query(MPECR()).filter_by(CodeB=CODEB).delete()
      elif NameTable == "ENKA ESTIBAS":
         session.query(MPECR()).filter_by(CodeB=CODEB).delete()
      elif NameTable == "IMPORTADO CAJA":
         session.query(MPICR()).filter_by(CodeB=CODEB).delete()
      else:
         session.query(MPIER()).filter_by(CodeB=CODEB).delete()
      session.commit()
      session.close()

   def DeleteALLMPPR(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if NameTable == "ENKA CAJA":
         session.query(MPECR()).delete()
      elif NameTable == "ENKA ESTIBAS":
         session.query(MPEER()).delete()
      elif NameTable == "IMPORTADO CAJA":
         session.query(MPICR()).delete()
      else:
         session.query(MPIER()).delete()
      session.commit()
      session.close()

   def UpdateMPPR(NameTable: str, TABLA: str, REMISION: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if NameTable == "ENKA CAJA":
         valueCodeB, ValueNumPre, ValueNumRem, ValueCoils, ValuerCoilsR, ValueTotalW, ValueTotalWR, ValueMe = SQLFunction.FindMPPR(
            NameTable, TABLA, REMISION)
         if DATO_MOD == "CODIGO DE BARRAS":
            session.query(MPECR()).filter_by(CodeB=valueCodeB).update({SQLFunction.CodeB: Value})
         elif DATO_MOD == "NUMERO DE REMISION":
            session.query(MPECR()).filter_by(Num_Rem=ValueNumRem).update({SQLFunction.Num_Rem: Value})
         elif DATO_MOD == "NUMERO DE PRESENTACION":
            session.query(MPECR()).filter_by(Num_Pre=ValueNumPre).update({SQLFunction.Num_Pre: Value})
         elif DATO_MOD == "PESO TOTAL":
            session.query(MPECR()).filter_by(Total_Weight=ValueTotalW).update({SQLFunction.Total_Weight: Value})
         elif DATO_MOD == "PESO RETIRADO":
            session.query(MPECR()).filter_by(Total_WeightR=ValueTotalWR).update({SQLFunction.Total_WeightR: Value})
         elif DATO_MOD == "NUMERO DE BOBINAS":
            session.query(MPECR()).filter_by(Num_Coils=ValueCoils).update({SQLFunction.Num_Coils: Value})
         elif DATO_MOD == "NUMERO DE BOBINAS RETIRADAS":
            session.query(MPECR()).filter_by(Num_CoilsR=ValuerCoilsR).update({SQLFunction.Num_CoilsR: Value})
         elif DATO_MOD == "UNIDAD DE MEDIDA":
            session.query(MPECR()).filter_by(Measurement=ValueMe).update({SQLFunction.Measurement: Value})
      elif NameTable == "ENKA ESTIBAS":
         valueCodeB, ValueNumPre, ValueNumRem, ValueCoils, ValuerCoilsR, ValueTotalW, ValueTotalWR, ValueMe = SQLFunction.FindMPPR(
            NameTable, TABLA, REMISION)
         if DATO_MOD == "CODIGO DE BARRAS":
            session.query(MPEER()).filter_by(CodeB=valueCodeB).update({SQLFunction.CodeB: Value})
         elif DATO_MOD == "NUMERO DE REMISION":
            session.query(MPEER()).filter_by(Num_Rem=ValueNumRem).update({SQLFunction.Num_Rem: Value})
         elif DATO_MOD == "NUMERO DE PRESENTACION":
            session.query(MPEER()).filter_by(Num_Pre=ValueNumPre).update({SQLFunction.Num_Pre: Value})
         elif DATO_MOD == "PESO TOTAL":
            session.query(MPEER()).filter_by(Total_Weight=ValueTotalW).update({SQLFunction.Total_Weight: Value})
         elif DATO_MOD == "PESO RETIRADO":
            session.query(MPEER()).filter_by(Total_WeightR=ValueTotalWR).update({SQLFunction.Total_WeightR: Value})
         elif DATO_MOD == "NUMERO DE BOBINAS":
            session.query(MPEER()).filter_by(Num_Coils=ValueCoils).update({SQLFunction.Num_Coils: Value})
         elif DATO_MOD == "NUMERO DE BOBINAS RETIRADAS":
            session.query(MPEER()).filter_by(Num_CoilsR=ValuerCoilsR).update({SQLFunction.Num_CoilsR: Value})
         elif DATO_MOD == "UNIDAD DE MEDIDA":
            session.query(MPEER()).filter_by(Measurement=ValueMe).update({SQLFunction.Measurement: Value})
      elif NameTable == "IMPORTADO CAJA":
         valueCodeB, ValueNumPre, ValueNumRem, ValueCoils, ValuerCoilsR, ValueTotalW, ValueTotalWR, ValueMe = SQLFunction.FindMPPR(
            NameTable, TABLA, REMISION)
         if DATO_MOD == "CODIGO DE BARRAS":
            session.query(MPICR()).filter_by(CodeB=valueCodeB).update({SQLFunction.CodeB: Value})
         elif DATO_MOD == "NUMERO DE REMISION":
            session.query(MPICR()).filter_by(Num_Rem=ValueNumRem).update({SQLFunction.Num_Rem: Value})
         elif DATO_MOD == "NUMERO DE PRESENTACION":
            session.query(MPICR()).filter_by(Num_Pre=ValueNumPre).update({SQLFunction.Num_Pre: Value})
         elif DATO_MOD == "PESO TOTAL":
            session.query(MPICR()).filter_by(Total_Weight=ValueTotalW).update({SQLFunction.Total_Weight: Value})
         elif DATO_MOD == "PESO RETIRADO":
            session.query(MPICR()).filter_by(Total_WeightR=ValueTotalWR).update({SQLFunction.Total_WeightR: Value})
         elif DATO_MOD == "NUMERO DE BOBINAS":
            session.query(MPICR()).filter_by(Num_Coils=ValueCoils).update({SQLFunction.Num_Coils: Value})
         elif DATO_MOD == "NUMERO DE BOBINAS RETIRADAS":
            session.query(MPICR()).filter_by(Num_CoilsR=ValuerCoilsR).update({SQLFunction.Num_CoilsR: Value})
         elif DATO_MOD == "UNIDAD DE MEDIDA":
            session.query(MPICR()).filter_by(Measurement=ValueMe).update({SQLFunction.Measurement: Value})
      else:
         valueCodeB, ValueNumPre, ValueNumRem, ValueCoils, ValuerCoilsR, ValueTotalW, ValueTotalWR, ValueMe = SQLFunction.FindMPPR(
            NameTable, TABLA, REMISION)
         if DATO_MOD == "CODIGO DE BARRAS":
            session.query(MPIER()).filter_by(CodeB=valueCodeB).update({SQLFunction.CodeB: Value})
         elif DATO_MOD == "NUMERO DE REMISION":
            session.query(MPIER()).filter_by(Num_Rem=ValueNumRem).update({SQLFunction.Num_Rem: Value})
         elif DATO_MOD == "NUMERO DE PRESENTACION":
            session.query(MPIER()).filter_by(Num_Pre=ValueNumPre).update({SQLFunction.Num_Pre: Value})
         elif DATO_MOD == "PESO TOTAL":
            session.query(MPIER()).filter_by(Total_Weight=ValueTotalW).update({SQLFunction.Total_Weight: Value})
         elif DATO_MOD == "PESO RETIRADO":
            session.query(MPIER()).filter_by(Total_WeightR=ValueTotalWR).update({SQLFunction.Total_WeightR: Value})
         elif DATO_MOD == "NUMERO DE BOBINAS":
            session.query(MPIER()).filter_by(Num_Coils=ValueCoils).update({SQLFunction.Num_Coils: Value})
         elif DATO_MOD == "NUMERO DE BOBINAS RETIRADAS":
            session.query(MPIER()).filter_by(Num_CoilsR=ValuerCoilsR).update({SQLFunction.Num_CoilsR: Value})
         elif DATO_MOD == "UNIDAD DE MEDIDA":
            session.query(MPIER()).filter_by(Measurement=ValueMe).update({SQLFunction.Measurement: Value})
      session.commit()
      session.close()