from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from src.core import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
if not database_exists(engine.url):
    create_database(engine.url)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
