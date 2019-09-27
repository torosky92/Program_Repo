from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLST(Base):
   __tablename__ = 'LISTA_DE_PAROS'
   Id = Column("ID", Integer, primary_key=True)
   Stop = Column("PARO", String)

   def FindALLST(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLST).all()
      session.close()
      PARO = []
      for References in ref:
         PARO.append(References.Stop)
      return PARO

   def FindST(TABLA: str, REFERENCE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      id = session.query(SQLST).all()
      session.close()
      for ID in id:
         if ID.Id == REFERENCE:
            return (ID.Stop)

   def AddST(TABLA: str, STOPED: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      PARO = SQLST()
      PARO.Stop = STOPED
      session.add(PARO)
      session.commit()
      session.close()

   def DeleteST(TABLA: str, ID: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLST).filter_by(Id=ID).delete()
      session.commit()
      session.close()

   def DeleteALLST(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLST).delete()
      session.commit()
      session.close()

   def UpdateST(TABLA: str, REFERENCE: str, Value: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLST).filter_by(Stop=REFERENCE).update({SQLST.Stop: Value})
      session.commit()
      session.close()

   def CreateST(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)