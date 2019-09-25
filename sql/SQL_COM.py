from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, update
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class SQLCOM(Base):
   __tablename__ = 'CONEXION_COM'
   #id = Column("ID", Integer, primary_key=True)
   Rfid = Column("LECTOR_TARJETA", String, primary_key=True)
   Weighing = Column("BASCULA", String)
   Permition = Column("AUTORIZACION", Integer)

   def AddCom(RFID: str,
              WEIGHING: str,
              PERMITION: str
              ):
      engine = create_engine('sqlite:///lib/CN.db', echo=True)
      Base.metadata.create_all(engine)
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
      engine = create_engine('sqlite:///lib/CN.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      Coms = session.query(SQLCOM).all()
      session.close()
      for com in Coms:
         if COM == "RFID":
            return com.Rfid
         elif COM == "BASCULA":
            return com.Weighing
         elif COM == "PERMITION":
            return com.Permition

   def UpdateCom(CONECT: str, COM: str):
      engine = create_engine('sqlite:///lib/CN.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      valueCOM = SQLCOM.FindCom(CONECT)
      if CONECT == "RFID":
         session.query(SQLCOM).filter_by(Rfid=valueCOM).update({SQLCOM.Rfid: COM})
      elif CONECT == "BASCULA":
         session.query(SQLCOM).filter_by(Weighing=valueCOM).update({SQLCOM.Weighing: COM})
      elif CONECT == "PERMITION":
         session.query(SQLCOM).filter_by(Permition=valueCOM).update({SQLCOM.Permition:COM})
      session.commit()
      session.close()