from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLAPIO(Base):
   __tablename__ = 'ALMACEN DE PIOLA'
   Id = Column("REF", Integer, primary_key=True)
   CodeB = Column("CODIGO BARRAS", String)
   Lote = Column("LOTE", String)
   Material = Column("MATERIAL", String)
   Presentation = Column("PRESENTACION", String)
   Quantity = Column("CANTIDAD DEL LOTE", Integer)
   QuantityD = Column("CANTIDAD DISPONIBLE", Integer)
   Initial_Date = Column("FECHA INICIO", String)
   Final_Date = Column("FECHA FINAL", String)

   def FindAPIO(TABLA: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLAPIO).all()
      session.close()
      for References in ref:
         if References.Lote == LOTE:
            return (References.CodeB, References.Lote, References.Material, References.Presentation,
                     References.Quantity, References.QuantityD, References.Initial_Date, References.Final_Date)

   def FindALLAPIO(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLAPIO).all()
      session.close()
      Refs = []
      CodeBr = []
      Lotes = []
      Materials = []
      Presentations = []
      Quantitys = []
      Quantityds = []
      InitialDate = []
      FinalDate = []
      for References in ref:
         Refs.append(References.Ref)
         CodeBr.append(References.CodeB)
         Lotes.append(References.Client)
         Materials.append(References.Material)
         Presentations.append(References.Presentation)
         Quantitys.append(References.Quantity)
         Quantityds.append(References.QuantityD)
         InitialDate.append(References.Initial_Date)
         FinalDate.append(References.Final_Date)
      return (CodeBr, Lotes, Materials, Presentations, Quantitys, Quantityds, InitialDate, FinalDate)

   def AddAPIO(TABLA:str, REF: str, CODEBAR: str, LOTE: str, MATERIAL: str, PRESENTATION: str, QUANTITY: int, QUANTITYD: str, INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLAPIO()
      MP.Ref = REF
      MP.CodeB = CODEBAR
      MP.Lote = LOTE
      MP.Material = MATERIAL
      MP.Presentation = PRESENTATION
      MP.Quantity = QUANTITY
      MP.QuantityD = QUANTITYD
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      session.add(MP)
      session.commit()
      session.close()

   def DeleteAPIO(TABLA: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLAPIO).filter_by(Lote=LOTE).delete()
      session.commit()
      session.close()

   def DeleteALLAPIO(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLAPIO).delete()
      session.commit()
      session.close()

   def UpdateAPIO(TABLA: str, LOTE: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if DATO_MOD == Settings.Var_Comp1(): session.query(SQLAPIO).filter_by(Lote=LOTE).update({SQLAPIO.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp38(): session.query(SQLAPIO).filter_by(Lote=LOTE).update({SQLAPIO.Lote: Value})
      elif DATO_MOD == Settings.Var_Comp42(): session.query(SQLAPIO).filter_by(Lote=LOTE).update({SQLAPIO.Material: Value})
      elif DATO_MOD == Settings.Var_Comp12(): session.query(SQLAPIO).filter_by(Lote=LOTE).update({SQLAPIO.Presentation: Value})
      elif DATO_MOD == Settings.Var_Comp49(): session.query(SQLAPIO).filter_by(Lote=LOTE).update({SQLAPIO.Quantity: Value})
      elif DATO_MOD == Settings.Var_Comp47(): session.query(SQLAPIO).filter_by(Lote=LOTE).update({SQLAPIO.QuantityD: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(SQLAPIO).filter_by(Lote=LOTE).update({SQLAPIO.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(SQLAPIO).filter_by(Lote=LOTE).update({SQLAPIO.Final_Date: Value})
      session.commit()
      session.close()

   def CreateAPIO(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)