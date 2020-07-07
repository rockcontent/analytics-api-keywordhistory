from typing import List
from sqlalchemy import and_
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.phrase_related import PhraseRelated
from app.schemas.phrase_related import PhraseRelatedCreate, PhraseRelatedUpdate


class CRUDPhraseRelated(CRUDBase[PhraseRelated, PhraseRelatedCreate, PhraseRelatedUpdate]):
    def get_by_keyword(self, db: Session, *, keyword: str, database: str) -> List[PhraseRelated]:
        return (
            db.query(PhraseRelated)
            .filter(and_(PhraseRelated.keyword_search == keyword, PhraseRelated.database == database))
            .all()
        )

    def create(
        self, db: Session, *, obj_in: List[PhraseRelatedCreate],
    ) -> List[PhraseRelated]:
        for p in obj_in:
            obj_in_data = jsonable_encoder(p)
            db_obj = self.model(**obj_in_data)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        return obj_in

phrase_related = CRUDPhraseRelated(PhraseRelated)



