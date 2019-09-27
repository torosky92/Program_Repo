from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLPIO(Base):
   __tablename__ = 'PEDIDOS DE PIOLA'
   Id = Column("REF", Integer, primary_key=True)
   Num_Order = Column("NUMERO DE PEDIDO", String)
   CodeB = Column("CODIGO BARRAS", String)
   Client = Column("CLIENTE", String)
   Material = Column("MATERIAL", String)
   Presentation = Column("PRESENTACION", String)
   Quantity = Column("CANTIDAD DE PEDIDO", Integer)
   Available = Column("DISPONIBILIDAD", String)
   Dispatched = Column("DESPACHADO", String)
   Initial_Date = Column("FECHA INICIO", String)
   Final_Date = Column("FECHA FINAL", String)

   def FindPIO(TABLA: str, CLIENT: str, N_ORDER: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLPIO).all()
      session.close()
      for References in ref:
         if References.Client == CLIENT:
            if References.Num_Order == N_ORDER:
               return (References.Num_Order, References.CodeB, References.Client, References.Material,
                       References.Presentation, References.Quantity, References.Available, References.Dispatche,
                       References.Initial_Date, References.Final_Date)

   def FindALLPIO(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLPIO).all()
      session.close()
      Refs = []
      N_Order = []
      CodeBr = []
      Clients = []
      Materials = []
      Presentations = []
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
         Materials.append(References.Material)
         Presentations.append(References.Presentation)
         Quantitys.append(References.Quantity)
         Availables.append(References.Available)
         Dispatcheds.append(References.Dispatche)
         InitialDate.append(References.Initial_Date)
         FinalDate.append(References.Final_Date)
      return (N_Order, CodeBr, Clients, Materials, Presentations, Quantitys, Availables,
              Dispatcheds, InitialDate, FinalDate)

   def AddPIO(TABLA:str, REF: str, N_ORDER:str, CODEBAR: str, CLIENT: str, MATERIAL: str, PRESENTATION: str, QUANTITY: int, AVAILABLE: str, DISPATCHE: str, INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLPIO()
      MP.Ref = REF
      MP.Num_Order = N_ORDER
      MP.CodeB = CODEBAR
      MP.Client = CLIENT
      MP.Material = MATERIAL
      MP.Presentation = PRESENTATION
      MP.Quantity = QUANTITY
      MP.Available = AVAILABLE
      MP.Dispatched = DISPATCHE
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      session.add(MP)
      session.commit()
      session.close()

   def DeletePIO(TABLA: str, CLIENT: str, N_ORDER: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLPIO).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).delete()
      session.commit()
      session.close()

   def DeleteALLPIO(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLPIO).delete()
      session.commit()
      session.close()

   def UpdatePIO(TABLA: str, CLIENT: str, N_ORDER: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if DATO_MOD == Settings.Var_Comp35(): session.query(SQLPIO).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPIO.Num_Order: Value})
      elif DATO_MOD == Settings.Var_Comp1(): session.query(SQLPIO).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPIO.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp38(): session.query(SQLPIO).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPIO.Client: Value})
      elif DATO_MOD == Settings.Var_Comp42(): session.query(SQLPIO).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPIO.Material: Value})
      elif DATO_MOD == Settings.Var_Comp12(): session.query(SQLPIO).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPIO.Presentation: Value})
      elif DATO_MOD == Settings.Var_Comp39(): session.query(SQLPIO).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPIO.Quantity: Value})
      elif DATO_MOD == Settings.Var_Comp40(): session.query(SQLPIO).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPIO.Available: Value})
      elif DATO_MOD == Settings.Var_Comp41(): session.query(SQLPIO).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPIO.Dispatched: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(SQLPIO).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPIO.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(SQLPIO).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPIO.Final_Date: Value})
      session.commit()
      session.close()

   def CreatePIO(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)