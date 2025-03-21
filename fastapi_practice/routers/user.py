"""Router for user."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi_practice.db import db_user
from fastapi_practice.db.database import get_db
from fastapi_practice.db.models import DbUser
from fastapi_practice.schemas import UserBase, UserDisplay

router = APIRouter(prefix="/users", tags=["user"])


@router.post("/new", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)) -> DbUser:
    """Create a new user."""
    return db_user.create_user(db, request)


@router.get("/", response_model=list[UserDisplay])
def get_users(db: Session = Depends(get_db)) -> list[DbUser]:
    """Retrieve all users."""
    return db_user.get_users(db)


@router.get("/{user_id}", response_model=UserDisplay)
def get_user(user_id: int, db: Session = Depends(get_db)) -> DbUser:
    """Retrieve an user."""
    return db_user.get_user(db, user_id)


@router.post("/{user_id}/update")
def update_user(user_id: int, request: UserBase, db: Session = Depends(get_db)) -> str:
    """Update an user."""
    return db_user.update_user(db, user_id, request)


@router.post("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)) -> str:
    """Delete an user."""
    return db_user.delete_user(db, user_id)
