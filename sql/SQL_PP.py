from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLPP(Base):
   __tablename__ = 'PARADO_DE_PROCESO'
   Id = Column("ID", Integer, primary_key=True)
   Ref = Column("REFERENCIA", String)
   CodeC = Column("CODIGO_COLOR", String)
   Worker = Column("OPERADOR", String)
   Machine = Column("MAQUINA", String)
   Reason = Column("RAZON_DE_PARO", String)
   Initial_Date = Column("FECHA_DE_INICIO", String)
   Final_Date = Column("FECHA_FINAL", String)

   def FindPP(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLPP).all()
      session.close()
      for References in ref:
         if References.Ref == REFERENCE:
            return (References.Ref, References.CodeC, References.Worker, References.Machine,
                    References.Reason, References.Initial_Date, References.Final_Date)

   def FindALLPP(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLPP).all()
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

   def AddPP(TABLA:str, REF: str, CODEC: str, WORKER: str, MACHINE: str, REASON: str,
             INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLPP()
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

   def DeletePP(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLPP).filter_by(Ref=REFERENCE).delete()
      session.commit()
      session.close()

   def DeleteALLPP(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLPP).delete()
      session.commit()
      session.close()

   def UpdatePP(TABLA: str, REMISION: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      valueRef, ValueCodeC, ValueWorker, ValueMachine, ValueReason, ValueInDate, ValueOutDate = SQLPP.FindPP(TABLA, REMISION)
      if DATO_MOD == "REFERENCIA":
         session.query(SQLPP).filter_by(Ref=valueRef).update({SQLPP.Ref: Value})
      elif DATO_MOD == "CODIGO DE COLORES":
         session.query(SQLPP).filter_by(CodeC=ValueCodeC).update({SQLPP.CodeC: Value})
      elif DATO_MOD == "OPERADOR":
         session.query(SQLPP).filter_by(Worker=ValueWorker).update({SQLPP.Worker: Value})
      elif DATO_MOD == "MAQUINA":
         session.query(SQLPP).filter_by(Machine=ValueMachine).update({SQLPP.Machine: Value})
      elif DATO_MOD == "FECHA DE INICIO":
         session.query(SQLPP).filter_by(Initial_Date=ValueInDate).update({SQLPP.Initial_Date: Value})
      elif DATO_MOD == "FECHA FINAL":
         session.query(SQLPP).filter_by(Final_Date=ValueOutDate).update({SQLPP.Final_Date: Value})
      elif DATO_MOD == "RAZON DE PARO":
         session.query(SQLPP).filter_by(Reason=ValueReason).update({SQLPP.Reason: Value})
      session.commit()
      session.close()