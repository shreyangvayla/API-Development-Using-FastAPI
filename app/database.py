from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:9997@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)  # Establish connection

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi',
#                                 user='postgres', password='9997', cursor_factory=RealDictCursor)  # For Database Connection
#         cursor = conn.cursor()  # execute sequel statement
#         print("Database connection was successfull!")
#         break
#     except Exception as error:
#         print("Connecting to database faied")
#         print("Error: ", error)
#         time.sleep(2)
