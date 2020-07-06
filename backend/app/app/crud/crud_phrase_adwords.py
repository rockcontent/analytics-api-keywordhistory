from typing import List
from sqlalchemy import and_

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.phrase_adwords import PhraseAdwords
from app.schemas.phrase_adwords import PhraseAdwordsCreate, PhraseAdwordsUpdate


class CRUDPhraseAdwords(CRUDBase[PhraseAdwords, PhraseAdwordsCreate, PhraseAdwordsUpdate]):
    def get_by_keyword(self, db: Session, *, keyword: str, database: str) -> List[PhraseAdwords]:
        return (
            db.query(PhraseAdwords)
            .filter(and_(PhraseAdwords.keyword == keyword, PhraseAdwords.database == database))
            .all()
        )


phrase_adwords = CRUDPhraseAdwords(PhraseAdwords)



