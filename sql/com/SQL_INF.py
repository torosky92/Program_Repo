from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine, BLOB, Integer
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLINF(Base):
   __tablename__ = 'IMAGEN'
   ID = Column("ID", Integer, primary_key=True)
   Name = Column("NOMBRE", String)
   Imagen = Column("IMAGEN", BLOB)

   def FindALLInf(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      Ref = session.query(SQLINF).all()
      session.close()
      New_Name = []
      New_Imagen = []
      for REFERENCE in Ref:
         New_Name.append(REFERENCE.Name)
         New_Imagen.append(REFERENCE.Imagen)
      return (New_Name, New_Imagen)

   def AddInf(TABLA: str, NAME: str, IMAGEN: BLOB):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLINF()
      MP.Name = NAME
      MP.Imagen = IMAGEN
      session.add(MP)
      session.commit()
      session.close()

   def DeleteALLInf(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLINF).delete()
      session.commit()
      session.close()
