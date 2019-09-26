from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from Settings import Settings

Base = declarative_base()

class SQLToken(Base):
   __tablename__ = 'LINK'
   Token = Column("TOKEN", String, primary_key=True)

   def FindToken():
      engine = create_engine(Settings.Dir_PW(), echo=True)
      Base.metadata.create_all(engine)
      Session = sessionmaker(engine)
      session =Session()
      id = session.query(SQLToken).all()
      session.close()
      for ID in id:
         return ID.Token

   def UpdateToken(TOKEN: str):
      engine = create_engine(Settings.Dir_PW(), echo=True)
      Base.metadata.create_all(bind=engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      ValueToken = SQLToken.FindToken()
      session.query(SQLToken).filter_by(Token=ValueToken).update({SQLToken.Token: TOKEN})
      session.commit()
      session.close()