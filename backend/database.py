import os

from sqlalchemy import create_engine, func, text

from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from utils import DELETE_1, GROUP_HOURLY_SQL_STATEMENT
Base = declarative_base()

load_dotenv()
DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL,echo=True)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try :
        db.execute(text(DELETE_1))
        db.commit()
        db.execute(text(GROUP_HOURLY_SQL_STATEMENT))
        db.commit()
        yield db
    finally:
        db.close()
