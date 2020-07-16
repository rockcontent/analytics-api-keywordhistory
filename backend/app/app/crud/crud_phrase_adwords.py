from typing import List
from sqlalchemy import and_
from fastapi.encoders import jsonable_encoder
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.phrase_adwords import PhraseAdwords
from app.schemas.phrase_adwords import PhraseAdwordsCreate, PhraseAdwordsUpdate


class CRUDPhraseAdwords(CRUDBase[PhraseAdwords, PhraseAdwordsCreate, PhraseAdwordsUpdate]):
    def get_by_keyword(self, db: Session, *, keyword: str, database: str) -> List[PhraseAdwords]:
        since = datetime.now() - timedelta(days=30)
        return (
            db.query(PhraseAdwords)
            .filter(and_(PhraseAdwords.keyword == keyword,
                         PhraseAdwords.database == database,
                         PhraseAdwords.created_at >= since)
                    )
            .all()
        )

    def create(
        self, db: Session, *, obj_in: List[PhraseAdwordsCreate],
    ) -> List[PhraseAdwords]:
        for p in obj_in:
            obj_in_data = jsonable_encoder(p)
            db_obj = self.model(**obj_in_data)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        return obj_in


phrase_adwords = CRUDPhraseAdwords(PhraseAdwords)



