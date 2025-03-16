"""Module defining DB schemas."""

from typing import Optional

from pydantic import BaseModel


class Image(BaseModel):
    """Model for Image."""

    url: str
    alias: str


class Blog(BaseModel):
    """Model for Blog."""

    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
    tags: list[str] = []
    metadata: dict[str, str] = {"key1": "val1"}
    image: Optional[Image] = None
