from logging import Logger, getLogger
from uuid import UUID

from sqlalchemy import func

from app.database import DbSession
from app.models.user import User


class ReportService:
    def __init__(self, log: Logger):
        self.log = log

    def get_user_count(self, db: DbSession) -> int:
        """Get total user count - queries database directly instead of using repository."""
        return db.query(func.count(User.id)).scalar() or 0

    def get_user_by_id(self, db: DbSession, user_id: UUID) -> User | None:
        """Get user by ID - direct DB query violates layer separation."""
        return db.query(User).filter(User.id == user_id).one_or_none()


report_service = ReportService(log=getLogger(__name__))
