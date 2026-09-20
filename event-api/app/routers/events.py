from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_database
from app.repositories.event_repository import EventRepository
from app.schemas.event import EventCreate, EventResponse
from app.services.event_service import EventService


router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


def get_event_service(
    database: Session = Depends(get_database)
) -> EventService:
    repository = EventRepository(database)
    return EventService(repository)


@router.post(
    "",
    response_model=EventResponse,
    status_code=status.HTTP_201_CREATED
)
def create_event(
    event_data: EventCreate,
    service: EventService = Depends(get_event_service)
):
    return service.create_event(event_data)


@router.get(
    "/{event_id}",
    response_model=EventResponse
)
def get_event(
    event_id: str,
    service: EventService = Depends(get_event_service)
):
    return service.get_event(event_id)