"""Defining app DB models."""

from sqlalchemy import Column, Integer, String

from fastapi_practice.db.database import Base


class DbUser(Base):
    """Database user."""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
