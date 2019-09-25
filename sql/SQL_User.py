from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker

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
      engine = create_engine('sqlite:///lib/OP.db', echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      ids = session.query(SQLUser).all()
      session.close()
      for IDD in ids:
         if IDD.Code == ID:
            return (IDD.Name, IDD.Per3)
      return ('No encontrado', 0)

   def AddUser(code: str,
               ID: str,
               name: str,
               per1: int,
               per2: int,
               per3: int,
               per4: int,
               per5: int,
               per6: int,
               per7: int,
               per8: int,
               per9: int,
               per10: int,
               gender: str,
               areaW: str,
               position: str,
               birthday: str,
               typeB: str,
               grade: str,
               profession: str,
               phone: int,
               mobile: int,
               eps: str,
               arl: str,
               pensions: str,
               address: str,
               neighborhood: str,
               municipality: str,
               socieconomic: str,
               mail: str,
               namesp: str,
               phone2: int,
               mobile2: int,
               namec: str,
               pnaemergency: str,
               pnaphone: int,
               policy: str,
               homeown: str,
               liketrain: str,
               height: float,
               weight: float,
               smoke: str,
               drink: str,
               sick: str,
               shirtsize: str,
               pantsize: str,
               shoesize: str,
               heightcourse: str,
               validcourse: str
               ):
      engine = create_engine('sqlite:///lib/OP.db', echo=True)
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
      engine = create_engine('sqlite:///lib/OP.db', echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      session.query(SQLUser).filter_by(Code = ID).delete()
      session.commit()
      session.close()
