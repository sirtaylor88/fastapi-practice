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


class ArticleBase(BaseModel):
    """Base Article schema for validation."""

    title: str
    content: str
    published: bool
    creator_id: int


class Article(BaseModel):
    """Article Schema for display in relationship."""

    title: str
    content: str
    published: bool

    class Config:
        """Configuration."""

        orm_mode = True


class User(BaseModel):
    """User schema for display in a relationship"""

    id: int
    username: str

    class Config:
        """Configuration."""

        orm_mode = True


class ArticleDisplay(BaseModel):
    """Article schema for individual display."""

    title: str
    content: str
    published: bool
    user: User

    class Config:
        """Configuration."""

        orm_mode = True


class UserBase(BaseModel):
    """Base User schema for validation."""

    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    """User schema for individual display."""

    username: str
    email: str
    items: list[Article] = []

    class Config:
        """Configuration."""

        orm_mode = True  # enable auto-conversion from DbUser model.
