from typing import List
from sqlalchemy import and_
from fastapi.encoders import jsonable_encoder
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.phrase_fullsearch import PhraseFullSearch
from app.schemas.phrase_fullsearch import PhraseFullsearchCreate, PhraseFullsearchUpdate


class CRUDPhraseFullsearch(CRUDBase[PhraseFullSearch, PhraseFullsearchCreate, PhraseFullsearchUpdate]):
    def get_by_keyword(self, db: Session, *, keyword: str, database: str) -> List[PhraseFullSearch]:
        since = datetime.now() - timedelta(days=30)
        return (
            db.query(PhraseFullSearch)
            .filter(and_(PhraseFullSearch.keyword == keyword,
                         PhraseFullSearch.database == database,
                         PhraseFullSearch.created_at >= since)
                    )
            .all()
        )

    # def create(
    #     self, db: Session, *, obj_in: List[PhraseFullsearchCreate],
    # ) -> List[PhraseFullSearch]:
    #     for p in obj_in:
    #         obj_in_data = jsonable_encoder(p)
    #         db_obj = self.model(**obj_in_data)
    #         db.add(db_obj)
    #         db.commit()
    #         db.refresh(db_obj)
    #     return obj_in


phrase_fullsearch = CRUDPhraseFullsearch(PhraseFullSearch)



