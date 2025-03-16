"""Main app."""

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from fastapi_practice.routers import blog_get, blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/", include_in_schema=False)
def index() -> dict:
    """Redirect to swagger and hide the endpoint from swagger."""
    return RedirectResponse("/docs")
