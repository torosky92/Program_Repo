from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLST(Base):
   __tablename__ = 'LISTA_DE_PAROS'
   Id = Column("ID", Integer, primary_key=True)
   Stop = Column("PARO", String)

   def FindALLST():
      engine = create_engine(Settings.Dir_RMAQ(), echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLST).all()
      session.close()
      PARO = []
      for References in ref:
         PARO.append(References.Stop)
      return PARO

   def FindST(REFERENCE: str):
      engine = create_engine(Settings.Dir_RMAQ(), echo=True)
      Session = sessionmaker(engine)
      session = Session()
      id = session.query(SQLST).all()
      session.close()
      for ID in id:
         if ID.Id == REFERENCE:
            return (ID.Stop)

   def AddST(STOPED: str):
      engine = create_engine(Settings.Dir_RMAQ(), echo=True)
      Session = sessionmaker(engine)
      session = Session()
      PARO = SQLST()
      PARO.Stop = STOPED
      session.add(PARO)
      session.commit()
      session.close()

   def DeleteST(ID: str):
      engine = create_engine(Settings.Dir_RMAQ(), echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLST).filter_by(Id=ID).delete()
      session.commit()
      session.close()

   def DeleteALLST():
      engine = create_engine(Settings.Dir_RMAQ(), echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLST).delete()
      session.commit()
      session.close()

   def UpdateST(REFERENCE: str, Value: str):
      engine = create_engine(Settings.Dir_RMAQ(), echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLST).filter_by(Stop=REFERENCE).update({SQLST.Stop: Value})
      session.commit()
      session.close()

   def CreateST():
      engine = create_engine(Settings.Dir_RMAQ(), echo=True)
      Base.metadata.create_all(bind=engine)