from datetime import datetime

from sqlalchemy import DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Event(Base):
	__tablename__ = "events"

	event_id: Mapped[str] = mapped_column(String(100), primary_key=True)
	user_id: Mapped[str] = mapped_column(String(100), nullable=False)
	event_type: Mapped[str] = mapped_column(String(100), nullable=False)
	value: Mapped[float] = mapped_column(Float, nullable=False)
	timestamp: Mapped[datetime] = mapped_column(DateTime, nullable=False)
