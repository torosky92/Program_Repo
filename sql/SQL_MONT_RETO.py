from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLMONTRETO(Base):
   __tablename__ = 'MONTAJE_RETORCIDO'
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

   def FindMONTRETO(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLMONTRETO).all()
      session.close()
      for References in ref:
         if References.Ref == REFERENCE:
            return (References.Ref, References.CodeC, References.Worker, References.Machine, References.Initial_Date,
                    References.Final_Date, References.Num_work, References.Steamed, References.CodeB)

   def FindALLMONTRETO(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLMONTRETO).all()
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

   def AddMONTRETO(TABLA:str, REF: str, CODEC: str, WORKER: str, MACHINE: str, INITIAL_DATE: str, FINAL_DATE: str,
                NUM_WORK: int, STEAMED: str, CODEB: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLMONTRETO()
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

   def DeleteMONTRETO(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMONTRETO).filter_by(Ref=REFERENCE).delete()
      session.commit()
      session.close()

   def DeleteALLMONTRETO(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMONTRETO).delete()
      session.commit()
      session.close()

   def UpdateMONTRETO(TABLA: str, REMISION: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      valueRef, ValueCodeC, ValueWorker, ValueMachine, ValueInDate, ValueOutDate, ValueNum_W, ValueSteamed, ValueCodeB = SQLMONTRETO.FindMONTRETO(TABLA, REMISION)
      if DATO_MOD == "REFERENCIA":
         session.query(SQLMONTRETO).filter_by(Ref=valueRef).update({SQLMONTRETO.Ref: Value})
      elif DATO_MOD == "CODIGO DE COLORES":
         session.query(SQLMONTRETO).filter_by(CodeC=ValueCodeC).update({SQLMONTRETO.CodeC: Value})
      elif DATO_MOD == "OPERADOR":
         session.query(SQLMONTRETO).filter_by(Worker=ValueWorker).update({SQLMONTRETO.Worker: Value})
      elif DATO_MOD == "MAQUINA":
         session.query(SQLMONTRETO).filter_by(Machine=ValueMachine).update({SQLMONTRETO.Machine: Value})
      elif DATO_MOD == "CODIGO DE BARRAS":
         session.query(SQLMONTRETO).filter_by(CodeB=ValueCodeB).update({SQLMONTRETO.CodeB: Value})
      elif DATO_MOD == "FECHA DE INICIO":
         session.query(SQLMONTRETO).filter_by(Initial_Date=ValueInDate).update({SQLMONTRETO.Initial_Date: Value})
      elif DATO_MOD == "FECHA FINAL":
         session.query(SQLMONTRETO).filter_by(Final_Date=ValueOutDate).update({SQLMONTRETO.Final_Date: Value})
      elif DATO_MOD == "NUMERO DE PUESTOS":
         session.query(SQLMONTRETO).filter_by(Num_work=ValueNum_W).update({SQLMONTRETO.Num_work: Value})
      elif DATO_MOD == "VAPORIZADO":
         session.query(SQLMONTRETO).filter_by(Steamed=ValueSteamed).update({SQLMONTRETO.Steamed: Value})
      session.commit()
      session.close()