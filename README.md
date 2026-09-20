# Event Processing Service

A small FastAPI service for accepting and querying user activity events.

## Run locally

```bash
python -m pip install -r requirements.txt
uvicorn Service.eventservice:app --reload
```

Open the interactive API documentation at `http://localhost:8000/docs`.

## API

- `POST /events` stores an event with `user_id`, `event_type`, and optional `payload`.
- `GET /events` lists events and supports `user_id` and `event_type` filters.
- `GET /events/{event_id}` retrieves one event.
- `GET /stats` returns total events, unique users, and counts by event type.
- `GET /health` provides a health check.

The repository is intentionally in-memory for this first version. The MVC boundaries make it straightforward to replace `EventRepository` with a database-backed implementation without changing the HTTP layer.
