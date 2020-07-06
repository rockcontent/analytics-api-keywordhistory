from typing import List
from sqlalchemy import and_

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


phrase_adwords_historical = CRUDPhraseAdwordsHistorical(PhraseAdwordsHistorical)



