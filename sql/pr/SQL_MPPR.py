from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings
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
      ref = session.query(SQLFunction.WhichTable(NameTable)).all()
      session.close()
      for References in ref:
         if References.Num_Rem == REFERENCE:
            return (References.CodeB, References.Num_Pre, References.Num_Rem, References.Num_Coils, References.Num_CoilsR, References.Total_Weight, References.Total_WeightR, References.Measurement)
      return (" ", " ", " ", 0, 0, 0, 0, " ")

   def FindCodeBMPPR(NameTable: str, TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLFunction.WhichTable(NameTable)).all()
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

   def FindsMPPR(NameTable: str, TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLFunction.WhichTable(NameTable)).all()
      session.close()
      for References in ref:
         if References.CodeB == REFERENCE:
            return (References.CodeB, References.Num_Pre, References.Num_Rem, References.Num_Coils, References.Num_CoilsR, References.Total_Weight, References.Total_WeightR, References.Measurement)
      return (REFERENCE, "0", "0", 0, 0, 0, 0, "kg")

   def FindALLMPPR(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLFunction.WhichTable(NameTable)).all()
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
      if NameTable == Settings.Var_EC():
         MP = MPECR()
      elif NameTable == Settings.Var_EE():
         MP = MPEER()
      elif NameTable == Settings.Var_IC():
         MP = MPICR()
      elif NameTable == Settings.Var_IE():
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
      session.query(SQLFunction.WhichTable(NameTable)).filter_by(CodeB=CODEB).delete()
      session.commit()
      session.close()

   def DeleteALLMPPR(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLFunction.WhichTable(NameTable)).delete()
      session.commit()
      session.close()

   def UpdateMPPR(NameTable: str, TABLA: str, REMISION: str, CODE: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      N_Table = SQLFunction.WhichTable(NameTable)
      if DATO_MOD == Settings.Var_Comp1(): session.query(N_Table).filter_by(Num_Rem=REMISION).filter_by(CodeB=CODE).update({N_Table.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp2(): session.query(N_Table).filter_by(Num_Rem=REMISION).filter_by(CodeB=CODE).update({N_Table.Num_Rem: Value})
      elif DATO_MOD == Settings.Var_Comp3(): session.query(N_Table).filter_by(Num_Rem=REMISION).filter_by(CodeB=CODE).update({N_Table.Num_Pre: Value})
      elif DATO_MOD == Settings.Var_Comp4(): session.query(N_Table).filter_by(Num_Rem=REMISION).filter_by(CodeB=CODE).update({N_Table.Total_Weight: Value})
      elif DATO_MOD == Settings.Var_Comp5(): session.query(N_Table).filter_by(Num_Rem=REMISION).filter_by(CodeB=CODE).update({N_Table.Total_WeightR: Value})
      elif DATO_MOD == Settings.Var_Comp6(): session.query(N_Table).filter_by(Num_Rem=REMISION).filter_by(CodeB=CODE).update({N_Table.Num_Coils: Value})
      elif DATO_MOD == Settings.Var_Comp7(): session.query(N_Table).filter_by(Num_Rem=REMISION).filter_by(CodeB=CODE).update({N_Table.Num_CoilsR: Value})
      else: session.query(N_Table).filter_by(Num_Rem=REMISION).filter_by(CodeB=CODE).update({N_Table.Measurement: Value})
      session.commit()
      session.close()

   def CreateTable(NameTable:str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Tabla = SQLFunction.WhichTable(NameTable)
      Tabla.metadata.create_all(engine)

   def WhichTable(NameTable: str):
      if NameTable == Settings.Var_EC(): return MPECR
      elif NameTable == Settings.Var_EE(): return MPEER
      elif NameTable == Settings.Var_IC(): return MPICR
      elif NameTable == Settings.Var_IE(): return MPIER