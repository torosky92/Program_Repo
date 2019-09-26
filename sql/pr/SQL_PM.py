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
   Reason = Column("RAZON_DE_PARO", String)
   Initial_Date = Column("FECHA_DE_INICIO", String)
   Final_Date = Column("FECHA_FINAL", String)

class SQLPM(Template, Base):
   __tablename__ = 'PARO_EN_MONTAJE'

class SQLPP(Template, Base):
   __tablename__ = 'PARO_DE_PROCESO'

class SQLFunctionPP:
   def FindPM(NameTable: str, TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLFunctionPP.WhichTable(NameTable)).all()
      session.close()
      for References in ref:
         if References.Ref == REFERENCE:
            return (References.Ref, References.CodeC, References.Worker, References.Machine,
                    References.Reason, References.Initial_Date, References.Final_Date)

   def FindALLPM(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLFunctionPP.WhichTable(NameTable)).all()
      session.close()
      Refs = []
      CodeCs = []
      Workers = []
      Machines = []
      Reasons = []
      InitialD = []
      FinalD = []
      for References in ref:
         Refs.append(References.Ref)
         CodeCs.append(References.CodeC)
         Workers.append(References.Worker)
         Machines.append(References.Machine)
         Reasons.append(References.Reason)
         InitialD.append(References.Initial_Date)
         FinalD.append(References.Final_Date)
      return (Refs, CodeCs, Workers, Machines, Reasons, InitialD, FinalD)

   def AddPM(NameTable: str, TABLA:str, REF: str, CODEC: str, WORKER: str, MACHINE: str, REASON: str,
             INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      if NameTable == Settings.Var_PP():
         MP = SQLPP()
      elif NameTable == Settings.Var_PM():
         MP = SQLPM()
      MP.Ref = REF
      MP.CodeC = CODEC
      MP.Worker = WORKER
      MP.Machine = MACHINE
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      MP.Reason = REASON
      session.add(MP)
      session.commit()
      session.close()

   def DeletePM(NameTable: str, TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLFunctionPP.WhichTable(NameTable)).filter_by(Ref=REFERENCE).delete()
      session.commit()
      session.close()

   def DeleteALLPM(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLFunctionPP.WhichTable(NameTable)).delete()
      session.commit()
      session.close()

   def UpdatePM(NameTable: str, TABLA: str, REMISION: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      Table = SQLFunctionPP.WhichTable(NameTable)
      valueRef, ValueCodeC, ValueWorker, ValueMachine, ValueReason, ValueInDate, ValueOutDate = SQLFunctionPP.FindPM(NameTable, TABLA, REMISION)
      if DATO_MOD == Settings.Var_Comp13(): session.query(Table).filter_by(Ref=valueRef).update({Table.Ref: Value})
      elif DATO_MOD == Settings.Var_Comp22(): session.query(Table).filter_by(CodeC=ValueCodeC).update({Table.CodeC: Value})
      elif DATO_MOD == Settings.Var_Comp15(): session.query(Table).filter_by(Worker=ValueWorker).update({Table.Worker: Value})
      elif DATO_MOD == Settings.Var_Comp10(): session.query(Table).filter_by(Machine=ValueMachine).update({Table.Machine: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(Table).filter_by(Initial_Date=ValueInDate).update({Table.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(Table).filter_by(Final_Date=ValueOutDate).update({Table.Final_Date: Value})
      elif DATO_MOD == Settings.Var_Comp33(): session.query(Table).filter_by(Reason=ValueReason).update({Table.Reason: Value})
      session.commit()
      session.close()

   def CreatePM(NameTable: str, TABLA: str):
      Table = SQLFunctionPP.WhichTable(NameTable)
      engine = create_engine(TABLA, echo=True)
      Table.metadata.create_all(bind=engine)

   def WhichTable(NameTable: str):
      if NameTable == Settings.Var_PP(): return SQLPP
      elif NameTable == Settings.Var_PM(): return SQLPM