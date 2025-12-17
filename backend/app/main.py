from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes_matches, routes_odds, routes_stats, routes_simulator, routes_chat
from app.database.session import engine
from app.database.base import Base
from app.services.api_football import fetch_daily_fixtures
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI(title="Capital Bet API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(routes_matches.router, prefix="/matches")
app.include_router(routes_odds.router, prefix="/odds")
app.include_router(routes_stats.router, prefix="/stats")
app.include_router(routes_simulator.router, prefix="/simulator")
app.include_router(routes_chat.router, prefix="/chat")

# Create DB tables
Base.metadata.create_all(bind=engine)

# Health check
@app.get("/health")
def health():
    return {"status": "healthy"}

# Scheduler for data updates
scheduler = BackgroundScheduler()
scheduler.add_job(fetch_daily_fixtures, 'interval', hours=1)  # Example job
scheduler.start()

@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()