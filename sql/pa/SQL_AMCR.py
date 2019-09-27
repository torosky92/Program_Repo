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
   Quantity = Column("CANTIDAD RETIRADO", Integer)
   Initial_Date = Column("FECHA INICIO", String)
   Final_Date = Column("FECHA FINAL", String)

class SQLAMCR(Template, Base):
   __tablename__ = 'ALMACEN DE MULTIFILAMENTO C RETIRADO'

class SQLARMR(Template, Base):
   __tablename__ = 'ALMACEN DE REDES MNOFILAMENTO RETIRADO'

class FunctionAPR:
   def FindAR(NameTable: str, TABLA: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(FunctionAPR.WhichTable(NameTable)).all()
      session.close()
      for References in ref:
         if References.Lote == LOTE:
            return (References.CodeB, References.Lote, References.Code, References.Quantity,
                     References.Initial_Date, References.Final_Date)

   def FindALLAR(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(FunctionAPR.WhichTable(NameTable)).all()
      session.close()
      Refs = []
      CodeBr = []
      Lotes = []
      Codes = []
      Quantitys = []
      InitialDate = []
      FinalDate = []
      for References in ref:
         Refs.append(References.Ref)
         CodeBr.append(References.CodeB)
         Lotes.append(References.Lote)
         Codes.append(References.Code)
         Quantitys.append(References.Quantity)
         InitialDate.append(References.Initial_Date)
         FinalDate.append(References.Final_Date)
      return (CodeBr, Lotes, Codes, Quantitys, InitialDate, FinalDate)

   def AddAR(NameTable: str, TABLA:str, REF: str, CODEBAR: str, LOTE: str, CODE: str, QUANTITY: int,
            INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      if NameTable == Settings.Var_AMC(): MP = SQLAMCR()
      elif NameTable == Settings.Var_ARM(): MP = SQLARMR()
      MP.Ref = REF
      MP.CodeB = CODEBAR
      MP.Lote = LOTE
      MP.Code = CODE
      MP.Quantity = QUANTITY
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      session.add(MP)
      session.commit()
      session.close()

   def DeleteAR(NameTable: str, TABLA: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(FunctionAPR.WhichTable(NameTable)).filter_by(Lote=LOTE).delete()
      session.commit()
      session.close()

   def DeleteALLAR(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(FunctionAPR.WhichTable(NameTable)).delete()
      session.commit()
      session.close()

   def UpdateAR(NameTable: str, TABLA: str, LOTE: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      Table = FunctionAPR.WhichTable(NameTable)
      if DATO_MOD == Settings.Var_Comp1(): session.query(Table).filter_by(Lote=LOTE).update({Table.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp38(): session.query(Table).filter_by(Lote=LOTE).update({Table.Lote: Value})
      elif DATO_MOD == Settings.Var_Comp45(): session.query(Table).filter_by(Lote=LOTE).update({Table.Code: Value})
      elif DATO_MOD == Settings.Var_Comp48(): session.query(Table).filter_by(Lote=LOTE).update({Table.Quantity: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(Table).filter_by(Lote=LOTE).update({Table.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(Table).filter_by(Lote=LOTE).update({Table.Final_Date: Value})
      session.commit()
      session.close()

   def CreateAR(NameTable: str, TABLA: str):
      Table = FunctionAPR.WhichTable(NameTable)
      engine = create_engine(TABLA, echo=True)
      Table.metadata.create_all(engine)

   def WhichTable(NameTable:str):
      if NameTable == Settings.Var_AMC(): return SQLAMCR
      elif NameTable == Settings.Var_ARM(): return SQLARMR