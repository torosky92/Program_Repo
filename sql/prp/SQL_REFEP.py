from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()
Reference = Column("REFERENCIA", String)
class SQLREFEP(Base):
   __tablename__ = 'REFERENCIA DE RECEPCION'
   Id = Column("ID", Integer, primary_key=True)
   TypeP = Column("TIPO DE PRODUCTO", String)
   Code = Column("CODIGO", String)

   def FindTypeP(TABLA: str, REF: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ref = session.query(SQLREFEP).all()
      session.close()
      Codes = []
      for REFERENCE in ref:
         if REF == REFERENCE.TypeP:
            Codes.append(REFERENCE.Code)
      return (Codes)

   def FindALLRef(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      Ref = session.query(SQLREFEP).all()
      session.close()
      New_TypeP = []
      New_Code = []
      for REFERENCE in Ref:
         New_TypeP.append(REFERENCE.TypeP)
         New_Code.append(REFERENCE.Code)
      return (New_TypeP, New_Code)

   def AddRef(TABLA: str, TYPEP: str, CODE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      MP = SQLREFEP()
      MP.TypeP = TYPEP
      MP.Code = CODE
      session.add(MP)
      session.commit()
      session.close()

   def DeleteRef(TABLA: str, TYPEP: str, CODE: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLREFEP).filter_by(TypeP=TYPEP).filter_by(Code=CODE).delete()
      session.commit()
      session.close()

   def DeleteALLRef(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLREFEP).delete()
      session.commit()
      session.close()

   def UpdateRef(TABLA: str, TYPE: str, TYPEP: str, CODE: str,  Item: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if TYPE == Settings.Var_Comp50(): session.query(SQLREFEP).filter_by(TypeP=TYPEP).filter_by(Code=CODE).update({SQLREFEP.TypeP: Item})
      else: session.query(SQLREFEP).filter_by(TypeP=TYPEP).filter_by(Code=CODE).update({SQLREFEP.Code: Item})
      session.commit()
      session.close()

   def CreateRef(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)