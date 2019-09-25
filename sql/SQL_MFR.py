from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLMFR(Base):
   __tablename__ = 'MATERIAL_FINAL_DE_RETORCIDO'
   Id = Column("ID", Integer, primary_key=True)
   Lote = Column("LOTE", String)
   Ref = Column("REF", String)
   CodeC = Column("CODIGO_COLOR", String)
   Reference = Column("REFERENCIA", String)
   Worker = Column("OPERADOR", String)
   Provider = Column("PROVEEDOR", String)
   Bottles = Column("CANTIDAD_DE_BOTELLAS", Integer)
   Weight = Column("PESO_NETO", Float)
   Weight_Desp = Column("PESO_DESPERDICION_NETO", Float)
   Steamed = Column("VAPORIZADO", String)
   Initial_Date = Column("FECHA_DE_INICIO", String)
   Final_Date = Column("FECHA_FINAL", String)

   def FindMFR(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLMFR).all()
      session.close()
      for References in ref:
         if References.Ref == REFERENCE:
            return (References.Lote, References.Ref, References.CodeC, References.Reference, References.Worker, References.Provider, References.Bottles,
                    References.Weight, References.Weight_Desp, References.Steamed, References.Initial_Date, References.Final_Date)

   def FindALLMFR(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLMFR).all()
      session.close()
      Lotes = []
      Refs = []
      CodeCs = []
      References2 = []
      Workers = []
      Providers = []
      Bottles2 = []
      Weights = []
      WeightDeps = []
      Steameds = []
      InitialD = []
      FinalD = []
      for References in ref:
         Lotes.append(References.Lote)
         Refs.append(References.Ref)
         CodeCs.append(References.CodeC)
         References2.append(References.Reference)
         Workers.append(References.Worker)
         Providers.append(References.Provider)
         Bottles2.append(References.Bottles)
         Weights.append(References.Weight)
         WeightDeps.append(References.Weight_Desp)
         Steameds.append(References.Steamed)
         InitialD.append(References.Initial_Date)
         FinalD.append(References.Final_Date)
      return (Lotes, Refs, CodeCs, References2, Workers, Providers, Bottles2, Weights, WeightDeps, Steameds,InitialD, FinalD)

   def AddMFR(TABLA:str, LOTE: str, REF: str, CODEC: str, REFERENCE: str, WORKER: str, PROVIDER: str, BOTTLES: int,
              WEIGHT: float, WEIGHT_DESP: float, STEAMED: str, INITIAL_DATE: str, FINAL_DATE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLMFR()
      MP.Lote = LOTE
      MP.Ref = REF
      MP.CodeC = CODEC
      MP.Reference = REFERENCE
      MP.Worker = WORKER
      MP.Provider = PROVIDER
      MP.Bottles = BOTTLES
      MP.Weight = WEIGHT
      MP.Weight_Desp = WEIGHT_DESP
      MP.Steamed = STEAMED
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      session.add(MP)
      session.commit()
      session.close()

   def DeleteMFR(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMFR).filter_by(Ref=REFERENCE).delete()
      session.commit()
      session.close()

   def DeleteALLMFR(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMFR).delete()
      session.commit()
      session.close()

   def UpdateMFR(TABLA: str, REMISION: str, DATO_MOD, Value):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      ValueLote, valueRef, ValueCodeC, ValueReference, ValueWorker, ValueProvider, ValueBottles, ValueW, ValueWD, ValueSteamed, ValueInDate, ValueOutDate = SQLMFR.FindMFR(TABLA, REMISION)
      if DATO_MOD == "REFERENCIA":
         session.query(SQLMFR).filter_by(Ref=valueRef).update({SQLMFR.Ref: Value})
      elif DATO_MOD == "LOTE":
         session.query(SQLMFR).filter_by(Lote=ValueLote).update({SQLMFR.Lote: Value})
      elif DATO_MOD == "CODIGO DE COLORES":
         session.query(SQLMFR).filter_by(CodeC=ValueCodeC).update({SQLMFR.CodeC: Value})
      elif DATO_MOD == "OPERADOR":
         session.query(SQLMFR).filter_by(Worker=ValueWorker).update({SQLMFR.Worker: Value})
      elif DATO_MOD == "REFERENCIA HILO":
         session.query(SQLMFR).filter_by(Reference=ValueReference).update({SQLMFR.Machine: Value})
      elif DATO_MOD == "PROVEEDOR":
         session.query(SQLMFR).filter_by(Provider=ValueProvider).update({SQLMFR.Provider: Value})
      elif DATO_MOD == "FECHA DE INICIO":
         session.query(SQLMFR).filter_by(Initial_Date=ValueInDate).update({SQLMFR.Initial_Date: Value})
      elif DATO_MOD == "FECHA FINAL":
         session.query(SQLMFR).filter_by(Final_Date=ValueOutDate).update({SQLMFR.Final_Date: Value})
      elif DATO_MOD == "CANTIDAD DE BOTELLAS":
         session.query(SQLMFR).filter_by(Bottles=ValueBottles).update({SQLMFR.Bottles: Value})
      elif DATO_MOD == "VAPORIZADO":
         session.query(SQLMFR).filter_by(Steamed=ValueSteamed).update({SQLMFR.Steamed: Value})
      elif DATO_MOD == "PESO NETO":
         session.query(SQLMFR).filter_by(Weight=ValueW).update({SQLMFR.Weight: Value})
      elif DATO_MOD == "PESO DESPERDICIO":
         session.query(SQLMFR).filter_by(Weight_Desp=ValueWD).update({SQLMFR.Weight_Desp: Value})
      session.commit()
      session.close()