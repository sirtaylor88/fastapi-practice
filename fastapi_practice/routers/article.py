"""Router for article."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi_practice.db import db_article
from fastapi_practice.db.database import get_db
from fastapi_practice.db.models import DbArticle
from fastapi_practice.schemas import ArticleBase, ArticleDisplay

router = APIRouter(prefix="/articles", tags=["article"])


@router.post("/new", response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)) -> DbArticle:
    """Create a new article."""
    return db_article.create_article(db, request)


@router.get("/{article_id}", response_model=ArticleDisplay)
def get_article(article_id: int, db: Session = Depends(get_db)) -> DbArticle:
    """Retrieve an article."""
    return db_article.get_article(db, article_id)
