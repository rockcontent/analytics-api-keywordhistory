from typing import List, Optional
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session

from sqlalchemy import and_

from app.crud.base import CRUDBase
from app.models.phrase_all import PhraseAll
from app.schemas.phrase_all import PhraseAllCreate, PhraseAllUpdate


class CRUDPhraseAll(CRUDBase[PhraseAll, PhraseAllCreate, PhraseAllUpdate]):
    def get_by_keyword(self, db: Session, *, keyword: str, database: Optional[str] = None) -> List[PhraseAll]:
        if database is not None:
            return (
                db.query(PhraseAll)
                .filter(and_(PhraseAll.keyword == keyword, PhraseAll.database == database))
                .all()
            )
        return (
            db.query(PhraseAll)
            .filter(PhraseAll.keyword == keyword)
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



