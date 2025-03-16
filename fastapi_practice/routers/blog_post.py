"""Router for blog using POST method."""

from fastapi import APIRouter

router = APIRouter(prefix="/blog", tags=["blog"])


@router.post("/create")
def create_blog() -> dict:
    """Endpoint to gcreate a blog."""
    pass
