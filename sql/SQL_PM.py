from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLPM(Base):
   __tablename__ = 'PARADO_EN_MONTAJE'
   Id = Column("ID", Integer, primary_key=True)
   Ref = Column("REFERENCIA", String)
   CodeC = Column("CODIGO_COLOR", String)
   Worker = Column("OPERADOR", String)
   Machine = Column("MAQUINA", String)
   Reason = Column("RAZON_DE_PARO", String)
   Initial_Date = Column("FECHA_DE_INICIO", String)
   Final_Date = Column("FECHA_FINAL", String)

   def FindPM(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLPM).all()
      session.close()
      for References in ref:
         if References.Ref == REFERENCE:
            return (References.Ref, References.CodeC, References.Worker, References.Machine,
                    References.Reason, References.Initial_Date, References.Final_Date)

   def FindALLPM(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLPM).all()
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

   def AddPM(TABLA:str, REF: str, CODEC: str, WORKER: str, MACHINE: str, REASON: str,
             INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
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

   def DeletePM(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLPM).filter_by(Ref=REFERENCE).delete()
      session.commit()
      session.close()

   def DeleteALLPM(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLPM).delete()
      session.commit()
      session.close()

   def UpdatePM(TABLA: str, REMISION: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      valueRef, ValueCodeC, ValueWorker, ValueMachine, ValueReason, ValueInDate, ValueOutDate = SQLPM.FindPM(TABLA, REMISION)
      if DATO_MOD == "REFERENCIA":
         session.query(SQLPM).filter_by(Ref=valueRef).update({SQLPM.Ref: Value})
      elif DATO_MOD == "CODIGO DE COLORES":
         session.query(SQLPM).filter_by(CodeC=ValueCodeC).update({SQLPM.CodeC: Value})
      elif DATO_MOD == "OPERADOR":
         session.query(SQLPM).filter_by(Worker=ValueWorker).update({SQLPM.Worker: Value})
      elif DATO_MOD == "MAQUINA":
         session.query(SQLPM).filter_by(Machine=ValueMachine).update({SQLPM.Machine: Value})
      elif DATO_MOD == "FECHA DE INICIO":
         session.query(SQLPM).filter_by(Initial_Date=ValueInDate).update({SQLPM.Initial_Date: Value})
      elif DATO_MOD == "FECHA FINAL":
         session.query(SQLPM).filter_by(Final_Date=ValueOutDate).update({SQLPM.Final_Date: Value})
      elif DATO_MOD == "RAZON DE PARO":
         session.query(SQLPM).filter_by(Reason=ValueReason).update({SQLPM.Reason: Value})
      session.commit()
      session.close()