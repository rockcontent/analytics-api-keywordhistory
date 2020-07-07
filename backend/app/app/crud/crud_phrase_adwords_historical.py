from typing import List
from sqlalchemy import and_
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.phrase_adwords_historical import PhraseAdwordsHistorical
from app.schemas.phrase_adwords_historical import PhraseAdwordsHistoricalCreate, PhraseAdwordsHistoricalUpdate


class CRUDPhraseAdwordsHistorical(CRUDBase[PhraseAdwordsHistorical, PhraseAdwordsHistoricalCreate, PhraseAdwordsHistoricalUpdate]):
    def get_by_keyword(self, db: Session, *, keyword: str, database: str) -> List[PhraseAdwordsHistorical]:
        return (
            db.query(PhraseAdwordsHistorical)
            .filter(and_(PhraseAdwordsHistorical.keyword == keyword, PhraseAdwordsHistorical.database == database))
            .all()
        )

    def create(
        self, db: Session, *, obj_in: List[PhraseAdwordsHistoricalCreate],
    ) -> List[PhraseAdwordsHistorical]:
        for p in obj_in:
            obj_in_data = jsonable_encoder(p)
            db_obj = self.model(**obj_in_data)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        return obj_in


phrase_adwords_historical = CRUDPhraseAdwordsHistorical(PhraseAdwordsHistorical)



