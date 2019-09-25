from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLPARO(Base):
   __tablename__ = 'LISTA_DE_PAROS'
   Id = Column("ID", Integer, primary_key=True)
   Stop = Column("PARO", String)

   def FindPARO(REFERENCE: str):
      engine = create_engine('sqlite:///lib/RMAQ.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      ref = session.query(SQLPARO).all()
      session.close()
      PARO=[]
      for References in ref:
         PARO.append(References.Stop)
      return PARO

   def FindPAROREF(REFERENCE: str):
      engine = create_engine('sqlite:///lib/RMAQ.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      id = session.query(SQLPARO).all()
      session.close()
      for ID in id:
         if ID.Id == REFERENCE:
            return (ID.Id, ID.Stop)

   def AddPARO(STOPED: str):
      engine = create_engine('sqlite:///lib/RMAQ.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      PARO = SQLPARO()
      PARO.Stop = STOPED
      session.add(PARO)
      session.commit()
      session.close()

   def DeleteMAQ(ID: str):
      engine = create_engine('sqlite:///lib/RMAQ.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLPARO).filter_by(Id=ID).delete()
      session.commit()
      session.close()

   def UpdatePARO(REFERENCE: str, DATO_MOD: str, Value: str):
      engine = create_engine('sqlite:///lib/RMAQ.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      ValueId, ValueParo = SQLPARO.FindPAROREF(REFERENCE)
      if DATO_MOD == "ID":
         session.query(SQLPARO).filter_by(Id=ValueId).update({SQLPARO.Id: Value})
      elif DATO_MOD == "PARO":
         session.query(SQLPARO).filter_by(Stop=ValueParo).update({SQLPARO.Stop: Value})
      session.commit()
      session.close()