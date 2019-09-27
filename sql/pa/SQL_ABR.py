from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLABR(Base):
   __tablename__ = 'ALMACEN DE BOYA RETIRADO'
   Id = Column("REF", Integer, primary_key=True)
   CodeB = Column("CODIGO BARRAS", String)
   Lote = Column("LOTE", String)
   Quantity = Column("CANTIDAD RETIRADO", Integer)
   Initial_Date = Column("FECHA INICIO", String)
   Final_Date = Column("FECHA FINAL", String)

   def FindABR(TABLA: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLABR).all()
      session.close()
      for References in ref:
         if References.Lote == LOTE:
            return (References.CodeB, References.Lote, References.Quantity, References.Initial_Date, References.Final_Date)

   def FindALLABR(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLABR).all()
      session.close()
      Refs = []
      CodeBr = []
      Lotes = []
      Quantitys = []
      InitialDate = []
      FinalDate = []
      for References in ref:
         Refs.append(References.Ref)
         CodeBr.append(References.CodeB)
         Lotes.append(References.Lote)
         Quantitys.append(References.Quantity)
         InitialDate.append(References.Initial_Date)
         FinalDate.append(References.Final_Date)
      return (CodeBr, Lotes, Quantitys, InitialDate, FinalDate)

   def AddABR(TABLA:str, REF: str, CODEBAR: str, LOTE: str, QUANTITY: int, INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLABR()
      MP.Ref = REF
      MP.CodeB = CODEBAR
      MP.Lote = LOTE
      MP.Quantity = QUANTITY
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      session.add(MP)
      session.commit()
      session.close()

   def DeleteABR(TABLA: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLABR).filter_by(Lote=LOTE).delete()
      session.commit()
      session.close()

   def DeleteALLABR(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLABR).delete()
      session.commit()
      session.close()

   def UpdateABR(TABLA: str, LOTE: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if DATO_MOD == Settings.Var_Comp1(): session.query(SQLABR).filter_by(Lote=LOTE).update({SQLABR.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp38(): session.query(SQLABR).filter_by(Lote=LOTE).update({SQLABR.Lote: Value})
      elif DATO_MOD == Settings.Var_Comp48(): session.query(SQLABR).filter_by(Lote=LOTE).update({SQLABR.Quantity: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(SQLABR).filter_by(Lote=LOTE).update({SQLABR.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(SQLABR).filter_by(Lote=LOTE).update({SQLABR.Final_Date: Value})
      session.commit()
      session.close()

   def CreateABR(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)