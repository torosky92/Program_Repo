from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class Template(object):
   Id = Column("REF", Integer, primary_key=True)
   CodeB = Column("CODIGO BARRAS", String)
   Lote = Column("LOTE", String)
   Code = Column("CODIGO", String)
   Quantity = Column("CANTIDAD DEL LOTE", Integer)
   QuantityD = Column("CANTIDAD DISPONIBLE", Integer)
   Initial_Date = Column("FECHA INICIO", String)
   Final_Date = Column("FECHA FINAL", String)

class SQLAMC(Template, Base):
   __tablename__ = 'ALMACEN DE MULTIFILAMENTO C'

class SQLARM(Template, Base):
   __tablename__ = 'ALMACEN DE REDES MNOFILAMENTO'

class FunctionAP:
   def FindA(NameTable: str, TABLA: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(FunctionAP.WhichTable(NameTable)).all()
      session.close()
      for References in ref:
         if References.Lote == LOTE:
            return (References.CodeB, References.Lote, References.Code, References.Quantity,
                     References.QuantityD, References.Initial_Date, References.Final_Date)

   def FindALLA(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(FunctionAP.WhichTable(NameTable)).all()
      session.close()
      Refs = []
      CodeBr = []
      Lotes = []
      Codes = []
      Quantitys = []
      QuantityDs = []
      InitialDate = []
      FinalDate = []
      for References in ref:
         Refs.append(References.Ref)
         CodeBr.append(References.CodeB)
         Lotes.append(References.Lote)
         Codes.append(References.Code)
         Quantitys.append(References.Quantity)
         QuantityDs.append(References.QuantityD)
         InitialDate.append(References.Initial_Date)
         FinalDate.append(References.Final_Date)
      return (CodeBr, Lotes, Codes, Quantitys, QuantityDs, InitialDate, FinalDate)

   def AddA(NameTable: str, TABLA:str, REF: str, CODEBAR: str, LOTE: str, CODE: str, QUANTITY: int,
            QUANTITYD: str, INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      if NameTable == Settings.Var_AMC(): MP = SQLAMC()
      elif NameTable == Settings.Var_ARM(): MP = SQLARM()
      MP.Ref = REF
      MP.CodeB = CODEBAR
      MP.Lote = LOTE
      MP.Code = CODE
      MP.Quantity = QUANTITY
      MP.QuantityD = QUANTITYD
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      session.add(MP)
      session.commit()
      session.close()

   def DeleteA(NameTable: str, TABLA: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(FunctionAP.WhichTable(NameTable)).filter_by(Lote=LOTE).delete()
      session.commit()
      session.close()

   def DeleteALLA(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(FunctionAP.WhichTable(NameTable)).delete()
      session.commit()
      session.close()

   def UpdateA(NameTable: str, TABLA: str, LOTE: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      Table = FunctionAP.WhichTable(NameTable)
      if DATO_MOD == Settings.Var_Comp1(): session.query(Table).filter_by(Lote=LOTE).update({Table.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp38(): session.query(Table).filter_by(Lote=LOTE).update({Table.Lote: Value})
      elif DATO_MOD == Settings.Var_Comp45(): session.query(Table).filter_by(Lote=LOTE).update({Table.Code: Value})
      elif DATO_MOD == Settings.Var_Comp49(): session.query(Table).filter_by(Lote=LOTE).update({Table.Quantity: Value})
      elif DATO_MOD == Settings.Var_Comp47(): session.query(Table).filter_by(Lote=LOTE).update({Table.QuantityD: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(Table).filter_by(Lote=LOTE).update({Table.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(Table).filter_by(Lote=LOTE).update({Table.Final_Date: Value})
      session.commit()
      session.close()

   def CreateA(NameTable: str, TABLA: str):
      Table = FunctionAP.WhichTable(NameTable)
      engine = create_engine(TABLA, echo=True)
      Table.metadata.create_all(engine)

   def WhichTable(NameTable:str):
      if NameTable == Settings.Var_AMC(): return SQLAMC
      elif NameTable == Settings.Var_ARM(): return SQLARM