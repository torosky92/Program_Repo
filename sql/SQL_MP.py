from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLMP(Base):
   __tablename__ = 'DATOS_MATERIA_PRIMA'
   Ref = Column("REF", Integer, primary_key=True)
   Ref2 = Column("REF2", String)
   Worker = Column("OPERADOR", String)
   Provider = Column("PROVEEDOR", String)
   Reference = Column("REFERENCIA", String)
   Presentation = Column("PRESENTACION", String)
   Num_Rem = Column("NUMERO_DE_REMISION", String)
   Num_Pre = Column("NUMERO_DE_PRESENTACION", Integer)
   Total_Weight = Column("PESO_TOTAL", Float)
   Initial_Date = Column("FECHA_DE_INICIO", String)
   Final_Date = Column("FECHA_FINAL", String)
   Code = Column("CODIGO_DE_BARRAS", String)
   Num_Coils = Column("NUMERO_DE_BOBINAS", Integer)

   def FindMP(REFERENCE: str):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLMP).all()
      session.close()
      for References in ref:
         if References.Ref2 == REFERENCE:
            return (References.Ref2, References.Worker, References.Provider, References.Reference, References.Presentation,
                    References.Num_Rem, References.Num_Pre, References.Total_Weight, References.Initial_Date, References.Final_Date,
                    References.Code, References.Num_Coils)

   def AddMP(REF2: str, WORKER: str, PROVIDER: str, REFERENCE: str,
             PRESENTATION: str, NUM_REM: str, NUM_PRE: int, TOTAL_WEIGHT: float,
             INITIAL_DATE: str, FINAL_DATE: str, CODE: str, NUM_COILS: int
             ):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLMP()
      MP.Ref2 = REF2
      MP.Worker = WORKER
      MP.Provider = PROVIDER
      MP.Reference = REFERENCE
      MP.Presentation = PRESENTATION
      MP.Num_Rem = NUM_REM
      MP.Num_Pre = NUM_PRE
      MP.Num_Coils = NUM_COILS
      MP.Total_Weight = TOTAL_WEIGHT
      MP.Initial_Date = INITIAL_DATE
      MP.Final_Date = FINAL_DATE
      MP.Code = CODE
      session.add(MP)
      session.commit()
      session.close()

   def DeleteMP(REMISION: str, REFERENCIA: str):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLMP).filter_by(Ref2=REMISION).filter_by(Reference=REFERENCIA).delete()
      session.commit()
      session.close()

   def UpdateMP(REMISION: str, DATO_MOD, Value):
      engine = create_engine('sqlite:///lib/CN.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      valueRef2, ValueWork, ValueProv, ValueReference, ValuePres, ValueRem, ValueNunPre, ValueTotalW, ValueInDate, ValueFinalDate, ValueCode, ValueCoils = SQLMP.FindMP(REMISION)
      if DATO_MOD == "REF2":
         session.query(SQLMP).filter_by(Ref2=valueRef2).update({SQLMP.Ref2: Value})
      elif DATO_MOD == "OPERADOR":
         session.query(SQLMP).filter_by(Worker=ValueWork).update({SQLMP.Worker: Value})
      elif DATO_MOD == "PROVEEDOR":
         session.query(SQLMP).filter_by(Provider=ValueProv).update({SQLMP.Provider: Value})
      elif DATO_MOD == "REFERENCIA":
         session.query(SQLMP).filter_by(Reference=ValueReference).update({SQLMP.Reference: Value})
      elif DATO_MOD == "PRESENTACION":
         session.query(SQLMP).filter_by(Presentation=ValuePres).update({SQLMP.Presentation: Value})
      elif DATO_MOD == "NUMERO DE REMISION":
         session.query(SQLMP).filter_by(Num_Rem=ValueRem).update({SQLMP.Num_Rem: Value})
      elif DATO_MOD == "NUMERO DE PRESENTACION":
         session.query(SQLMP).filter_by(Num_Pre=ValueNunPre).update({SQLMP.Num_Pre: Value})
      elif DATO_MOD == "PESO TOTAL":
         session.query(SQLMP).filter_by(Total_Weight=ValueTotalW).update({SQLMP.Total_Weight: Value})
      elif DATO_MOD == "FECHA DE INICIO":
         session.query(SQLMP).filter_by(Initial_Date=ValueInDate).update({SQLMP.Initial_Date: Value})
      elif DATO_MOD == "FECHA FINAL":
         session.query(SQLMP).filter_by(Final_Date=ValueFinalDate).update({SQLMP.Final_Date: Value})
      elif DATO_MOD == "CODIGO DE BARRAS":
         session.query(SQLMP).filter_by(Code=ValueCode).update({SQLMP.Code: Value})
      elif DATO_MOD == "NUMERO DE BOBINAS":
         session.query(SQLMP).filter_by(Num_Coils=ValueCoils).update({SQLMP.Num_Coils: Value})
      session.commit()
      session.close()