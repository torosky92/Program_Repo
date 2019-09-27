from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLIN(Base):
   __tablename__ = 'PROCESO DE INGRESO'
   Id = Column("REF", Integer, primary_key=True)
   Num_Order = Column("NUMERO DE PEDIDO", String)
   CodeB = Column("CODIGO BARRAS", String)
   Client = Column("CLIENTE", String)
   TypeP = Column("TIPO DE PRESENTACION", String)
   Code = Column("CODIGO", String)
   Material = Column("MATERIAL", String)
   Diameter = Column("DIAMETRO", String)
   Presentation = Column("PRESENTACION", String)
   Num_Meshes = Column("NUMERO DE MALLAS", Integer)
   Quantity = Column("CANTIDAD DE PEDIDO", Integer)
   Available = Column("DISPONIBILIDAD", String)
   Dispatched = Column("DESPACHADO", String)
   Initial_Date = Column("FECHA INICIO", String)
   Final_Date = Column("FECHA FINAL", String)

   def FindIN(TABLA: str, CLIENT: str, N_ORDER: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLIN).all()
      session.close()
      for References in ref:
         if References.Client == CLIENT:
            if References.Num_Order == N_ORDER:
               return (References.Num_Order, References.CodeB, References.Client, References.TypeP, References.Code, References.Material,
                       References.Diameter, References.Presentation, References.Num_Meshes, References.Quantity,
                       References.Available, References.Dispatche, References.Initial_Date, References.Final_Date)

   def FindALLPIN(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLIN).all()
      session.close()
      Refs = []
      N_Order = []
      CodeBr = []
      Clients = []
      TypePs = []
      Codes = []
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
         TypePs.append(References.TypeP)
         Codes.append(References.Code)
         Materials.append(References.Material)
         Diameters.append(References.Diameter)
         Presentations.append(References.Presentation)
         NumMeshes.append(References.Num_Meshes)
         Quantitys.append(References.Quantity)
         Availables.append(References.Available)
         Dispatcheds.append(References.Dispatche)
         InitialDate.append(References.Initial_Date)
         FinalDate.append(References.Final_Date)
      return (N_Order, CodeBr, Clients, TypePs, Codes, Materials, Diameters, Presentations, NumMeshes,
              Quantitys, Availables, Dispatcheds, InitialDate, FinalDate)

   def AddPIN(TABLA:str, REF: str, N_ORDER:str, CODEBAR: str, CLIENT: str, TYPEPRESENTATION: str, CODE:str,
              MATERIAL: str, DIAMETER: str, PRESENTATION: str, N_MESHES: str, QUANTITY: int, AVAILABLE: str,
              DISPATCHE: str, INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLIN()
      MP.Ref = REF
      MP.Num_Order = N_ORDER
      MP.CodeB = CODEBAR
      MP.Client = CLIENT
      MP.TypeP = TYPEPRESENTATION
      MP.Code = CODE
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

   def DeleteIN(TABLA: str, CLIENT: str, N_ORDER: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLIN).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).delete()
      session.commit()
      session.close()

   def DeleteALLIN(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLIN).delete()
      session.commit()
      session.close()

   def UpdateIN(TABLA: str, CLIENT: str, N_ORDER: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if DATO_MOD == Settings.Var_Comp35(): session.query(SQLIN).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLIN.Num_Order: Value})
      elif DATO_MOD == Settings.Var_Comp1(): session.query(SQLIN).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLIN.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp38(): session.query(SQLIN).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLIN.Client: Value})
      elif DATO_MOD == Settings.Var_Comp46(): session.query(SQLIN).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLIN.TypeP: Value})
      elif DATO_MOD == Settings.Var_Comp45(): session.query(SQLIN).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLIN.Code: Value})
      elif DATO_MOD == Settings.Var_Comp42(): session.query(SQLIN).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLIN.Material: Value})
      elif DATO_MOD == Settings.Var_Comp43(): session.query(SQLIN).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLIN.Diameter: Value})
      elif DATO_MOD == Settings.Var_Comp12(): session.query(SQLIN).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLIN.Presentation: Value})
      elif DATO_MOD == Settings.Var_Comp44(): session.query(SQLIN).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLIN.Num_Meshes: Value})
      elif DATO_MOD == Settings.Var_Comp39(): session.query(SQLIN).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLIN.Quantity: Value})
      elif DATO_MOD == Settings.Var_Comp40(): session.query(SQLIN).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLIN.Available: Value})
      elif DATO_MOD == Settings.Var_Comp41(): session.query(SQLIN).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLIN.Dispatched: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(SQLIN).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLIN.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(SQLIN).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({SQLIN.Final_Date: Value})
      session.commit()
      session.close()

   def CreateIN(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)