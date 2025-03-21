"""DB actions for DbArticle."""

from sqlalchemy.orm.session import Session

from fastapi_practice.db.models import DbArticle
from fastapi_practice.schemas import ArticleBase


def create_article(db: Session, request: ArticleBase) -> DbArticle:
    """Create a new article in DB."""
    new_article = DbArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id,
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)

    return new_article


def get_article(db: Session, article_id: int) -> DbArticle:
    """Get an article by ID."""
    return db.query(DbArticle).filter(DbArticle.id == article_id).first()
