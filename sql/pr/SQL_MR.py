from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class Template(object):
   Id = Column("ID", Integer, primary_key=True)
   Ref = Column("REFERENCIA", String)
   CodeC = Column("CODIGO_COLOR", String)
   Worker = Column("OPERADOR", String)
   Machine = Column("MAQUINA", String)
   Initial_Date = Column("FECHA_DE_INICIO", String)
   Final_Date = Column("FECHA_FINAL", String)
   Num_work = Column("NUMERO_DE_PUESTOS", Integer)
   Steamed = Column("VAPORIZADO", String)
   CodeB = Column("CODIGO_DE_BARRAS", String)

class SQLMR(Template, Base):
   __tablename__ = 'MONTAJE_RETORCIDO'

class SQLPR(Template, Base):
   __tablename__ = 'PROCESO_RETORCIDO'

class SQLFunctionTime:
   def FindMR(NameTable: str, TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLFunctionTime.WhichTable(NameTable)).all()
      session.close()
      for References in ref:
         if References.Ref == REFERENCE:
            return (References.Ref, References.CodeC, References.Worker, References.Machine, References.Initial_Date,
                    References.Final_Date, References.Num_work, References.Steamed, References.CodeB)

   def FindALLMR(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLFunctionTime.WhichTable(NameTable)).all()
      session.close()
      Refs = []
      CodeCs = []
      Workers = []
      Machines = []
      InitialD = []
      FinalD = []
      Num_works = []
      Steameds = []
      CodeBr = []
      for References in ref:
         Refs.append(References.Ref)
         CodeCs.append(References.CodeC)
         Workers.append(References.Worker)
         Machines.append(References.Machine)
         InitialD.append(References.Initial_Date)
         FinalD.append(References.Final_Date)
         Num_works.append(References.Num_work)
         Steameds.append(References.Steamed)
         CodeBr.append(References.CodeB)
      return (Refs, CodeCs, Workers, Machines, InitialD, FinalD, Num_works, Steameds, CodeBr)

   def AddMR(NameTable: str, TABLA:str, REF: str, CODEC: str, WORKER: str, MACHINE: str, INITIAL_DATE: str, FINAL_DATE: str,
                NUM_WORK: int, STEAMED: str, CODEB: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      if NameTable == Settings.Var_PR():
         MP = SQLPR()
      elif NameTable == Settings.Var_MR():
         MP = SQLMR()
      MP.Ref = REF
      MP.CodeC = CODEC
      MP.Worker = WORKER
      MP.Machine = MACHINE
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      MP.Num_work = NUM_WORK
      MP.Steamed = STEAMED
      MP.CodeB = CODEB
      session.add(MP)
      session.commit()
      session.close()

   def DeleteMR(NameTable: str, TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLFunctionTime.WhichTable(NameTable)).filter_by(Ref=REFERENCE).delete()
      session.commit()
      session.close()

   def DeleteALLMR(NameTable:str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLFunctionTime.WhichTable(NameTable)).delete()
      session.commit()
      session.close()

   def UpdateMR(NameTable: str, TABLA: str, REMISION: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      Table = SQLFunctionTime.WhichTable(NameTable)
      valueRef, ValueCodeC, ValueWorker, ValueMachine, ValueInDate, ValueOutDate, ValueNum_W, ValueSteamed, ValueCodeB = SQLMR.FindMR(NameTable, TABLA, REMISION)
      if DATO_MOD == Settings.Var_Comp13(): session.query(Table).filter_by(Ref=valueRef).update({Table.Ref: Value})
      elif DATO_MOD == Settings.Var_Comp22(): session.query(Table).filter_by(CodeC=ValueCodeC).update({Table.CodeC: Value})
      elif DATO_MOD == Settings.Var_Comp14(): session.query(Table).filter_by(Worker=ValueWorker).update({Table.Worker: Value})
      elif DATO_MOD == Settings.Var_Comp10(): session.query(Table).filter_by(Machine=ValueMachine).update({Table.Machine: Value})
      elif DATO_MOD == Settings.Var_Comp1(): session.query(Table).filter_by(CodeB=ValueCodeB).update({Table.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(Table).filter_by(Initial_Date=ValueInDate).update({Table.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(Table).filter_by(Final_Date=ValueOutDate).update({Table.Final_Date: Value})
      elif DATO_MOD == Settings.Var_Comp34(): session.query(Table).filter_by(Num_work=ValueNum_W).update({Table.Num_work: Value})
      elif DATO_MOD == Settings.Var_Comp16(): session.query(Table).filter_by(Steamed=ValueSteamed).update({Table.Steamed: Value})
      session.commit()
      session.close()

   def CreateMR(NameTable: str, TABLA: str):
      Table = SQLFunctionTime.WhichTable(NameTable)
      engine = create_engine(TABLA, echo=True)
      Table.metadata.create_all(bind=engine)

   def WhichTable(NameTable: str):
      if NameTable == Settings.Var_PR(): return SQLPR
      elif NameTable == Settings.Var_MR(): return SQLMR