"""DB actions fro DBUser."""

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
