# Define the User model
from models.base import Base
from sqlalchemy import create_engine, Column, TEXT, VARCHAR, LargeBinary
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    
    id = Column(TEXT, primary_key=True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100), unique=True, index=True)
    password = Column(LargeBinary)

    favorites = relationship('Favorite', back_populates= 'user')