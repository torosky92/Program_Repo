from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLPM(Base):
   __tablename__ = 'PEDIDOS DE MULTIFILAMENTO'
   Id = Column("REF", Integer, primary_key=True)
   Num_Order = Column("NUMERO DE PEDIDO", String)
   CodeB = Column("CODIGO BARRAS", String)
   Client = Column("CLIENTE", String)
   Material = Column("MATERIAL", String)
   Diameter = Column("DIAMETRO", String)
   Presentation = Column("PRESENTACION", String)
   Num_Meshes = Column("NUMERO DE MALLAS", Integer)
   Quantity = Column("CANTIDAD DE PEDIDO", Integer)
   Available = Column("DISPONIBILIDAD", String)
   Dispatched = Column("DESPACHADO", String)
   Initial_Date = Column("FECHA INICIO", String)
   Final_Date = Column("FECHA FINAL", String)

   def FindPM(TABLA: str, CLIENT: str, N_ORDER: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLPM).all()
      session.close()
      for References in ref:
         if References.Client == CLIENT:
            if References.Num_Order == N_ORDER:
               return (References.Num_Order, References.CodeB, References.Client, References.Material,
                       References.Diameter, References.Presentation, References.Num_Meshes, References.Quantity,
                       References.Available, References.Dispatche, References.Initial_Date, References.Final_Date)

   def FindALLPM(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLPM).all()
      session.close()
      Refs = []
      N_Order = []
      CodeBr = []
      Clients = []
      Materials = []
      Diameters = []
      Presentations = []
      NumMeshes = []
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
         Diameters.append(References.Diameter)
         Presentations.append(References.Presentation)
         NumMeshes.append(References.Num_Meshes)
         Quantitys.append(References.Quantity)
         Availables.append(References.Available)
         Dispatcheds.append(References.Dispatche)
         InitialDate.append(References.Initial_Date)
         FinalDate.append(References.Final_Date)
      return (N_Order, CodeBr, Clients, Materials, Diameters, Presentations, NumMeshes, Quantitys, Availables,
              Dispatcheds, InitialDate, FinalDate)

   def AddPM(TABLA:str, REF: str, N_ORDER:str, CODEBAR: str, CLIENT: str, MATERIAL: str, DIAMETER: str, PRESENTATION: str, N_MESHES: str, QUANTITY: int, AVAILABLE: str, DISPATCHE: str, INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLPM()
      MP.Ref = REF
      MP.Num_Order = N_ORDER
      MP.CodeB = CODEBAR
      MP.Client = CLIENT
      MP.Material = MATERIAL
      MP.Diameter = DIAMETER
      MP.Presentation = PRESENTATION
      MP.Num_Meshes = N_MESHES
      MP.Quantity = QUANTITY
      MP.Available = AVAILABLE
      MP.Dispatched = DISPATCHE
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      session.add(MP)
      session.commit()
      session.close()

   def DeletePM(TABLA: str, CLIENT: str, N_ORDER: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLPM).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).delete()
      session.commit()
      session.close()

   def DeleteALLPM(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLPM).delete()
      session.commit()
      session.close()

   def UpdatePM(TABLA: str, CLIENT: str, N_ORDER: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if DATO_MOD == Settings.Var_Comp35(): session.query(SQLPM).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPM.Num_Order: Value})
      elif DATO_MOD == Settings.Var_Comp1(): session.query(SQLPM).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPM.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp38(): session.query(SQLPM).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPM.Client: Value})
      elif DATO_MOD == Settings.Var_Comp42(): session.query(SQLPM).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPM.Material: Value})
      elif DATO_MOD == Settings.Var_Comp43(): session.query(SQLPM).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPM.Diameter: Value})
      elif DATO_MOD == Settings.Var_Comp12(): session.query(SQLPM).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPM.Presentation: Value})
      elif DATO_MOD == Settings.Var_Comp44(): session.query(SQLPM).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPM.Num_Meshes: Value})
      elif DATO_MOD == Settings.Var_Comp39(): session.query(SQLPM).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPM.Quantity: Value})
      elif DATO_MOD == Settings.Var_Comp40(): session.query(SQLPM).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPM.Available: Value})
      elif DATO_MOD == Settings.Var_Comp41(): session.query(SQLPM).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPM.Dispatched: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(SQLPM).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPM.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(SQLPM).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLPM.Final_Date: Value})
      session.commit()
      session.close()

   def CreatePM(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)