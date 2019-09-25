from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLREFE(Base):
   __tablename__ = 'REFERENCIA'
   Provider = Column("PROVEEDOR", String, primary_key=True)
   Reference = Column("REFERENCIA", String)

   def FindReference(REF: str):
      engine = create_engine('sqlite:///lib/REFE.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      PERM = session.query(SQLREFE).all()
      session.close()
      for Permition in PERM:
         if REF == "PROVEEDOR":
            return Permition.Permition_Op
         elif REF == "REFERENCIA":
            return Permition.Permition_All

   def UpdateReference(REF: str, Item: str):
      engine = create_engine('sqlite:///lib/REFE.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      ValueRef = SQLREFE.FindReference(REF)
      if REF == "PROVEEDOR":
         session.query(SQLREFE).filter_by(Provider=ValueRef).update({SQLREFE.Provider: Item})
      elif REF == "REFERENCIA":
         session.query(SQLREFE).filter_by(Reference=ValueRef).update({SQLREFE.Reference: Item})
      session.commit()
      session.close()