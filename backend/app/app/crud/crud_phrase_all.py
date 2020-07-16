from typing import List, Optional
from sqlalchemy import and_
from sqlalchemy.sql import func
from fastapi.encoders import jsonable_encoder
from datetime import datetime, timedelta

from sqlalchemy.orm import Session



from app.crud.base import CRUDBase
from app.models.phrase_all import PhraseAll
from app.schemas.phrase_all import PhraseAllCreate, PhraseAllUpdate


class CRUDPhraseAll(CRUDBase[PhraseAll, PhraseAllCreate, PhraseAllUpdate]):
    def get_by_keyword(self, db: Session, *, keyword: str, database: Optional[str] = None) -> List[PhraseAll]:
        since = datetime.now() - timedelta(days=30)
        return (
            db.query(PhraseAll)
            .filter(and_(PhraseAll.keyword == keyword, PhraseAll.database == database, PhraseAll.date >= since ))
            .all()
        )

    def create(
        self, db: Session, *, obj_in: List[PhraseAllCreate],
    ) -> List[PhraseAll]:
        for p in obj_in:
            obj_in_data = jsonable_encoder(p)
            db_obj = self.model(**obj_in_data)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        return obj_in


phrase_all = CRUDPhraseAll(PhraseAll)



