from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
from SettingsUser import SettingsUs
from Settings import Settings

Base = declarative_base()

class SQLClient(Base):
   __tablename__ = 'CLIENTES'
   Ref = Column("ID", Integer, primary_key=True)
   Name = Column("NOMBRE", String)
   Id = Column("TIPO DE DOCUMENTO", String)
   Num_Id = Column("NUMERO DE DOCUMENTO", String)
   Branch = Column("SUCURSAL", String)
   Address = Column("DIRECCION", String)
   Deparment = Column("DEPARTAMENTO", String)
   City = Column("CIUDAD", String)
   Mobile = Column("CELULAR", String)
   Phone = Column("TELEFONO", String)
   Mail = Column("CORREO", String)

   def FindClient(TABLA: str, CLIENT: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ids = session.query(SQLClient).all()
      session.close()
      for IDD in ids:
          if CLIENT == IDD.Name:
            return (IDD.Name, IDD.Id, IDD.Num_Id, IDD.Branch, IDD.Address, IDD.Deparment, IDD.City, IDD.Mobile, IDD.Phone, IDD.Mail)

   def FindAllClients(TABLA: str):
         engine = create_engine(TABLA, echo=True)
         Session = sessionmaker(engine)
         session = Session()
         Ref = session.query(SQLClient).all()
         session.close()
         New_Name = []
         New_ID = []
         New_NumID = []
         New_Branch = []
         New_Address = []
         New_Deparment = []
         New_City = []
         New_Mobile = []
         New_Phone = []
         New_Mail = []
         for IDD in Ref:
             New_Name.append(IDD.Name)
             New_ID.append(IDD.Id)
             New_NumID.append(IDD.Num_Id)
             New_Branch.append(IDD.Branch)
             New_Address.append(IDD.Address)
             New_Deparment.append(IDD.Deparment)
             New_City.append(IDD.City)
             New_Mobile.append(IDD.Mobile)
             New_Phone.append(IDD.Phone)
             New_Mail.append(IDD.Mail)
         return (New_Name, New_ID, New_NumID, New_Branch, New_Address, New_Deparment, New_City, New_Mobile, New_Phone, New_Mail)

   def AddClient(TABLA: str, REF: int, NAME: str, ID: str, NUM_ID: str, BRANCH: str, ADDRESS: str, DEPARMENT: str,
                 CITY: str, MOBILE: str, PHONE: str, MAIL: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      User = SQLClient()
      User.Ref = REF
      User.Name = NAME
      User.Id = ID
      User.Num_Id = NUM_ID
      User.Branch = BRANCH
      User.Address = ADDRESS
      User.Deparment = DEPARMENT
      User.City = CITY
      User.Mobile = MOBILE
      User.Phone = PHONE
      User.Mail = MAIL
      session.add(User)
      session.commit()
      session.close()

   def DeleteClient(TABLA: str, NAME: str):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLClient).filter_by(Name=NAME).delete()
      session.commit()
      session.close()

   def UpdateClient(TABLA: str, NAME: str, DATO_MOD: str, Value):
      engine = create_engine(TABLA, echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      if DATO_MOD == SettingsUs.Ref_User2(): session.query(SQLClient).filter_by(Name=NAME).update({SQLClient.Name: Value})
      elif DATO_MOD == SettingsUs.Ref_User49(): session.query(SQLClient).filter_by(Name=NAME).update({SQLClient.Id: Value})
      elif DATO_MOD == SettingsUs.Ref_User50(): session.query(SQLClient).filter_by(Name=NAME).update({SQLClient.Num_Id: Value})
      elif DATO_MOD == SettingsUs.Ref_User51(): session.query(SQLClient).filter_by(Name=NAME).update({SQLClient.Branch: Value})
      elif DATO_MOD == SettingsUs.Ref_User25(): session.query(SQLClient).filter_by(Name=NAME).update({SQLClient.Address: Value})
      elif DATO_MOD == SettingsUs.Ref_User52(): session.query(SQLClient).filter_by(Name=NAME).update({SQLClient.Deparment: Value})
      elif DATO_MOD == SettingsUs.Ref_User53(): session.query(SQLClient).filter_by(Name=NAME).update({SQLClient.City: Value})
      elif DATO_MOD == SettingsUs.Ref_User21(): session.query(SQLClient).filter_by(Name=NAME).update({SQLClient.Mobile: Value})
      elif DATO_MOD == SettingsUs.Ref_User20(): session.query(SQLClient).filter_by(Name=NAME).update({SQLClient.Phone: Value})
      elif DATO_MOD == SettingsUs.Ref_User29(): session.query(SQLClient).filter_by(Name=NAME).update({SQLClient.Mail: Value})
      session.commit()
      session.close()

   def CreateClient(TABLA: str):
      engine = create_engine(TABLA, echo=True)
      Base.metadata.create_all(bind=engine)