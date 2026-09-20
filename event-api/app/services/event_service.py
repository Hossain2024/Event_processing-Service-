from fastapi import HTTPException, status

from app.models.event import Event
from app.repositories.event_repository import EventRepository
from app.schemas.event import EventCreate


class EventService:
    def __init__(self, repository: EventRepository):
        self.repository = repository

    def create_event(self, event_data: EventCreate) -> Event:
        existing_event = self.repository.find_by_id(
            event_data.event_id
        )

        if existing_event:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="An event with this ID already exists"
            )

        return self.repository.create(event_data)

    def get_event(self, event_id: str) -> Event:
        event = self.repository.find_by_id(event_id)

        if event is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Event not found"
            )

        return event