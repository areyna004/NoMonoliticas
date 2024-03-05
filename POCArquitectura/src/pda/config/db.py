from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = None
SessionLocal = None

def init_db():
    global engine, SessionLocal, Base
    if not engine:
        engine = create_engine('mysql+pymysql://root:U6yEZgrAjc6c1olP@34.66.105.29:3306/db-propiedades')
    if not SessionLocal:
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return engine, SessionLocal, Base
