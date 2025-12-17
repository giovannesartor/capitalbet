from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.database.base import Base

class Bet(Base):
    __tablename__ = "bets"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    fixture_id = Column(Integer)
    market = Column(String)
    amount = Column(Float)
    odd = Column(Float)
    status = Column(String)  # pending, won, lost
    outcome = Column(Float)  # profit/loss