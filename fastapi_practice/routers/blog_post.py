"""Router for blog using POST method."""

from typing import Optional

from fastapi import APIRouter, Body, Path, Query

from fastapi_practice.models import Blog

router = APIRouter(prefix="/blog", tags=["blog"])


@router.post("/new")
def create_blog(blog: Blog, blog_id: int, version: int = 1) -> dict:
    """Endpoint to create a blog."""

    return {
        "id": blog_id,
        "data": blog,
        "version": version,
    }


@router.post("/new/{blog_id}/comment/{comment_id}")
def create_comment(
    blog: Blog,
    blog_id: int,
    comment_title: int = Query(
        None,
        title="Comment title",
        description="Comment description",
        alias="commentId",
        deprecated=True,
    ),  # metadata
    comment_id: int = Path(gt=5, le=10),
    content: str = Body(
        ..., min_length=10, max_length=50, regex=r"^[a-z\s]*$"
    ),  # require a string with at least 10 chars
    v: Optional[list[str]] = Query(["1.0", "1.1", "1.2"]),
) -> dict:
    """Endpoint to create a blog comment."""

    return {
        "blog": blog,
        "blog_id": blog_id,
        "comment_title": comment_title,
        "comment_id": comment_id,
        "content": content,
        "version": v,
    }
