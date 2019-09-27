from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLCC(Base):
   __tablename__ = 'CODIGO_COLOR'
   Id = Column("ID", Integer, primary_key=True)
   CodeC = Column("CODIGO COLOR", String)

   def FindALLCC(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLCC).all()
      session.close()
      CC=[]
      for References in ref:
         CC.append(References.CodeC)
      return CC

   def FindCC(TABLA: str, COLOUR: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session =Session()
      id = session.query(SQLCC).all()
      session.close()
      for ID in id:
         if ID.CodeC == COLOUR:
            return (ID.CodeC)

   def AddCC(TABLA: str, COLOUR: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      CC = SQLCC()
      CC.CodeC = COLOUR
      session.add(CC)
      session.commit()
      session.close()

   def DeleteCC(TABLA: str, COLOUR: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLCC).filter_by(CodeC=COLOUR).delete()
      session.commit()
      session.close()

   def DeleteALLCC(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLCC).delete()
      session.commit()
      session.close()

   def UpdateCC(TABLA: str, COLOUR: str, Value: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLCC).filter_by(CodeC=COLOUR).update({SQLCC.CodeC: Value})
      session.commit()
      session.close()

   def CreateCC(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)