from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
from SettingsUser import SettingsUs
from Settings import Settings

Base = declarative_base()

class SQLUser(Base):
   __tablename__ = 'OPERADORES'
   Code = Column("CODIGO", String, primary_key=True)
   Id = Column("CEDULA", String)
   Name = Column("NOMBRE_DE_OPERARIO", String)
   Per1 = Column("PERMISO_RMP", Integer)
   Per2 = Column("PERMISO_RP", Integer)
   Per3 = Column("PERMISO_RETO", Integer)
   Per4 = Column("PERMISO_4", Integer)
   Per5 = Column("PERMISO_5", Integer)
   Per6 = Column("PERMISO_6", Integer)
   Per7 = Column("PERMISO_7", Integer)
   Per8 = Column("PERMISO_8", Integer)
   Per9 = Column("PERMISO_9", Integer)
   Per10 = Column("PERMISO_10", Integer)
   Gender = Column("GENERO", String)
   AreaW = Column("AREA_DE_TRABAJO", String)
   Position = Column("CARGO", String)
   Birthday = Column("FECHA_DE_NACIMIENTO", String)
   TypeB = Column("TIPO_DE_SANGRE",String)
   Grade = Column("GRADO_DE_ESCOLARIDAD", String)
   Profession = Column("PROFESION", String)
   Phone = Column("TELEFONO_FIJO", Integer)
   Mobile = Column("CELULAR", Integer)
   EPS = Column("EPS", String)
   ARL = Column("ARL", String)
   Pensions = Column("PENSIONES", String)
   Address = Column("DIRECCION", String)
   Neighborhood = Column("BARRIO", String)
   Municipality = Column("MUNICIPIO", String)
   Socioeconomic = Column("ESTRATO_SOCIOECONOMICO", String)
   Mail = Column("MAIL", String)
   NameSP = Column("NOMBRE_DE_CÓNYUGE_O_PADRES", String)
   Phone2 = Column("TELEFONO_FIJO_2", Integer)
   Mobile2 = Column("CELULAR_2", Integer)
   NameC = Column("NOMBRE_DE_HIJOS", String)
   PNAEmergency = Column("PNA_EN_CASO_DE_EMERGENCIA", String)
   PNAPhone = Column("TELEFONO_PNA",Integer)
   Policy = Column("POLIZA", String)
   HomeOwn = Column("TENENCIA_VIVIENDA", String)
   LikeTrain = Column("QUE_ES_LO_QUE_LE_GUSTA_FORMARSE", String)
   Height = Column("ALTURA", Float)
   Weight = Column("PESO", Float)
   Smoke = Column("FUMA", String)
   Drink = Column("BEBE", String)
   Sick = Column("A_SUFRIDO_O_SUFRE_DE_ALGUNA_ENFERMEDAD", String)
   ShirtSize = Column("TALLA_DE_CAMISA", String)
   PantSize = Column("TALLA_DE_PANTALONES", String)
   ShoeSize = Column("TALLA_DE_ZAPATOS", String)
   HeightCourse = Column("REQUIERE_CURSO_DE_ALTURAS", String)
   ValidCourse = Column("VIGENCIA_DE_CURSO_DE_ALTURAS", String)

   def FindUser(ID: str):
      engine = create_engine(Settings.Dir_OP(), echo=True)
      Session = sessionmaker(engine)
      session = Session()
      ids = session.query(SQLUser).all()
      session.close()
      for IDD in ids:
         if IDD.Code == ID:
            return (IDD.Name, IDD.Per3)
      return (Settings.Var_KNOW())

   def FindESUser(ID: str):
         engine = create_engine(Settings.Dir_OP(), echo=True)
         Session = sessionmaker(engine)
         session = Session()
         Ref = session.query(SQLUser).all()
         session.close()
         for IDD in Ref:
             if IDD.Code == ID:
                return (IDD.Name, IDD.Per1, IDD.Per2, IDD.Per3, IDD.Per4, IDD.Per5, IDD.Per6, IDD.Per7, IDD.Per8, IDD.Per9, IDD.Per10, IDD.New_Gender, IDD.AreaW,
                   IDD.Position, IDD.Birthday, IDD.TypeB, IDD.Grade, IDD.Profession, IDD.Phone, IDD.Mobile, IDD.EPS, IDD.ARL, IDD.Pensions, IDD.Address, IDD.Neighborhood,
                   IDD.Municipality, IDD.Socioeconomic, IDD.Mail, IDD.NameSP, IDD.Phone2, IDD.Mobile2, IDD.NameC, IDD.PNAEmergency, IDD.PNAPhone, IDD.Policy, IDD.HomeOwn,
                   IDD.LikeTrain, IDD.Height, IDD.Weight, IDD.Smoke, IDD.Drink, IDD.Sick, IDD.ShirtSize, IDD.PantSize, IDD.ShoeSize, IDD.HeightCourse, IDD.ValidCourse)

   def FindAll():
         engine = create_engine(Settings.Dir_OP(), echo=True)
         Session = sessionmaker(engine)
         session = Session()
         Ref = session.query(SQLUser).all()
         session.close()
         New_ID = []
         New_Name = []
         New_Per1 = []
         New_Per2 = []
         New_Per3 = []
         New_Per4 = []
         New_Per5 = []
         New_Per6 = []
         New_Per7 = []
         New_Per8 = []
         New_Per9 = []
         New_Per10 = []
         New_Gender = []
         New_AreaW = []
         New_Position = []
         New_Birthday = []
         New_TypeB = []
         New_Grade = []
         New_Profession = []
         New_Phone = []
         New_Mobile = []
         New_EPS = []
         New_ARL = []
         New_Pensions = []
         New_Address = []
         New_Neighborhood = []
         New_Municipality = []
         New_Socioeconomic = []
         New_Mail = []
         New_NameSP = []
         New_Phone2 = []
         New_Mobile2 = []
         New_NameC = []
         New_PNAEmergency = []
         New_PNAPhone = []
         New_Policy = []
         New_HomeOwn = []
         New_LikeTrain = []
         New_Height = []
         New_Weight = []
         New_Smoke = []
         New_Drink = []
         New_Sick = []
         New_ShirtSize = []
         New_PantSize = []
         New_ShoeSize = []
         NeW_HeightCourse = []
         New_ValidCourse = []
         for IDD in Ref:
             New_ID.append(IDD.Id)
             New_Name.append(IDD.Name)
             New_Per1.append(IDD.Per1)
             New_Per2.append(IDD.Per2)
             New_Per3.append(IDD.Per3)
             New_Per4.append(IDD.Per4)
             New_Per5.append(IDD.Per5)
             New_Per6.append(IDD.Per6)
             New_Per7.append(IDD.Per7)
             New_Per8.append(IDD.Per8)
             New_Per9.append(IDD.Per9)
             New_Per10.append(IDD.Per10)
             New_Gender.append(IDD.Gender)
             New_AreaW.append(IDD.AreaW)
             New_Position.append(IDD.Position)
             New_Birthday.append(IDD.Birthday)
             New_TypeB.append(IDD.TypeB)
             New_Grade.append(IDD.Grade)
             New_Profession.append(IDD.Profession)
             New_Phone.append(IDD.Phone)
             New_Mobile.append(IDD.Mobile)
             New_EPS.append(IDD.EPS)
             New_ARL.append(IDD.ARL)
             New_Pensions.append(IDD.Pensions)
             New_Address.append(IDD.Address)
             New_Neighborhood.append(IDD.Neighborhood)
             New_Municipality.append(IDD.Municipality)
             New_Socioeconomic.append(IDD.Socioeconomic)
             New_Mail.append(IDD.Mail)
             New_NameSP.append(IDD.NameSP)
             New_Phone2.append(IDD.Phone2)
             New_Mobile2.append(IDD.Mobile2)
             New_NameC.append(IDD.NameC)
             New_PNAEmergency.append(IDD.PNAEmergency)
             New_PNAPhone.append(IDD.PNAPhone)
             New_Policy.append(IDD.Policy)
             New_HomeOwn.append(IDD.HomeOwn)
             New_LikeTrain.append(IDD.LikeTrain)
             New_Height.append(IDD.Height)
             New_Weight.append(IDD.Weight)
             New_Smoke.append(IDD.Smoke)
             New_Drink.append(IDD.Drink)
             New_Sick.append(IDD.Sick)
             New_ShirtSize.append(IDD.ShirtSize)
             New_PantSize.append(IDD.PantSize)
             New_ShoeSize.append(IDD.ShoeSize)
             NeW_HeightCourse.append(IDD.HeightCourse)
             New_ValidCourse.append(IDD.ValidCourse)
         return (New_ID, New_Name, New_Per1, New_Per2, New_Per3, New_Per4, New_Per5, New_Per6, New_Per7, New_Per8, New_Per9, New_Per10, New_Gender, New_AreaW,
                   New_Position, New_Birthday, New_TypeB, New_Grade, New_Profession, New_Phone, New_Mobile, New_EPS, New_ARL, New_Pensions, New_Address, New_Neighborhood,
                   New_Municipality, New_Socioeconomic, New_Mail, New_NameSP, New_Phone2, New_Mobile2, New_NameC, New_PNAEmergency, New_PNAPhone, New_Policy, New_HomeOwn,
                   New_LikeTrain, New_Height, New_Weight, New_Smoke, New_Drink, New_Sick, New_ShirtSize, New_PantSize, New_ShoeSize, NeW_HeightCourse, New_ValidCourse)

   def AddUser(code: str, ID: str, name: str, per1: int, per2: int, per3: int, per4: int, per5: int, per6: int, per7: int,
               per8: int, per9: int, per10: int, gender: str, areaW: str, position: str, birthday: str, typeB: str,
               grade: str, profession: str, phone: int, mobile: int, eps: str, arl: str, pensions: str, address: str,
               neighborhood: str, municipality: str, socieconomic: str, mail: str, namesp: str, phone2: int, mobile2: int,
               namec: str, pnaemergency: str, pnaphone: int, policy: str, homeown: str, liketrain: str, height: float,
               weight: float, smoke: str, drink: str, sick: str, shirtsize: str, pantsize: str, shoesize: str,
               heightcourse: str, validcourse: str):
      engine = create_engine(Settings.Dir_OP(), echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session = Session()
      User = SQLUser()
      User.Code = code
      User.Id = ID
      User.Name = name
      User.Per1 = per1
      User.Per2 = per2
      User.Per3 = per3
      User.Per4 = per4
      User.Per5 = per5
      User.Per6 = per6
      User.Per7 = per7
      User.Per8 = per8
      User.Per9 = per9
      User.Per10 = per10
      User.Gender = gender
      User.AreaW = areaW
      User.Position = position
      User.Birthday = birthday
      User.TypeB = typeB
      User.Grade = grade
      User.Profession =profession
      User.Phone = phone
      User.Mobile = mobile
      User.EPS = eps
      User.ARL = arl
      User.Pensions = pensions
      User.Address = address
      User.Neighborhood = neighborhood
      User.Municipality = municipality
      User.Socioeconomic = socieconomic
      User.Mail = mail
      User.NameSP = namesp
      User.Phone2 = phone2
      User.Mobile2 = mobile2
      User.NameC = namec
      User.PNAEmergency = pnaemergency
      User.PNAPhone = pnaphone
      User.Policy = policy
      User.HomeOwn =homeown
      User.LikeTrain = liketrain
      User.Height = height
      User.Weight = weight
      User.Smoke = smoke
      User.Drink = drink
      User.Sick = sick
      User.ShirtSize =shirtsize
      User.PantSize = pantsize
      User.ShoeSize = shoesize
      User.HeightCourse = heightcourse
      User.ValidCourse = validcourse
      session.add(User)
      session.commit()
      session.close()

   def DeleteUser(ID: str):
      engine = create_engine(Settings.Dir_OP(), echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLUser).filter_by(Code=ID).delete()
      session.commit()
      session.close()

   def DeleteALLUser(ID: str):
      engine = create_engine(Settings.Dir_OP(), echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLUser).delete()
      session.commit()
      session.close()

   def UpdateMR(REMISION: str, DATO_MOD, Value):
      engine = create_engine(Settings.Dir_OP(), echo=True)
      Session = sessionmaker(bind=engine)
      session = Session()
      (VID, VName, VPer1, VPer2, VPer3, VPer4, VPer5, VPer6, VPer7, VPer8, VPer9, VPer10, VGender, VAreaW, VPosition, VBirthday,
       VTypeB, VGrade, VProfession, VPhone, VMobile, VEPS, VARL, VPensions, VAddress, VNeighborhood, VMunicipality, VSocioeconomic,
       VMail, VNameSP, VPhone2, VMobile2, VNameC, VPNAEmergency, VPNAPhone, VPolicy, VHomeOwn, VLikeTrain, VHeight, VWeight, VSmoke,
       VDrink, VSick, VShirtSize, VPantSize, VShoeSize, VHeightCourse, VValidCourse) = SQLUser.FindESUser(REMISION)
      if len(VID) > 1:
          return
      if DATO_MOD == SettingsUs.Ref_User1(): session.query(SQLUser).filter_by(Id=VID).update({SQLUser.Id: Value})
      elif DATO_MOD == SettingsUs.Ref_User2(): session.query(SQLUser).filter_by(Name=VName).update({SQLUser.Name: Value})
      elif DATO_MOD == SettingsUs.Ref_User3(): session.query(SQLUser).filter_by(Per1=VPer1).update({SQLUser.Per1: Value})
      elif DATO_MOD == SettingsUs.Ref_User4(): session.query(SQLUser).filter_by(Per2=VPer2).update({SQLUser.Per2: Value})
      elif DATO_MOD == SettingsUs.Ref_User5(): session.query(SQLUser).filter_by(Per3=VPer3).update({SQLUser.Per3: Value})
      elif DATO_MOD == SettingsUs.Ref_User6(): session.query(SQLUser).filter_by(Per4=VPer4).update({SQLUser.Per4: Value})
      elif DATO_MOD == SettingsUs.Ref_User7(): session.query(SQLUser).filter_by(Per5=VPer5).update({SQLUser.Per5: Value})
      elif DATO_MOD == SettingsUs.Ref_User8(): session.query(SQLUser).filter_by(Per6=VPer6).update({SQLUser.Per6: Value})
      elif DATO_MOD == SettingsUs.Ref_User9(): session.query(SQLUser).filter_by(Per7=VPer7).update({SQLUser.Per7: Value})
      elif DATO_MOD == SettingsUs.Ref_User10(): session.query(SQLUser).filter_by(Per8=VPer8).update({SQLUser.Per8: Value})
      elif DATO_MOD == SettingsUs.Ref_User11(): session.query(SQLUser).filter_by(Per9=VPer9).update({SQLUser.Per9: Value})
      elif DATO_MOD == SettingsUs.Ref_User12(): session.query(SQLUser).filter_by(Per10=VPer10).update({SQLUser.Per10: Value})
      elif DATO_MOD == SettingsUs.Ref_User13(): session.query(SQLUser).filter_by(Gender=VGender).update({SQLUser.Gender: Value})
      elif DATO_MOD == SettingsUs.Ref_User14(): session.query(SQLUser).filter_by(AreW=VAreaW).update({SQLUser.AreaW: Value})
      elif DATO_MOD == SettingsUs.Ref_User15(): session.query(SQLUser).filter_by(Position=VPosition).update({SQLUser.Position: Value})
      elif DATO_MOD == SettingsUs.Ref_User16(): session.query(SQLUser).filter_by(Birthday=VBirthday).update({SQLUser.Birthday: Value})
      elif DATO_MOD == SettingsUs.Ref_User17(): session.query(SQLUser).filter_by(TypeB=VTypeB).update({SQLUser.TypeB: Value})
      elif DATO_MOD == SettingsUs.Ref_User18(): session.query(SQLUser).filter_by(Grade=VGrade).update({SQLUser.Grade: Value})
      elif DATO_MOD == SettingsUs.Ref_User19(): session.query(SQLUser).filter_by(Profession=VProfession).update({SQLUser.Profession: Value})
      elif DATO_MOD == SettingsUs.Ref_User20(): session.query(SQLUser).filter_by(Phone=VPhone).update({SQLUser.Phone: Value})
      elif DATO_MOD == SettingsUs.Ref_User21(): session.query(SQLUser).filter_by(Mobile=VMobile).update({SQLUser.Mobile: Value})
      elif DATO_MOD == SettingsUs.Ref_User22(): session.query(SQLUser).filter_by(EPS=VEPS).update({SQLUser.EPS: Value})
      elif DATO_MOD == SettingsUs.Ref_User23(): session.query(SQLUser).filter_by(ARL=VARL).update({SQLUser.ARL: Value})
      elif DATO_MOD == SettingsUs.Ref_User24(): session.query(SQLUser).filter_by(Pensions=VPensions).update({SQLUser.Pensions: Value})
      elif DATO_MOD == SettingsUs.Ref_User25(): session.query(SQLUser).filter_by(Address=VAddress).update({SQLUser.Address: Value})
      elif DATO_MOD == SettingsUs.Ref_User26(): session.query(SQLUser).filter_by(Neighborhood=VNeighborhood).update({SQLUser.Neighborhood: Value})
      elif DATO_MOD == SettingsUs.Ref_User27(): session.query(SQLUser).filter_by(Municipality=VMunicipality).update({SQLUser.Municipality: Value})
      elif DATO_MOD == SettingsUs.Ref_User28(): session.query(SQLUser).filter_by(Socioeconomic=VSocioeconomic).update({SQLUser.Socioeconomic: Value})
      elif DATO_MOD == SettingsUs.Ref_User29(): session.query(SQLUser).filter_by(Mail=VMail).update({SQLUser.Mail: Value})
      elif DATO_MOD == SettingsUs.Ref_User30(): session.query(SQLUser).filter_by(NameSP=VNameSP).update({SQLUser.NameSP: Value})
      elif DATO_MOD == SettingsUs.Ref_User31(): session.query(SQLUser).filter_by(Phone2=VPhone2).update({SQLUser.Phone2: Value})
      elif DATO_MOD == SettingsUs.Ref_User32(): session.query(SQLUser).filter_by(Mobile2=VMobile2).update({SQLUser.Mobile2: Value})
      elif DATO_MOD == SettingsUs.Ref_User33(): session.query(SQLUser).filter_by(NameC=VNameC).update({SQLUser.NameC: Value})
      elif DATO_MOD == SettingsUs.Ref_User34(): session.query(SQLUser).filter_by(PNAEmergency=VPNAEmergency).update({SQLUser.PNAEmergency: Value})
      elif DATO_MOD == SettingsUs.Ref_User35(): session.query(SQLUser).filter_by(PNAPhone=VPNAPhone).update({SQLUser.PNAPhone: Value})
      elif DATO_MOD == SettingsUs.Ref_User36(): session.query(SQLUser).filter_by(Policy=VPolicy).update({SQLUser.Policy: Value})
      elif DATO_MOD == SettingsUs.Ref_User37(): session.query(SQLUser).filter_by(HomeOwn=VHomeOwn).update({SQLUser.HomeOwn: Value})
      elif DATO_MOD == SettingsUs.Ref_User38(): session.query(SQLUser).filter_by(LikeTrain=VLikeTrain).update({SQLUser.LikeTrain: Value})
      elif DATO_MOD == SettingsUs.Ref_User39(): session.query(SQLUser).filter_by(Height=VHeight).update({SQLUser.Height: Value})
      elif DATO_MOD == SettingsUs.Ref_User40(): session.query(SQLUser).filter_by(Weight=VWeight).update({SQLUser.Weight: Value})
      elif DATO_MOD == SettingsUs.Ref_User41(): session.query(SQLUser).filter_by(Smoke=VSmoke).update({SQLUser.Smoke: Value})
      elif DATO_MOD == SettingsUs.Ref_User42(): session.query(SQLUser).filter_by(Drink=VDrink).update({SQLUser.Drink: Value})
      elif DATO_MOD == SettingsUs.Ref_User43(): session.query(SQLUser).filter_by(Sick=VSick).update({SQLUser.Sick: Value})
      elif DATO_MOD == SettingsUs.Ref_User44(): session.query(SQLUser).filter_by(ShirtSize=VShirtSize).update({SQLUser.ShirtSize: Value})
      elif DATO_MOD == SettingsUs.Ref_User45(): session.query(SQLUser).filter_by(PantSize=VPantSize).update({SQLUser.PantSize: Value})
      elif DATO_MOD == SettingsUs.Ref_User46(): session.query(SQLUser).filter_by(ShoeSize=VShoeSize).update({SQLUser.ShoeSize: Value})
      elif DATO_MOD == SettingsUs.Ref_User47(): session.query(SQLUser).filter_by(HeightCourse=VHeightCourse).update({SQLUser.HeightCourse: Value})
      elif DATO_MOD == SettingsUs.Ref_User48(): session.query(SQLUser).filter_by(ValidCourse=VValidCourse).update({SQLUser.ValidCourse: Value})
      session.commit()
      session.close()

   def CreateUser(ID: str):
      engine = create_engine(Settings.Dir_OP(), echo=True)
      Base.metadata.create_all(bind=engine)
