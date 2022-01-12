from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.settings import settings


engine = create_engine(settings.db_url)
Session = sessionmaker(bind=engine)


Base = declarative_base()


