from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings
Base = declarative_base()

class Template1(object):
   Id = Column("REF", Integer, primary_key=True)
   CodeB = Column("CODIGO_DE_BARRAS", String)
   Num_Rec = Column("NUMERO_DE_RECEPCION", String)
   Num_Rem = Column("NUMERO_DE_REMISION", String)
   Num_Box = Column("NUMERO_DE_CAJA", Integer)
   Num_Coils = Column("NUMERO DE BOBINAS", Integer)
   Total_Weight = Column("PESO NETO", Float)
   Measurement = Column("UNIDAD DE MEDIDA", String)

class Template2(object):
   Id = Column("REF", Integer, primary_key=True)
   CodeB = Column("CODIGO_DE_BARRAS", String)
   Num_Rec = Column("NUMERO_DE_RECEPCION", String)
   Num_Rem = Column("NUMERO_DE_REMISION", String)
   Num_Box = Column("NUMERO_DE_ESTIBA", Integer)
   Num_Coils = Column("NUMERO DE BOBINAS", Integer)
   Total_Weight = Column("PESO NETO", Float)
   Measurement = Column("UNIDAD DE MEDIDA", String)

class MPECR(Template1, Base):
   __tablename__ = "MATERIA_PRIMA_ENKA_CAJA"

class MPEER(Template2, Base):
   __tablename__ = "MATERIA_PRIMA_ENKA_ESTIBAS"

class MPICR(Template1, Base):
   __tablename__ = "MATERIA_PRIMA_IMPORTADO_CAJA"

class MPIER(Template2, Base):
   __tablename__ = "MATERIA_PRIMA_IMPORTADO_ESTIBAS"

class SQLFunctionMPP:
   def FindMPP(NameTable: str, TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLFunctionMPP.WhichTable(NameTable)).all()
      session.close()
      for References in ref:
         if References.CodeB == REFERENCE:
            return (References.CodeB, References.Num_Rec, References.Num_Rem, References.Num_Box, References.Num_Coils,
                    References.Total_Weight, References.Measurement)

   def FindALLMPP(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLFunctionMPP.WhichTable(NameTable)).all()
      CodeBr = []
      NumRec = []
      NumRem = []
      NumBox = []
      NumCoils = []
      TotalW = []
      Measure = []
      for References in ref:
         CodeBr.append(References.CodeB)
         NumRec.append(References.Num_Rec)
         NumRem.append(References.Num_Rem)
         NumBox.append(References.Num_Box)
         NumCoils.append(References.Num_Coils)
         TotalW.append(References.Total_Weight)
         Measure.append(References.Measurement)
      session.close()
      return (CodeBr, NumRec, NumRem, NumBox, NumCoils, TotalW, Measure)

   def AddMPP(NameTable: str, TABLA:str, ID: int,  CODEB: str, NUM_REC: str, NUM_REM: str, NUM_BOX: int, NUM_COILS:int, TOTAL_WEIGHT: float, MEASUREMENT: str):
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
      MP.Id = ID
      MP.CodeB = CODEB
      MP.Num_Rec = NUM_REC
      MP.Num_Rem = NUM_REM
      MP.Num_Box = NUM_BOX
      MP.Num_Coils = NUM_COILS
      MP.Total_Weight = TOTAL_WEIGHT
      MP.Measurement = MEASUREMENT
      session.add(MP)
      session.commit()
      session.close()

   def DeleteMPP(NameTable: str, TABLA: str, CODEB: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLFunctionMPP.WhichTable(NameTable)).filter_by(CodeB=CODEB).delete()
      session.commit()
      session.close()

   def DeleteALLMPP(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLFunctionMPP.WhichTable(NameTable)).delete()
      session.commit()
      session.close()

   def UpdateMPP(NameTable: str, TABLA: str, REMISION: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      N_Table = SQLFunctionMPP.WhichTable(NameTable)
      valueCodeB, ValueNumRec, ValueNumRem, ValueBox, ValueCoils, ValueTotalW, ValueMe = SQLFunctionMPP.FindMPP(NameTable, TABLA, REMISION)
      if DATO_MOD == Settings.Var_Comp1(): session.query(N_Table).filter_by(CodeB=valueCodeB).update({N_Table.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp2(): session.query(N_Table).filter_by(Num_Rem=ValueNumRem).update({N_Table.Num_Rem: Value})
      elif DATO_MOD == Settings.Var_Comp9(): session.query(N_Table).filter_by(Num_Rec=ValueNumRec).update({N_Table.Num_Rec: Value})
      elif DATO_MOD == Settings.Var_Comp8(): session.query(N_Table).filter_by(Total_Weight=ValueTotalW).update({N_Table.Total_Weight: Value})
      elif DATO_MOD == Settings.Var_Comp3(): session.query(N_Table).filter_by(Num_Box=ValueBox).update({N_Table.Num_Box: Value})
      elif DATO_MOD == Settings.Var_Comp6(): session.query(N_Table).filter_by(Num_Coils=ValueCoils).update({N_Table.Num_Coils: Value})
      else: session.query(N_Table).filter_by(Measurement=ValueMe).update({N_Table.Measurement: Value})
      session.commit()
      session.close()

   def CreateTable(NameTable:str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Tabla = SQLFunctionMPP.WhichTable(NameTable)
      Tabla.metadata.create_all(engine)

   def WhichTable(NameTable: str):
      if NameTable == Settings.Var_EC(): return MPECR
      elif NameTable == Settings.Var_EE(): return MPEER
      elif NameTable == Settings.Var_IC(): return MPICR
      elif NameTable == Settings.Var_IE(): return MPIER