from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class Template(object):
   Id = Column("REF", Integer, primary_key=True)
   CodeB = Column("CODIGO BARRAS", String)
   Worker = Column("OPERADORES", String)
   Lote = Column("LOTE", String)
   TypeP = Column("TIPO DE PRESENTACION", String)
   Code = Column("CODIGO", String)
   Material = Column("MATERIAL", String)
   Diameter = Column("DIAMETRO", String)
   Presentation = Column("PRESENTACION", String)
   Num_Meshes = Column("NUMERO DE MALLAS", Integer)
   Quantity = Column("CANTIDAD DE LOTE", Integer)
   Initial_Date = Column("FECHA INICIO", String)
   Final_Date = Column("FECHA FINAL", String)

class SQLOUT(Template, Base):
   __tablename__ = 'PROCESO DE RETIRO DE ALMACEN'

class SQLIN(Template, Base):
   __tablename__ = 'PROCESO DE INGRESO DE ALMACEN'

class FunctionIN:
   def FindIN(NameTable: str, TABLA: str, WORKER: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(FunctionIN.WhichTable(NameTable)).all()
      session.close()
      for References in ref:
         if References.Worker == WORKER:
            if References.Lote == LOTE:
               return (References.CodeB, References.Worker, References.Lote, References.TypeP, References.Code,
                       References.Material, References.Diameter, References.Presentation, References.Num_Meshes,
                       References.Quantity, References.Initial_Date, References.Final_Date)

   def FindALLPIN(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(FunctionIN.WhichTable(NameTable)).all()
      session.close()
      Refs = []
      CodeBr = []
      Workers = []
      Lotes = []
      TypePs = []
      Codes = []
      Materials = []
      Diameters = []
      Presentations = []
      NumMeshes = []
      Quantitys = []
      InitialDate = []
      FinalDate = []
      for References in ref:
         Refs.append(References.Ref)
         CodeBr.append(References.CodeB)
         Workers.append(References.Worker)
         Lotes.append(References.Lote)
         TypePs.append(References.TypeP)
         Codes.append(References.Code)
         Materials.append(References.Material)
         Diameters.append(References.Diameter)
         Presentations.append(References.Presentation)
         NumMeshes.append(References.Num_Meshes)
         Quantitys.append(References.Quantity)
         InitialDate.append(References.Initial_Date)
         FinalDate.append(References.Final_Date)
      return (CodeBr, Workers, Lotes, TypePs, Codes, Materials, Diameters, Presentations, NumMeshes,
              Quantitys, InitialDate, FinalDate)

   def AddPIN(NameTable: str, TABLA:str, REF: str, CODEBAR: str, WORKER: str, LOTES: str, TYPEPRESENTATION: str, CODE:str,
              MATERIAL: str, DIAMETER: str, PRESENTATION: str, N_MESHES: str, QUANTITY: int, INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      if NameTable == Settings.Var_IN(): MP = SQLIN()
      elif NameTable == Settings.Var_OUT(): MP = SQLOUT()
      MP.Ref = REF
      MP.CodeB = CODEBAR
      MP.Worker = WORKER
      MP.Lote = LOTES
      MP.TypeP = TYPEPRESENTATION
      MP.Code = CODE
      MP.Material = MATERIAL
      MP.Diameter = DIAMETER
      MP.Presentation = PRESENTATION
      MP.Num_Meshes = N_MESHES
      MP.Quantity = QUANTITY
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      session.add(MP)
      session.commit()
      session.close()

   def DeleteIN(NameTable: str, TABLA: str, WORKER: str, LOTE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(FunctionIN.WhichTable(NameTable)).filter_by(Worker=WORKER).filter_by(Lote=LOTE).delete()
      session.commit()
      session.close()

   def DeleteALLIN(NameTable: str, TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(FunctionIN.WhichTable(NameTable)).delete()
      session.commit()
      session.close()

   def UpdateIN(NameTable: str, TABLA: str, WORKER: str, LOTE: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      Table = FunctionIN.WhichTable(NameTable)
      if DATO_MOD == Settings.Var_Comp35(): session.query(Table).filter_by(Worker=WORKER).filter_by(Lote=LOTE).update({Table.Num_Order: Value})
      elif DATO_MOD == Settings.Var_Comp1(): session.query(Table).filter_by(Worker=WORKER).filter_by(Lote=LOTE).update({Table.CodeB: Value})
      elif DATO_MOD == Settings.Var_Comp15(): session.query(Table).filter_by(Worker=WORKER).filter_by(Lote=LOTE).update({Table.Worker: Value})
      elif DATO_MOD == Settings.Var_Comp46(): session.query(Table).filter_by(Worker=WORKER).filter_by(Lote=LOTE).update({Table.TypeP: Value})
      elif DATO_MOD == Settings.Var_Comp45(): session.query(Table).filter_by(Worker=WORKER).filter_by(Lote=LOTE).update({Table.Code: Value})
      elif DATO_MOD == Settings.Var_Comp42(): session.query(Table).filter_by(Worker=WORKER).filter_by(Lote=LOTE).update({Table.Material: Value})
      elif DATO_MOD == Settings.Var_Comp43(): session.query(Table).filter_by(Worker=WORKER).filter_by(Lote=LOTE).update({Table.Diameter: Value})
      elif DATO_MOD == Settings.Var_Comp12(): session.query(Table).filter_by(Worker=WORKER).filter_by(Lote=LOTE).update({Table.Presentation: Value})
      elif DATO_MOD == Settings.Var_Comp44(): session.query(Table).filter_by(Worker=WORKER).filter_by(Lote=LOTE).update({Table.Num_Meshes: Value})
      elif DATO_MOD == Settings.Var_Comp39(): session.query(Table).filter_by(Worker=WORKER).filter_by(Lote=LOTE).update({Table.Quantity: Value})
      elif DATO_MOD == Settings.Var_Comp19(): session.query(Table).filter_by(Worker=WORKER).filter_by(Lote=LOTE).update({Table.Initial_Date: Value})
      elif DATO_MOD == Settings.Var_Comp20(): session.query(Table).filter_by(Worker=WORKER).filter_by(Lote=LOTE).update({Table.Final_Date: Value})
      session.commit()
      session.close()

   def CreateIN(NameTable: str, TABLA: str):
      Table = FunctionIN.WhichTable(NameTable)
      engine = create_engine(TABLA, echo=True)
      Table.metadata.create_all(engine)

   def WhichTable(NameTable:str):
      if NameTable == Settings.Var_IN(): return SQLIN
      elif NameTable == Settings.Var_OUT(): return SQLOUT