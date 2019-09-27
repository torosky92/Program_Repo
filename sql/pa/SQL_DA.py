from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class Template(object):
   Id = Column("REF", Integer, primary_key=True)
   CodeB = Column("CODIGO BARRAS", String)
   Worker = Column("OPERADORES", String)
   Lote = Column("LOTE", String)
   Initial_Date = Column("FECHA INICIO", String)
   Final_Date = Column("FECHA FINAL", String)

class SQLAA(Template, Base):
   __tablename__ = 'ALMACEN DE ALMACENAMIENTO'

class SQLAAR(Template, Base):
   __tablename__ = 'ALMACEN DE ALMACENAMIENTO RETIRADO'

class FunctionAA:
   def FindAA(NameTable: str, TABLA: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(FunctionAA.WhichTable(NameTable)).all()
      session.close()
      for References in ref:
         if References.Lote == LOTE:
            return (References.CodeB, References.Worker, References.Lote, References.Initial_Date, References.Final_Date)

   def FindALLAA(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(FunctionAA.WhichTable(NameTable)).all()
      session.close()
      Refs = []
      CodeBr = []
      Workers = []
      Lotes = []
      InitialDate = []
      FinalDate = []
      for References in ref:
         Refs.append(References.Ref)
         CodeBr.append(References.CodeB)
         Lotes.append(References.Lote)
         Workers.append(References.Worker)
         InitialDate.append(References.Initial_Date)
         FinalDate.append(References.Final_Date)
      return (CodeBr, Workers, Lotes, InitialDate, FinalDate)

   def AddAA(NameTable: str, TABLA:str, REF: str, CODEBAR:str, WORKER: str, LOTE: str, INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      if NameTable == Settings.Var_AA(): MP = SQLAA()
      elif NameTable == Settings.Var_AAR(): MP = SQLAAR()
      MP.Ref = REF
      MP.CodeB = CODEBAR
      MP.Worker = WORKER
      MP.Lote = LOTE
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      session.add(MP)
      session.commit()
      session.close()

   def DeleteAA(NameTable: str, TABLA: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(FunctionAA.WhichTable(NameTable)).filter_by(Lote=LOTE).delete()
      session.commit()
      session.close()

   def DeleteALLAA(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(FunctionAA.WhichTable(NameTable)).delete()
      session.commit()
      session.close()

   def UpdateAA(NameTable: str, TABLA: str, LOTE: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      Table = FunctionAA.WhichTable(NameTable)
      if DATO_MOD == Settings.Var_Comp1(): session.query(Table).filter_by(Lote=LOTE).update({Table.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp38(): session.query(Table).filter_by(Lote=LOTE).update({Table.Lote: Value})
      elif DATO_MOD == Settings.Var_Comp15(): session.query(Table).filter_by(Lote=LOTE).update({Table.Worker: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(Table).filter_by(Lote=LOTE).update({Table.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(Table).filter_by(Lote=LOTE).update({Table.Final_Date: Value})
      session.commit()
      session.close()

   def CreateAA(NameTable: str, TABLA: str):
      Table = FunctionAA.WhichTable(NameTable)
      engine = create_engine(TABLA, echo=True)
      Table.metadata.create_all(engine)

   def WhichTable(NameTable:str):
      if NameTable == Settings.Var_AA(): return SQLAA
      elif NameTable == Settings.Var_AAR(): return SQLAAR