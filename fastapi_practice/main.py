"""Main app."""

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse, PlainTextResponse, RedirectResponse

from fastapi_practice.db import models
from fastapi_practice.db.database import engine
from fastapi_practice.exceptions import StoryException
from fastapi_practice.routers import article, blog, user

app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(article.router)


@app.get("/", include_in_schema=False)
def index() -> dict:
    """Redirect to swagger and hide the endpoint from swagger."""
    return RedirectResponse("/docs")


@app.exception_handler(StoryException)
def story_exception_handler(exc: StoryException) -> JSONResponse:
    """Handle StoryException."""
    return JSONResponse(status_code=418, content={"detail": exc.name})


@app.exception_handler(HTTPException)
def custom_handler(exc: StoryException) -> PlainTextResponse:
    """Default handle of Exception."""
    return PlainTextResponse(str(exc), status_code=status.HTTP_400_BAD_REQUEST)


models.Base.metadata.create_all(engine)
