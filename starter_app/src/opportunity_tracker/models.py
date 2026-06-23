from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, Field

OpportunityStatus = Literal["idea", "applied", "interview", "offer", "closed"]


class OpportunityCreate(BaseModel):
    """Input model for a new opportunity."""

    title: str = Field(..., min_length=2, examples=["LinkedIn AI internship"])
    source: str = Field(..., min_length=2, examples=["LinkedIn"])
    status: OpportunityStatus = "idea"
    deadline: date | None = None
    notes: str | None = None


class OpportunityOut(OpportunityCreate):
    """Output model returned by the API."""

    id: int
    created_at: datetime


class StatusUpdate(BaseModel):
    """Input model for changing an opportunity status."""

    status: OpportunityStatus
