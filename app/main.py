"""FastAPI application entrypoint."""

from fastapi import FastAPI

app = FastAPI(title="daily-bible-share", version="0.1.0")


@app.get("/")
def read_root() -> dict[str, str]:
    """Return a short message for the root endpoint."""
    return {"message": "daily-bible-share API"}


@app.get("/health")
def read_health() -> dict[str, str]:
    """Return a simple service health payload."""
    return {
        "status": "ok",
        "service": "daily-bible-share",
        "version": "0.1.0",
    }
