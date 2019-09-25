import numpy as np
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine, Numeric
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Template(object):
    Id = Column("ID", Integer, primary_key=True)
    CodeB = Column("CODIGO_DE_BARRAS", String)
    Num_Pre = Column("NUMERO_DE_PRESENTACION", Integer)

class EEE(Template, Base):
    __tablename__ = "EJEMPLO1"

class EDE(Template, Base):
    __tablename__ = "EJEMPLO2"

class Forms:
    def AddEX(NameTable: str, TABLA:str, CODEB: str, NUM_PRE: int):
      engine = create_engine(TABLA, echo=True)
      if NameTable == "Pe":
        MP = EEE()
        Session = sessionmaker(engine)
        session = Session()
      else:
          MP = EDE()
          Session = sessionmaker(engine)
          session = Session()
      MP.CodeB = CODEB
      MP.Num_Pre = NUM_PRE
      session.add(MP)
      session.commit()
      session.close()
    def Find(NameTable: str, TABLA: str):
        engine = create_engine(TABLA, echo=True)
        #Base.metadata.create_all(engine)
        Session = sessionmaker(engine)
        session = Session()
        if NameTable == "Pe":
            ref = session.query(EEE).all()
        else:
            ref = session.query(EDE).all()
        session.close()
        CodeBr = []
        NumPre = []
        for References in ref:
            CodeBr.append(References.CodeB)
            NumPre.append(References.Num_Pre)
        return (CodeBr, NumPre)

    def DeleteALL(NameTable: str, TABLA: str):
        engine = create_engine(TABLA, echo=True)
        #Base.metadata.create_all(engine)
        Session = sessionmaker(engine)
        session = Session()
        if NameTable == "Pe":
            session.query(EEE).delete()
        else:
            session.query(EDE).delete()
        session.commit()
        session.close()

    def Delete(NameTable: str, TABLA: str, CODEB: str):
        engine = create_engine(TABLA, echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(engine)
        session = Session()
        if NameTable == "Pe":
            session.query(EEE).filter_by(CodeB=CODEB).delete()
        else:
            session.query(EDE).filter_by(CodeB=CODEB).delete()
        session.commit()
        session.close()