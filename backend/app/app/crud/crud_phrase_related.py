from typing import List
from sqlalchemy import and_

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.phrase_related import PhraseRelated
from app.schemas.phrase_related import PhraseRelatedCreate, PhraseRelatedUpdate


class CRUDPhraseRelated(CRUDBase[PhraseRelated, PhraseRelatedCreate, PhraseRelatedUpdate]):
    def get_by_keyword(self, db: Session, *, keyword: str, database: str) -> List[PhraseRelated]:
        return (
            db.query(PhraseRelated)
            .filter(and_(PhraseRelated.keyword == keyword, PhraseRelated.database == database))
            .all()
        )


phrase_related = CRUDPhraseRelated(PhraseRelated)



