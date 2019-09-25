from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLMAQ(Base):
   __tablename__ = 'MAQUINA'
   Id = Column("ID", Integer, primary_key=True)
   Machine = Column("MAQUINA", String)
   State = Column("ESTADO", String)

   def FindMAQ(REFERENCE: str):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      id = session.query(SQLMAQ).all()
      session.close()
      for ID in id:
         if ID.Id == REFERENCE:
            return (ID.Id, ID.Machine, ID.State)

   def FindALLMAQ(REFERENCE: str):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLMAQ).all()
      session.close()
      MAQ=[]
      STATE=[]
      for References in ref:
         MAQ.append(References.Machine)
         STATE.append(References.State)
      return (MAQ, STATE)

   def AddMAQ(MACHINE: str, STATE: str):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      MC = SQLMAQ()
      MC.Machine = MACHINE
      MC.Machine = STATE
      session.add(MC)
      session.commit()
      session.close()

   def DeleteMAQ(MACHINE: str):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMAQ).filter_by(Mechine=MACHINE).delete()
      session.commit()
      session.close()

   def UpdateMAQ(REMISION: str, DATO_MOD: str, Value: str):
      engine = create_engine('sqlite:///lib/CN.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      ValueId, ValueMachine, ValueState = SQLMAQ.FindMAQ(REMISION)
      if DATO_MOD == "MAQUINA":
         session.query(SQLMAQ).filter_by(Machine=ValueMachine).update({SQLMAQ.Machine: Value})
      elif DATO_MOD == "ESTADO":
         session.query(SQLMAQ).filter_by(State=ValueState).update({SQLMAQ.State: Value})
      session.commit()
      session.close()