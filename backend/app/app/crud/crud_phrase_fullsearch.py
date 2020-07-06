from typing import List
from sqlalchemy import and_

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.phrase_fullsearch import PhraseFullSearch
from app.schemas.phrase_fullsearch import PhraseFullsearchCreate, PhraseFullsearchUpdate


class CRUDPhraseFullsearch(CRUDBase[PhraseFullSearch, PhraseFullsearchCreate, PhraseFullsearchUpdate]):
    def get_by_keyword(self, db: Session, *, keyword: str, database: str) -> List[PhraseFullSearch]:
        return (
            db.query(PhraseFullSearch)
            .filter(and_(PhraseFullSearch.keyword == keyword, PhraseFullSearch.database == database))
            .all()
        )


phrase_fullsearch = CRUDPhraseFullsearch(PhraseFullSearch)



