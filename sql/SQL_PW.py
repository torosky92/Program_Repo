from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLPW(Base):
   __tablename__ = 'PASSWORD'
   Pass = Column("CONTRASENA", String, primary_key=True)

   def FindPass():
      engine = create_engine('sqlite:///lib/PW.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      PASS = session.query(SQLPW).all()
      session.close()
      for Pw in PASS:
         return Pw.Token

   def UpdatePW(PW: str):
      engine = create_engine('sqlite:///lib/PW.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      ValuePW = SQLPW.FindToken()
      session.query(SQLPW).filter_by(Pass=ValuePW).update({SQLPW.Pass: PW})
      session.commit()
      session.close()