"""Router for blogs."""

from typing import Optional

from fastapi import APIRouter, Body, Path, Query, Response, status

from constants import BlogType
from fastapi_practice.schemas import Blog

router = APIRouter(prefix="/blogs", tags=["blog"])


# GET
@router.get(
    "/",
    summary="Retrieve all blogs",
    description="Fetching all blogs.",
    response_description="The lsit of available blogs.",
)
def get_all_blogs(page_size: Optional[int] = None, page_number: int = 1) -> dict:
    """Endpoint to get all blogs."""
    return {"message": f"All {page_size} blogs provided on page {page_number}."}


@router.get("/type/{blog_type}")
def get_blogs_by_type(blog_type: BlogType) -> dict:
    """Endpoint to get all blogs by the provided type."""
    return {"message": f"All blogs with type `{blog_type.value}.`"}


@router.get("/{blog_id}/comments/{comment_id}", tags=["comment"])
def get_comment_from_blog(
    blog_id: int, comment_id: int, valid: bool = True, username: Optional[str] = None
) -> dict:
    """Endpoint to get a comment from a blog."""
    return {
        "message": (
            f"Comment {comment_id}, blog {blog_id}, valid {valid}, username {username}."
        )
    }


@router.get("/{blog_id}", status_code=status.HTTP_200_OK)
def get_blog(blog_id: int, response: Response) -> dict:
    """Endpoint to get a blog based on its ID."""
    if blog_id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog ID {blog_id} not found!"}
    return {"message": f"Blog with id {blog_id}."}


# POST
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
