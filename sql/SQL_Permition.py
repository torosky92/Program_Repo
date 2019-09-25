from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLPERMITION(Base):
   __tablename__ = 'AUTORIZACION'
   Permition_Op = Column("PERMISO_OPERADOR", Integer, primary_key=True)
   Permition_All = Column("PERMISO_TOTAL", Integer)

   def FindPermition(PERMITION: str):
      engine = create_engine('sqlite:///lib/PW.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      PERM = session.query(SQLPERMITION).all()
      session.close()
      for Permition in PERM:
         if PERMITION == "OPERADOR":
            return Permition.Permition_Op
         elif PERMITION == "TOTAL":
            return Permition.Permition_All

   def UpdatePermition(PERMITION: str, NEW_Permition: int):
      engine = create_engine('sqlite:///lib/PW.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      ValuePermition = SQLPERMITION.FindToken(PERMITION)
      if PERMITION == "OPERADOR":
         session.query(SQLPERMITION).filter_by(Permition_Op=ValuePermition).update({SQLPERMITION.Permition_Op: NEW_Permition})
      elif PERMITION == "TOTAL":
         session.query(SQLPERMITION).filter_by(Permition_All=ValuePermition).update({SQLPERMITION.Permition_All: NEW_Permition})
      session.commit()
      session.close()