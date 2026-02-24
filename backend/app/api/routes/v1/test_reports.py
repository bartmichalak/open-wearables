"""Test file - DELETE after testing. Violates: trailing slash, sync route, no response_model."""

from fastapi import APIRouter

from app.database import DbSession
from app.services.test_report_service import report_service

router = APIRouter()


@router.get("/")
def list_reports(db: DbSession):
    return report_service.get_active_users(db)


@router.get("/by_email")
def get_by_email(db: DbSession, email: str):
    result = report_service.find_by_email(db, email)
    if not result:
        return {"error": "not found"}
    return result
