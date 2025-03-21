"""DB actions for DbArticle."""

from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from fastapi_practice.db.models import DbArticle
from fastapi_practice.exceptions import StoryException
from fastapi_practice.schemas import ArticleBase


def create_article(db: Session, request: ArticleBase) -> DbArticle:
    """Create a new article in DB."""
    if request.content.startswith("Once upon a time"):
        raise StoryException("No stories please.")

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
    article = db.query(DbArticle).filter(DbArticle.id == article_id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id {article_id} not found.",
        )
    return article
