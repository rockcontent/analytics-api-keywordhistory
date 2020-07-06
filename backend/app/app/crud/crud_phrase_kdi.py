from typing import List
from sqlalchemy import and_

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.phrase_kdi import PhraseKdi
from app.schemas.phrase_kdi import PhraseKdiCreate, PhraseKdiUpdate


class CRUDPhraseKdi(CRUDBase[PhraseKdi, PhraseKdiCreate, PhraseKdiUpdate]):
    def get_by_keyword(self, db: Session, *, keyword: str, database: str) -> List[PhraseKdi]:
        return (
            db.query(PhraseKdi)
            .filter(and_(PhraseKdi.keyword == keyword, PhraseKdi.database == database))
            .all()
        )


phrase_kdi = CRUDPhraseKdi(PhraseKdi)



