"""Router for user."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi_practice.db import db_user
from fastapi_practice.db.database import get_db
from fastapi_practice.schemas import UserBase, UserDisplay

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/new", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    """Create a new user."""
    return db_user.create_user(db, request)
