from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLCOM(Base):
   __tablename__ = 'CONEXION_COM'
   Rfid = Column("LECTOR_TARJETA", String, primary_key=True)
   Weighing = Column("BASCULA", String)
   Permition = Column("AUTORIZACION", Integer)

   def AddCom(RFID: str, WEIGHING: str, PERMITION: str):
      engine = create_engine(Settings.Dir_CN(), echo=True)
      Session = sessionmaker(engine)
      session = Session()
      COM = SQLCOM()
      COM.Rfid = RFID
      COM.Weighing = WEIGHING
      COM.Permition = PERMITION
      session.add(COM)
      session.commit()
      session.close()

   def FindCom(COM: str):
      engine = create_engine(Settings.Dir_CN(), echo=True)
      Session = sessionmaker(engine)
      session =Session()
      Coms = session.query(SQLCOM).all()
      session.close()
      for com in Coms:
         if COM == Settings.Var_Find1(): return com.Rfid
         elif COM == Settings.Var_Find2(): return com.Weighing
         elif COM == Settings.Var_Find3(): return com.Permition

   def UpdateCom(CONECT: str, COM: str):
      engine = create_engine(Settings.Dir_CN(), echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      valueCOM = SQLCOM.FindCom(CONECT)
      if CONECT == Settings.Var_Find1(): session.query(SQLCOM).filter_by(Rfid=valueCOM).update({SQLCOM.Rfid: COM})
      elif CONECT == Settings.Var_Find2(): session.query(SQLCOM).filter_by(Weighing=valueCOM).update({SQLCOM.Weighing: COM})
      elif CONECT == Settings.Var_Find3(): session.query(SQLCOM).filter_by(Permition=valueCOM).update({SQLCOM.Permition:COM})
      session.commit()
      session.close()

   def CreateCom():
      engine = create_engine(Settings.Dir_CN(), echo=True)
      Base.metadata.create_all(bind=engine)