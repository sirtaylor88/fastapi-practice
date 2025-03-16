"""Module defining DB schemas."""

from typing import Optional

from pydantic import BaseModel


class Image(BaseModel):
    """Image schema."""

    url: str
    alias: str


class Blog(BaseModel):
    """Blog schema."""

    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
    tags: list[str] = []
    metadata: dict[str, str] = {"key1": "val1"}
    image: Optional[Image] = None


class UserBase(BaseModel):
    """User schema."""

    username: str
    email: str
    password: str
