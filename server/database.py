from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine


DATABASE_URL = 'postgresql://postgres:123321@localhost:5432/fluttermusicapp'

# Create database engine and session
engine = create_engine(DATABASE_URL) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():  
    db = SessionLocal()
    try:
        yield db
    finally:
         db.close()    
