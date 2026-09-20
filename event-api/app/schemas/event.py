from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class EventBase(BaseModel):
    user_id: str = Field(min_length=1, max_length=100)
    event_type: str = Field(min_length=1, max_length=100)
    value: float = Field(ge=0)
    timestamp: datetime


class EventCreate(EventBase):
    event_id: str = Field(min_length=1, max_length=100)


class EventResponse(EventBase):
    model_config = ConfigDict(from_attributes=True)

    event_id: str