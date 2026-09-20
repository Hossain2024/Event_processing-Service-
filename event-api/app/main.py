from fastapi import FastAPI

from app.database import Base, engine
from app.models.event import Event
from app.routers.events import router as events_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Event Processing API",
    version="1.0.0"
)

app.include_router(events_router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}