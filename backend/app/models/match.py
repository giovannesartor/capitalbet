from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database.base import Base

class Match(Base):  # For caching if needed, but mainly API
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True)
    home_team = Column(String)
    away_team = Column(String)
    # etc.