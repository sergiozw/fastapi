from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'


SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:postgres@localhost:5432/dad_db2'


SQLALCHEMY_DATABASE_URL = 'postgresql://drqprjkfyuafzh:6a051c96bd983aacadc9d459201e9a28b080c6e6c6ffdc15ff2fd61a16e6a9d3@ec2-3-230-199-240.compute-1.amazonaws.com:5432/d1j26patssms9f'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()




# while True:

#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
#                                 password='password123', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)
