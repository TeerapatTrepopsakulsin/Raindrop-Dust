"""Database connection."""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

load_dotenv()
DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Get the database connection/session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
