from sqlalchemy import Column, Integer, String, Float
from app.database.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password_hash = Column(String)
    balance = Column(Float, default=1000.0)