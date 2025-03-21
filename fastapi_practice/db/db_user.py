"""DB actions for DBUser."""

from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from fastapi_practice.db.hash import HashService
from fastapi_practice.db.models import DbUser
from fastapi_practice.schemas import UserBase


def create_user(db: Session, request: UserBase) -> DbUser:
    """Create a new user in DB."""
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=HashService.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # to set new ID for the user.

    return new_user


def get_users(db: Session) -> list[DbUser]:
    """Get all users in DB."""
    return db.query(DbUser).all()


def get_user(db: Session, user_id: int) -> DbUser:
    """Get an user by ID."""
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found.",
        )
    return db.query(DbUser).filter(DbUser.id == user_id).first()


def update_user(db: Session, user_id: int, request: UserBase) -> str:
    """Update an user."""
    user = db.query(DbUser).filter(DbUser.id == user_id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found.",
        )
    user.update(
        {
            DbUser.username: request.username,
            DbUser.email: request.email,
            DbUser.password: request.password,
        }
    )
    db.commit()
    return "OK"


def delete_user(db: Session, user_id: int) -> str:
    """Delete an user."""
    user = db.query(DbUser).filter(DbUser.id == user_id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found.",
        )
    user.delete()
    db.commit()
    return "OK"
