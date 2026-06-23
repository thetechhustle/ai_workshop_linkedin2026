from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Query, status

from opportunity_tracker.db import create_opportunity, get_opportunity, init_db, list_opportunities, update_opportunity_status
from opportunity_tracker.models import OpportunityCreate, OpportunityOut, OpportunityStatus, StatusUpdate


@asynccontextmanager
async def lifespan(_app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Opportunity Tracker API",
    description="FastAPI and SQLite starter app for the LinkedIn AI Workshop.",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Opportunity Tracker API", "docs": "/docs", "health": "/health"}


@app.get("/health")
def health() -> dict[str, str]:
    init_db()
    return {"status": "ok", "service": "opportunity-tracker"}


@app.post("/opportunities", response_model=OpportunityOut, status_code=status.HTTP_201_CREATED)
def create(payload: OpportunityCreate) -> dict:
    return create_opportunity(payload.model_dump())


@app.get("/opportunities", response_model=list[OpportunityOut])
def list_all(status_filter: OpportunityStatus | None = Query(default=None, alias="status")) -> list[dict]:
    return list_opportunities(status=status_filter)


@app.get("/opportunities/{opportunity_id}", response_model=OpportunityOut)
def get_one(opportunity_id: int) -> dict:
    opportunity = get_opportunity(opportunity_id)
    if opportunity is None:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return opportunity


@app.patch("/opportunities/{opportunity_id}/status", response_model=OpportunityOut)
def update_status(opportunity_id: int, payload: StatusUpdate) -> dict:
    opportunity = update_opportunity_status(opportunity_id, payload.status)
    if opportunity is None:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return opportunity
