from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class Template(object):
   Id = Column("REF", Integer, primary_key=True)
   Num_Order = Column("NUMERO DE PEDIDO", String)
   CodeB = Column("CODIGO BARRAS", String)
   Client = Column("CLIENTE", String)
   Code = Column("CODIGO", String)
   Quantity = Column("CANTIDAD DE PEDIDO", Integer)
   Available = Column("DISPONIBILIDAD", String)
   Dispatched = Column("DESPACHADO", String)
   Initial_Date = Column("FECHA INICIO", String)
   Final_Date = Column("FECHA FINAL", String)

class SQLPMC(Template, Base):
   __tablename__ = 'PEDIDOS DE MULTIFILAMENTO C'

class SQLRM(Template, Base):
   __tablename__ = 'PEDIDOS DE REDES MNOFILAMENTO'

class FunctionPR:
   def FindPMC(NameTable: str, TABLA: str, CLIENT: str, N_ORDER: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(FunctionPR.WhichTable(NameTable)).all()
      session.close()
      for References in ref:
         if References.Client == CLIENT:
            if References.Num_Order == N_ORDER:
               return (References.Num_Order, References.CodeB, References.Client, References.Code, References.Quantity,
                       References.Available, References.Dispatche, References.Initial_Date, References.Final_Date)

   def FindALLPMC(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(FunctionPR.WhichTable(NameTable)).all()
      session.close()
      Refs = []
      N_Order = []
      CodeBr = []
      Clients = []
      Codes = []
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
         Codes.append(References.Code)
         Quantitys.append(References.Quantity)
         Availables.append(References.Available)
         Dispatcheds.append(References.Dispatche)
         InitialDate.append(References.Initial_Date)
         FinalDate.append(References.Final_Date)
      return (N_Order, CodeBr, Clients, Codes, Quantitys, Availables, Dispatcheds, InitialDate, FinalDate)

   def AddPMC(NameTable: str, TABLA:str, REF: str, N_ORDER:str, CODEBAR: str, CLIENT: str,
              CODE: str, QUANTITY: int, AVAILABLE: str, DISPATCHE: str, INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      if NameTable == Settings.Var_MC(): MP = SQLPMC()
      elif NameTable == Settings.Var_RM(): MP = SQLRM()
      MP.Ref = REF
      MP.Num_Order = N_ORDER
      MP.CodeB = CODEBAR
      MP.Client = CLIENT
      MP.Code = CODE
      MP.Quantity = QUANTITY
      MP.Available = AVAILABLE
      MP.Dispatched = DISPATCHE
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      session.add(MP)
      session.commit()
      session.close()

   def DeletePMC(NameTable: str, TABLA: str, CLIENT: str, N_ORDER: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(FunctionPR.WhichTable(NameTable)).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).delete()
      session.commit()
      session.close()

   def DeleteALLPMC(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(FunctionPR.WhichTable(NameTable)).delete()
      session.commit()
      session.close()

   def UpdatePMC(NameTable: str, TABLA: str, CLIENT: str, N_ORDER: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      Table = FunctionPR.WhichTable(NameTable)
      if DATO_MOD == Settings.Var_Comp35(): session.query(Table).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({Table.Num_Order: Value})
      elif DATO_MOD == Settings.Var_Comp1(): session.query(Table).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({Table.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp38(): session.query(Table).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({Table.Client: Value})
      elif DATO_MOD == Settings.Var_Comp45(): session.query(Table).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({Table.Code: Value})
      elif DATO_MOD == Settings.Var_Comp39(): session.query(Table).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({Table.Quantity: Value})
      elif DATO_MOD == Settings.Var_Comp40(): session.query(Table).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({Table.Available: Value})
      elif DATO_MOD == Settings.Var_Comp41(): session.query(Table).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({Table.Dispatched: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(Table).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({Table.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(Table).filter_by(Client=CLIENT).filter_by(Num_Order=N_ORDER).update({Table.Final_Date: Value})
      session.commit()
      session.close()

   def CreatePMC(NameTable: str, TABLA: str):
      Table = FunctionPR.WhichTable(NameTable)
      engine = create_engine(TABLA, echo=True)
      Table.metadata.create_all(engine)

   def WhichTable(NameTable:str):
      if NameTable == Settings.Var_MC(): return SQLPMC
      elif NameTable == Settings.Var_RM(): return SQLRM