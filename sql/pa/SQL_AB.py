from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLAB(Base):
   __tablename__ = 'ALMACEN DE BOYA'
   Id = Column("REF", Integer, primary_key=True)
   CodeB = Column("CODIGO BARRAS", String)
   Lote = Column("LOTE", String)
   Quantity = Column("CANTIDAD DEL LOTE", Integer)
   QuantityD = Column("CANTIDAD DISPONIBLE", Integer)
   Initial_Date = Column("FECHA INICIO", String)
   Final_Date = Column("FECHA FINAL", String)

   def FindAB(TABLA: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLAB).all()
      session.close()
      for References in ref:
         if References.Lote == LOTE:
            return (References.CodeB, References.Lote, References.Quantity, References.QuantityD, References.Initial_Date, References.Final_Date)

   def FindALLAB(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLAB).all()
      session.close()
      Refs = []
      CodeBr = []
      Lotes = []
      Quantitys = []
      Quantityds = []
      InitialDate = []
      FinalDate = []
      for References in ref:
         Refs.append(References.Ref)
         CodeBr.append(References.CodeB)
         Lotes.append(References.Lote)
         Quantitys.append(References.Quantity)
         Quantityds.append(References.QuantityD)
         InitialDate.append(References.Initial_Date)
         FinalDate.append(References.Final_Date)
      return (CodeBr, Lotes, Quantitys, Quantityds, InitialDate, FinalDate)

   def AddAB(TABLA:str, REF: str, CODEBAR: str, LOTE: str, QUANTITY: int, QUANTITYD: str, INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLAB()
      MP.Ref = REF
      MP.CodeB = CODEBAR
      MP.Lote = LOTE
      MP.Quantity = QUANTITY
      MP.QuantityD = QUANTITYD
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      session.add(MP)
      session.commit()
      session.close()

   def DeleteAB(TABLA: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLAB).filter_by(Lote=LOTE).delete()
      session.commit()
      session.close()

   def DeleteALLAB(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLAB).delete()
      session.commit()
      session.close()

   def UpdateAB(TABLA: str, LOTE: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if DATO_MOD == Settings.Var_Comp1(): session.query(SQLAB).filter_by(Lote=LOTE).update({SQLAB.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp38(): session.query(SQLAB).filter_by(Lote=LOTE).update({SQLAB.Lote: Value})
      elif DATO_MOD == Settings.Var_Comp49(): session.query(SQLAB).filter_by(Lote=LOTE).update({SQLAB.Quantity: Value})
      elif DATO_MOD == Settings.Var_Comp47(): session.query(SQLAB).filter_by(Lote=LOTE).update({SQLAB.QuantityD: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(SQLAB).filter_by(Lote=LOTE).update({SQLAB.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(SQLAB).filter_by(Lote=LOTE).update({SQLAB.Final_Date: Value})
      session.commit()
      session.close()

   def CreateAB(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)