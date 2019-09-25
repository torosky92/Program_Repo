from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLCC(Base):
   __tablename__ = 'LISTA_DE_PAROS'
   Id = Column("ID", Integer, primary_key=True)
   CodeC = Column("CODIGO COLOR", String)

   def FindCC(REFERENCE: str):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLCC).all()
      session.close()
      CC=[]
      for References in ref:
         CC.append(References.CodeC)
      return CC

   def FindCCR(REFERENCE: str):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      id = session.query(SQLCC).all()
      session.close()
      for ID in id:
         if ID.Id == REFERENCE:
            return (ID.Id, ID.CodeC)

   def AddCC(COLOUR: str):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      CC = SQLCC()
      CC.CodeC = COLOUR
      session.add(CC)
      session.commit()
      session.close()

   def DeleteCC(ID: str):
      engine = create_engine('sqlite:///lib/CBD.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLCC).filter_by(Id=ID).delete()
      session.commit()
      session.close()

   def UpdateCC(REFERENCE: str, DATO_MOD: str, Value: str):
      engine = create_engine('sqlite:///lib/CN.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      ValueId, ValueCC = SQLCC.FindCCR(REFERENCE)
      if DATO_MOD == "ID":
         session.query(SQLCC).filter_by(Id=ValueId).update({SQLCC.Id: Value})
      elif DATO_MOD == "PARO":
         session.query(SQLCC).filter_by(CodeC=ValueCC).update({SQLCC.CodeC: Value})
      session.commit()
      session.close()