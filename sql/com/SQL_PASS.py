from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLPERMITION(Base):
   __tablename__ = 'AUTORIZACION'
   Permition_Op = Column("Permiso Operador", Integer, primary_key=True)
   Permition_All = Column("Permiso TOTAL", Integer)

   def FindPermition(TABLA: str, PERMITION: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      PERM = session.query(SQLPERMITION).all()
      session.close()
      for Permition in PERM:
         if PERMITION == Settings.Var_Comp15(): return Permition.Permition_Op
         elif PERMITION == Settings.Var_Comp31(): return Permition.Permition_All

   def UpdatePermition(TABLA: str, PERMITION: str, NEW_Permition: int):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      ValuePermition = SQLPERMITION.FindPermition(TABLA, PERMITION)
      if PERMITION == Settings.Var_Comp15(): session.query(SQLPERMITION).filter_by(Permition_Op=ValuePermition).update({SQLPERMITION.Permition_Op: NEW_Permition})
      elif PERMITION == Settings.Var_Comp31(): session.query(SQLPERMITION).filter_by(Permition_All=ValuePermition).update({SQLPERMITION.Permition_All: NEW_Permition})
      session.commit()
      session.close()