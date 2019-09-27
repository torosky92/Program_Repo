from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLMAQ(Base):
   __tablename__ = 'MAQUNAS'
   Id = Column("ID", Integer, primary_key=True)
   Machine = Column("MAQUINA", String)
   State = Column("ESTADO", String)

   def FindMAQ(TABLA: str, MACHINE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      id = session.query(SQLMAQ).all()
      session.close()
      for ID in id:
         if ID.Machine == MACHINE: return (ID.Machine, ID.State)

   def FindALLMAQ(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLMAQ).all()
      session.close()
      MAQ = []
      STATE = []
      for References in ref:
         MAQ.append(References.Machine)
         STATE.append(References.State)
      return (MAQ, STATE)

   def AddMAQ(TABLA: str, MACHINE: str, STATES: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MC = SQLMAQ()
      MC.Machine = MACHINE
      MC.State = STATES
      session.add(MC)
      session.commit()
      session.close()

   def DeleteMAQ(TABLA: str, MACHINE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMAQ).filter_by(Machine=MACHINE).delete()
      session.commit()
      session.close()

   def DeleteALLMAQ(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMAQ).delete()
      session.commit()
      session.close()

   def UpdateMAQ(TABLA: str, REMISION: str, DATO_MOD: str, Value: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      ValueMachine, ValueState = SQLMAQ.FindMAQ(TABLA, REMISION)
      if DATO_MOD == Settings.Var_Comp10(): session.query(SQLMAQ).filter_by(Machine=ValueMachine).update({SQLMAQ.Machine: Value})
      elif DATO_MOD == Settings.Var_Comp11(): session.query(SQLMAQ).filter_by(State=ValueState).update({SQLMAQ.State: Value})
      session.commit()
      session.close()

   def CreateMAQ(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)