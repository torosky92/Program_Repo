from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLPB(Base):
   __tablename__ = 'PEDIDOS DE BOYA'
   Id = Column("REF", Integer, primary_key=True)
   Num_Order = Column("NUMERO DE PEDIDO", String)
   CodeB = Column("CODIGO BARRAS", String)
   Client = Column("CLIENTE", String)
   Quantity = Column("CANTIDAD DE PEDIDO", Integer)
   Available = Column("DISPONIBILIDAD", String)
   Dispatched = Column("DESPACHADO", String)
   Initial_Date = Column("FECHA INICIO", String)
   Final_Date = Column("FECHA FINAL", String)

   def FindPB(TABLA: str, CLIENT: str, N_ORDER: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLPB).all()
      session.close()
      for References in ref:
         if References.Client == CLIENT:
            if References.Num_Order == N_ORDER:
               return (References.Num_Order, References.CodeB, References.Client, References.Quantity, References.Available, References.Dispatche, References.Initial_Date, References.Final_Date)

   def FindALLPB(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLPB).all()
      session.close()
      Refs = []
      N_Order = []
      CodeBr = []
      Clients = []
      Quantitys = []
      Availables = []
      Dispatcheds = []
      InitialDate = []
      FinalDate = []
      for References in ref:
         Refs.append(References.Ref)
         N_Order.append(References.Num_Order)
         CodeBr.append(References.CodeB)
         Clients.append(References.Client)
         Quantitys.append(References.Quantity)
         Availables.append(References.Available)
         Dispatcheds.append(References.Dispatche)
         InitialDate.append(References.Initial_Date)
         FinalDate.append(References.Final_Date)
      return (N_Order, CodeBr, Clients, Quantitys, Availables, Dispatcheds, InitialDate, FinalDate)

   def AddPB(TABLA:str, REF: str, N_ORDER:str, CODEBAR: str, CLIENT: str, QUANTITY: int, AVAILABLE: str, DISPATCHE: str, INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLPB()
      MP.Ref = REF
      MP.Num_Order = N_ORDER
      MP.CodeB = CODEBAR
      MP.Client = CLIENT
      MP.Quantity = QUANTITY
      MP.Available = AVAILABLE
      MP.Dispatched = DISPATCHE
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      session.add(MP)
      session.commit()
      session.close()

   def DeletePB(TABLA: str, CLIENT: str, N_ORDER: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLPB).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).delete()
      session.commit()
      session.close()

   def DeleteALLPB(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLPB).delete()
      session.commit()
      session.close()

   def UpdatePB(TABLA: str, CLIENT: str, N_ORDER: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if DATO_MOD == Settings.Var_Comp35(): session.query(SQLPB).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPB.Num_Order: Value})
      elif DATO_MOD == Settings.Var_Comp1(): session.query(SQLPB).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPB.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp38(): session.query(SQLPB).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPB.Client: Value})
      elif DATO_MOD == Settings.Var_Comp39(): session.query(SQLPB).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPB.Quantity: Value})
      elif DATO_MOD == Settings.Var_Comp40(): session.query(SQLPB).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPB.Available: Value})
      elif DATO_MOD == Settings.Var_Comp41(): session.query(SQLPB).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPB.Dispatched: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(SQLPB).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPB.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(SQLPB).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPB.Final_Date: Value})
      session.commit()
      session.close()

   def CreatePB(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)