from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import psycopg2

#lee la url de las variables de entorno que definimos en el docker-compose
#en caso de no encontrarla, usa una url por defecto
DATABASE_URL =os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://user:password@localhost/dbname"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()