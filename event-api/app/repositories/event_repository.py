from typing import Optional

from sqlalchemy.orm import Session

from app.models.event import Event
from app.schemas.event import EventCreate


class EventRepository:
    def __init__(self, database: Session):
        self.database = database

    def find_by_id(self, event_id: str) -> Optional[Event]:
        return (
            self.database.query(Event)
            .filter(Event.event_id == event_id)
            .first()
        )

    def create(self, event_data: EventCreate) -> Event:
        event = Event(**event_data.model_dump())

        self.database.add(event)
        self.database.commit()
        self.database.refresh(event)

        return event