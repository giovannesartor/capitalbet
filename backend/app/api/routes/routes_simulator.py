from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.bet import Bet
from app.models.user import User
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class BetInput(BaseModel):
    fixture_id: int
    market: str
    amount: float
    odd: float

router = APIRouter()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    user = db.query(User).filter(User.id == payload["sub"]).first()
    return user

@router.post("/place")
async def place_bet(bet: BetInput, user = Depends(get_current_user), db: Session = Depends(get_db)):
    if user.balance < bet.amount:
        raise ValueError("Insufficient balance")
    new_bet = Bet(user_id=user.id, **bet.dict(), status="pending")
    db.add(new_bet)
    user.balance -= bet.amount
    db.commit()
    return {"success": True}

@router.get("/history")
async def history(user = Depends(get_current_user), db: Session = Depends(get_db)):
    bets = db.query(Bet).filter(Bet.user_id == user.id).all()
    roi = calculate_roi(bets)  # Implement
    return {"bets": bets, "roi": roi, "balance": user.balance}

# Add register/login routes for auth
@router.post("/register")
async def register(user_data: dict, db: Session = Depends(get_db)):
    # Hash password, create user with balance=1000
    pass

@router.post("/login")
async def login(credentials: dict, db: Session = Depends(get_db)):
    # Verify, return JWT
    pass