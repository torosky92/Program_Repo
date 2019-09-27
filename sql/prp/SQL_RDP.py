from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLRDP(Base):
   __tablename__ = 'DATOS DEL PEDIDOS'
   Id = Column("REF", Integer, primary_key=True)
   Num_Order = Column("NUMERO DE PEDIDO", String)
   Worker = Column("OPERADOR", String)
   Client = Column("CLIENTE", String)
   Phone = Column("NUMERO TELEFONO", String)
   Num_Items = Column("NUMERO DE ITEMS", Integer)
   CodeB = Column("CODIGO BARRAS", String)
   Initial_Date = Column("FECHA INICIO", String)
   Final_Date = Column("FECHA FINAL", String)

   def FindRDP(TABLA: str, CLIENT: str, NUM_ORDER: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLRDP).all()
      session.close()
      for References in ref:
         if References.Client == CLIENT:
            if References.Num_Order == NUM_ORDER:
               return (References.Num_Order, References.Worker, References.Client, References.Phone, References.Num_Items, References.CodeB, References.Initial_Date, References.Final_Date)

   def FindALLRDP(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLRDP).all()
      session.close()
      Refs = []
      N_Order = []
      Workers = []
      Clients = []
      Phones = []
      NumItems = []
      CodeBr = []
      InitialDate = []
      FinalDate = []
      for References in ref:
         Refs.append(References.Ref)
         N_Order.append(References.Num_Order)
         Workers.append(References.Worker)
         Clients.append(References.Client)
         Phones.append(References.Phone)
         NumItems.append(References.Num_Items)
         CodeBr.append(References.CodeB)
         InitialDate.append(References.Initial_Date)
         FinalDate.append(References.Final_Date)
      return (N_Order, Workers, Clients, Phones, NumItems, CodeBr, InitialDate, FinalDate)

   def AddRDP(TABLA:str, REF: str, N_ORDER:str, WORKER: str, CLIENT: str, PHONE: str, NUM_ITEMS: str, CODEBAR: str, INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLRDP()
      MP.Ref = REF
      MP.Num_Order = N_ORDER
      MP.Worker = WORKER
      MP.Client = CLIENT
      MP.Phone = PHONE
      MP.Num_Items = NUM_ITEMS
      MP.CodeB = CODEBAR
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      session.add(MP)
      session.commit()
      session.close()

   def DeleteRDP(TABLA: str, CLIENT: str, N_ORDER: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLRDP).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).delete()
      session.commit()
      session.close()

   def DeleteALLRDP(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLRDP).delete()
      session.commit()
      session.close()

   def UpdateRDP(TABLA: str, CLIENT: str, N_ORDER: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if DATO_MOD == Settings.Var_Comp35(): session.query(SQLRDP).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLRDP.Num_Order: Value})
      elif DATO_MOD == Settings.Var_Comp15(): session.query(SQLRDP).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLRDP.Worker: Value})
      elif DATO_MOD == Settings.Var_Comp38(): session.query(SQLRDP).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLRDP.Client: Value})
      elif DATO_MOD == Settings.Var_Comp37(): session.query(SQLRDP).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLRDP.Phone: Value})
      elif DATO_MOD == Settings.Var_Comp36(): session.query(SQLRDP).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLRDP.Num_Items: Value})
      elif DATO_MOD == Settings.Var_Comp1(): session.query(SQLRDP).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLRDP.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(SQLRDP).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLRDP.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(SQLRDP).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLRDP.Final_Date: Value})
      session.commit()
      session.close()

   def CreateRDP(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)