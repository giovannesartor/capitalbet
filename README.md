# Capital Bet

Plataforma de análise esportiva avançada e simulação de apostas (não reais).

## Stack
- Backend: Python, FastAPI, PostgreSQL, Redis
- Frontend: Next.js, Tailwind CSS

## Setup Local
1. Backend:
   - `cd backend`
   - `pip install -r requirements.txt`
   - Set env vars: DATABASE_URL, REDIS_URL, API_FUTEBOL_KEY, API_FOOTBALL_KEY, JWT_SECRET
   - `uvicorn app.main:app --reload`
2. Frontend:
   - `cd frontend`
   - `npm install`
   - `npm run dev`

## Deploy no Railway
- Crie app, anexe Postgres e Redis.
- Defina vars de ambiente.
- Deploy backend e frontend separadamente ou como monorepo.

Aviso: Não apostas reais.
