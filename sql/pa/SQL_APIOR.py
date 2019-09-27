from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLAPIOR(Base):
   __tablename__ = 'ALMACEN DE PIOLA RETIRADO'
   Id = Column("REF", Integer, primary_key=True)
   CodeB = Column("CODIGO BARRAS", String)
   Lote = Column("LOTE", String)
   Material = Column("MATERIAL", String)
   Presentation = Column("PRESENTACION", String)
   Quantity = Column("CANTIDAD RETIRADO", Integer)
   Initial_Date = Column("FECHA INICIO", String)
   Final_Date = Column("FECHA FINAL", String)

   def FindAPIOR(TABLA: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLAPIOR).all()
      session.close()
      for References in ref:
         if References.Lote == LOTE:
            return (References.CodeB, References.Lote, References.Material, References.Presentation,
                     References.Quantity, References.Initial_Date, References.Final_Date)

   def FindALLAPIOR(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLAPIOR).all()
      session.close()
      Refs = []
      CodeBr = []
      Lotes = []
      Materials = []
      Presentations = []
      Quantitys = []
      InitialDate = []
      FinalDate = []
      for References in ref:
         Refs.append(References.Ref)
         CodeBr.append(References.CodeB)
         Lotes.append(References.Client)
         Materials.append(References.Material)
         Presentations.append(References.Presentation)
         Quantitys.append(References.Quantity)
         InitialDate.append(References.Initial_Date)
         FinalDate.append(References.Final_Date)
      return (CodeBr, Lotes, Materials, Presentations, Quantitys, InitialDate, FinalDate)

   def AddAPIOR(TABLA:str, REF: str, CODEBAR: str, LOTE: str, MATERIAL: str, PRESENTATION: str, QUANTITY: int, INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLAPIOR()
      MP.Ref = REF
      MP.CodeB = CODEBAR
      MP.Lote = LOTE
      MP.Material = MATERIAL
      MP.Presentation = PRESENTATION
      MP.Quantity = QUANTITY
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      session.add(MP)
      session.commit()
      session.close()

   def DeleteAPIOR(TABLA: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLAPIOR).filter_by(Lote=LOTE).delete()
      session.commit()
      session.close()

   def DeleteALLAPIOR(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLAPIOR).delete()
      session.commit()
      session.close()

   def UpdateAPIOR(TABLA: str, LOTE: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if DATO_MOD == Settings.Var_Comp1(): session.query(SQLAPIOR).filter_by(Lote=LOTE).update({SQLAPIOR.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp38(): session.query(SQLAPIOR).filter_by(Lote=LOTE).update({SQLAPIOR.Lote: Value})
      elif DATO_MOD == Settings.Var_Comp42(): session.query(SQLAPIOR).filter_by(Lote=LOTE).update({SQLAPIOR.Material: Value})
      elif DATO_MOD == Settings.Var_Comp12(): session.query(SQLAPIOR).filter_by(Lote=LOTE).update({SQLAPIOR.Presentation: Value})
      elif DATO_MOD == Settings.Var_Comp48(): session.query(SQLAPIOR).filter_by(Lote=LOTE).update({SQLAPIOR.Quantity: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(SQLAPIOR).filter_by(Lote=LOTE).update({SQLAPIOR.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(SQLAPIOR).filter_by(Lote=LOTE).update({SQLAPIOR.Final_Date: Value})
      session.commit()
      session.close()

   def CreateAPIOR(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)