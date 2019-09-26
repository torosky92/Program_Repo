from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLPW(Base):
   __tablename__ = 'PASSWORD'
   Pass = Column("Contrasena", String, primary_key=True)

   def FindPW():
      engine = create_engine(Settings.Dir_PW(), echo=True)
      Session = sessionmaker(engine)
      session =Session()
      PASS = session.query(SQLPW).all()
      session.close()
      for Pw in PASS:
         return Pw.Pass

   def UpdatePW(PW: str):
      engine = create_engine(Settings.Dir_PW(), echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      ValuePW = SQLPW.FindPW()
      session.query(SQLPW).filter_by(Pass=ValuePW).update({SQLPW.Pass: PW})
      session.commit()
      session.close()

   def CreatePW():
      engine = create_engine(Settings.Dir_PW(), echo=True)
      Base.metadata.create_all(bind=engine)