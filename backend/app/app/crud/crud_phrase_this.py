from typing import List
from sqlalchemy import and_

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.phrase_this import PhraseThis
from app.schemas.phrase_this import PhraseThisCreate, PhraseThisUpdate


class CRUDPhraseThis(CRUDBase[PhraseThis, PhraseThisCreate, PhraseThisUpdate]):
    def get_by_keyword(self, db: Session, *, keyword: str, database: str) -> List[PhraseThis]:
        return (
            db.query(PhraseThis)
            .filter(and_(PhraseThis.keyword == keyword, PhraseThis.database == database))
            .all()
        )


phrase_this = CRUDPhraseThis(PhraseThis)



