from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.phrase_all import PhraseAll
from app.schemas.phrase_all import PhraseAllCreate, PhraseAllUpdate


class CRUDPhraseAll(CRUDBase[PhraseAll, PhraseAllCreate, PhraseAllUpdate]):
    def get_by_keyword(self, db: Session, *, keyword: str) -> List[PhraseAll]:
        return (
            db.query(PhraseAll)
            .filter(PhraseAll.keyword == keyword)
            .all()
        )


phrase_all = CRUDPhraseAll(PhraseAll)



