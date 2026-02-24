"""Test file - DELETE after testing. Violates: direct DB in service, no AppService pattern."""

from sqlalchemy import select

from app.database import DbSession
from app.models.user import User
from app.schemas.user import UserRead


class ReportService:
    """Violation: not extending AppService, doing direct DB queries, returning Pydantic."""

    def get_active_users(self, db: DbSession) -> list[UserRead]:
        results = db.execute(select(User)).scalars().all()
        return [UserRead.model_validate(u) for u in results]

    def count_users(self, db: DbSession) -> int:
        stmt = select(User)
        return db.execute(stmt).scalars().all().__len__()

    def find_by_email(self, db: DbSession, email: str) -> UserRead | None:
        user = db.execute(select(User).where(User.email == email)).scalar_one_or_none()
        if user:
            return UserRead.model_validate(user)
        return None


report_service = ReportService()
