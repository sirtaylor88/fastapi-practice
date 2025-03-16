"""Main app."""

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from fastapi_practice.db import models
from fastapi_practice.db.database import engine
from fastapi_practice.routers import blog, user

app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)


@app.get("/", include_in_schema=False)
def index() -> dict:
    """Redirect to swagger and hide the endpoint from swagger."""
    return RedirectResponse("/docs")


models.Base.metadata.create_all(engine)
