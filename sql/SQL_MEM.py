from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLMM(Base):
   __tablename__ = 'MEMORIA'
   Worker = Column("OPERADOR", String, primary_key=True)
   Provider = Column("PROVEEDOR", String)
   Reference = Column("REFERENCIA", String)
   Presentation = Column("PRESENTACION", String)
   Num_Rem = Column("NUMERO_DE_REMISION", String)
   Num_Pre = Column("NUMERO_DE_PRESENTACION", Integer)
   Total_Weight = Column("PESO_TOTAL", Float)
   Ref2 = Column("REF2", String)
   Code = Column("CODIGO_DE_BARRAS", String)

   def FindMM(REFERENCE: str):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLMM).all()
      session.close()
      for References in ref:
         if References.Ref2 == REFERENCE:
            return (References.Worker, References.Provider, References.Reference, References.Presentation,
                    References.Num_Rem, References.Num_Pre, References.Total_Weight, References.Ref2, References.Code)

   def AddMM(WORKER: str, PROVIDER: str, REFERENCE: str, PRESENTATION: str,
             NUM_REM: str, NUM_PRE: int, TOTAL_WEIGHT: float, REF2: str, CODE: str
             ):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      MM = SQLMM()
      MM.Worker = WORKER
      MM.Provider = PROVIDER
      MM.Reference = REFERENCE
      MM.Presentation = PRESENTATION
      MM.Num_Rem = NUM_REM
      MM.Num_Pre = NUM_PRE
      MM.Total_Weight = TOTAL_WEIGHT
      MM.Ref1 = REF2
      MM.Code = CODE
      session.add(MM)
      session.commit()
      session.close()

   def DeleteMM(REMISION: str):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMM).filter_by(Ref2=REMISION).delete()
      session.commit()
      session.close()

   def DeleteALL(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMM).delete()
      session.commit()
      session.close()

   def UpdateMM(REMISION: str, DATO_MOD, Value):
      engine = create_engine('sqlite:///lib/CN.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      ValueWork, ValueProv, ValueReference, ValuePres, ValueRem, ValueNunPre, ValueTotalW, valueRef2, ValueCode = SQLMM.FindMM(REMISION)
      if DATO_MOD == "REF2":
         session.query(SQLMM).filter_by(Ref2=valueRef2).update({SQLMM.Ref2: Value})
      elif DATO_MOD == "OPERADOR":
         session.query(SQLMM).filter_by(Worker=ValueWork).update({SQLMM.Worker: Value})
      elif DATO_MOD == "PROVEEDOR":
         session.query(SQLMM).filter_by(Provider=ValueProv).update({SQLMM.Provider: Value})
      elif DATO_MOD == "REFERENCIA":
         session.query(SQLMM).filter_by(Reference=ValueReference).update({SQLMM.Reference: Value})
      elif DATO_MOD == "PRESENTACION":
         session.query(SQLMM).filter_by(Presentation=ValuePres).update({SQLMM.Presentation: Value})
      elif DATO_MOD == "NUMERO DE REMISION":
         session.query(SQLMM).filter_by(Num_Rem=ValueRem).update({SQLMM.Num_Rem: Value})
      elif DATO_MOD == "NUMERO DE PRESENTACION":
         session.query(SQLMM).filter_by(Num_Pre=ValueNunPre).update({SQLMM.Num_Pre: Value})
      elif DATO_MOD == "PESO TOTAL":
         session.query(SQLMM).filter_by(Total_Weight=ValueTotalW).update({SQLMM.Total_Weight: Value})
      elif DATO_MOD == "CODIGO DE BARRAS":
         session.query(SQLMM).filter_by(Code=ValueCode).update({SQLMM.Code: Value})
      session.commit()
      session.close()