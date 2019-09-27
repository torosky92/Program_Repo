from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLAM(Base):
   __tablename__ = 'ALMACEN DE MULTIFILAMENTO'
   Id = Column("REF", Integer, primary_key=True)
   CodeB = Column("CODIGO BARRAS", String)
   Lote = Column("LOTE", String)
   Material = Column("MATERIAL", String)
   Diameter = Column("DIAMETRO", String)
   Presentation = Column("PRESENTACION", String)
   Num_Meshes = Column("NUMERO DE MALLAS", Integer)
   Quantity = Column("CANTIDAD DEL LOTE", Integer)
   QuantityD = Column("CANTIDAD DISPONIBLE", Integer)
   Initial_Date = Column("FECHA INICIO", String)
   Final_Date = Column("FECHA FINAL", String)

   def FindAM(TABLA: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLAM).all()
      session.close()
      for References in ref:
         if References.Lote == LOTE:
            return (References.CodeB, References.Lote, References.Material, References.Diameter,
                    References.Presentation, References.Num_Meshes, References.Quantity, References.QuantityD,
                    References.Initial_Date, References.Final_Date)

   def FindALLAM(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLAM).all()
      session.close()
      Refs = []
      CodeBr = []
      Lotes = []
      Materials = []
      Diameters = []
      Presentations = []
      NumMeshes = []
      Quantitys = []
      Quantityds = []
      InitialDate = []
      FinalDate = []
      for References in ref:
         Refs.append(References.Ref)
         CodeBr.append(References.CodeB)
         Lotes.append(References.Lote)
         Materials.append(References.Material)
         Diameters.append(References.Diameter)
         Presentations.append(References.Presentation)
         NumMeshes.append(References.Num_Meshes)
         Quantitys.append(References.Quantity)
         Quantityds.append(References.QuantityD)
         InitialDate.append(References.Initial_Date)
         FinalDate.append(References.Final_Date)
      return (CodeBr, Lotes, Materials, Diameters, Presentations, NumMeshes, Quantitys, Quantityds,
              InitialDate, FinalDate)

   def AddAM(TABLA:str, REF: str, CODEBAR: str, LOTE: str, MATERIAL: str, DIAMETER: str, PRESENTATION: str,
             N_MESHES: str, QUANTITY: int, QUANTITYD: str, INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLAM()
      MP.Ref = REF
      MP.CodeB = CODEBAR
      MP.Lote = LOTE
      MP.Material = MATERIAL
      MP.Diameter = DIAMETER
      MP.Presentation = PRESENTATION
      MP.Num_Meshes = N_MESHES
      MP.Quantity = QUANTITY
      MP.QuantityD = QUANTITYD
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      session.add(MP)
      session.commit()
      session.close()

   def DeleteAM(TABLA: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLAM).filter_by(Lote=LOTE).delete()
      session.commit()
      session.close()

   def DeleteALLAM(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLAM).delete()
      session.commit()
      session.close()

   def UpdateAM(TABLA: str, LOTE: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if DATO_MOD == Settings.Var_Comp1(): session.query(SQLAM).filter_by(Lote=LOTE).update({SQLAM.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp38(): session.query(SQLAM).filter_by(Lote=LOTE).update({SQLAM.Lote: Value})
      elif DATO_MOD == Settings.Var_Comp42(): session.query(SQLAM).filter_by(Lote=LOTE).update({SQLAM.Material: Value})
      elif DATO_MOD == Settings.Var_Comp43(): session.query(SQLAM).filter_by(Lote=LOTE).update({SQLAM.Diameter: Value})
      elif DATO_MOD == Settings.Var_Comp12(): session.query(SQLAM).filter_by(Lote=LOTE).update({SQLAM.Presentation: Value})
      elif DATO_MOD == Settings.Var_Comp44(): session.query(SQLAM).filter_by(Lote=LOTE).update({SQLAM.Num_Meshes: Value})
      elif DATO_MOD == Settings.Var_Comp49(): session.query(SQLAM).filter_by(Lote=LOTE).update({SQLAM.Quantity: Value})
      elif DATO_MOD == Settings.Var_Comp47(): session.query(SQLAM).filter_by(Lote=LOTE).update({SQLAM.QuantityD: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(SQLAM).filter_by(Lote=LOTE).update({SQLAM.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(SQLAM).filter_by(Lote=LOTE).update({SQLAM.Final_Date: Value})
      session.commit()
      session.close()

   def CreateAM(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)