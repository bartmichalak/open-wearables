"""Test file - DELETE after testing. Violates: Pydantic v1 syntax."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


# Violation: using class Config instead of model_config = ConfigDict(from_attributes=True)
class ReportRead(BaseModel):
    class Config:
        orm_mode = True

    id: UUID
    title: str
    created_at: datetime


# Violation: using class Config instead of ConfigDict
class ReportCreate(BaseModel):
    class Config:
        schema_extra = {"example": {"title": "Monthly report"}}

    title: str
