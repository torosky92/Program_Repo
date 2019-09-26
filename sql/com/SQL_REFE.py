from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLREFE(Base):
   __tablename__ = 'REFERENCIA'
   Id = Column("ID", Integer, primary_key=True)
   Provider = Column("PROVEEDOR", String)
   Reference = Column("REFERENCIA", String)

   def FindRef(REF: str):
      engine = create_engine(Settings.Dir_REFE(), echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLREFE).all()
      session.close()
      for REFERENCE in ref:
         if REF == REFERENCE.Provider or REF == REFERENCE.Reference: return (REFERENCE.Provider, REFERENCE.Reference)

   def FindALLRef():
      engine = create_engine(Settings.Dir_REFE(), echo=True)
      Session = sessionmaker(engine)
      session = Session()
      Ref = session.query(SQLREFE).all()
      session.close()
      New_Pro = []
      New_Ref = []
      for REFERENCE in Ref:
         New_Pro.append(REFERENCE.Provider)
         New_Ref.append(REFERENCE.Reference)
      return (New_Pro, New_Ref)

   def AddRef(PROVIDER: str, REFERENCE: str):
      engine = create_engine(Settings.Dir_REFE(), echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLREFE()
      MP.Provider = PROVIDER
      MP.Reference = REFERENCE
      session.add(MP)
      session.commit()
      session.close()

   def DeleteRef(PROVIDER: str, REFERENCE: str):
      engine = create_engine(Settings.Dir_REFE(), echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLREFE).filter_by(Provider=PROVIDER).filter_by(Ref=REFERENCE).delete()
      session.commit()
      session.close()

   def DeleteALLRef():
      engine = create_engine(Settings.Dir_REFE(), echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLREFE).delete()
      session.commit()
      session.close()

   def UpdateRef(PROVIDER: str, REF: str, Item: str):
      engine = create_engine(Settings.Dir_REFE(), echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      ValuePro, ValueRef = SQLREFE.FindRef(REF)
      ValueProvider = ""
      ValueReference = ""
      if REF == Settings.Var_Comp13():
         for x in range(len(ValuePro)):
             if PROVIDER == ValuePro[x]:
               ValueProvider = ValuePro[x]
               ValueReference = ValueRef[x]
      elif REF == Settings.Var_Comp14():
         for x in range(len(ValuePro)):
            if PROVIDER == ValueRef[x]:
               ValueProvider = ValuePro[x]
               ValueReference = ValueRef[x]
      if REF == Settings.Var_Comp13(): session.query(SQLREFE).filter_by(Provider=ValueProvider).filter_by(Reference=ValueReference).update({SQLREFE.Reference: Item})
      else: session.query(SQLREFE).filter_by(Provider=ValueProvider).filter_by(Reference=ValueReference).update({SQLREFE.Provider: Item})
      session.commit()
      session.close()

   def CreateRef():
      engine = create_engine(Settings.Dir_REFE(), echo=True)
      Base.metadata.create_all(bind=engine)