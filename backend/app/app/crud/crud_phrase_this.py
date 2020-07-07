from typing import List
from sqlalchemy import and_
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.phrase_this import PhraseThis
from app.schemas.phrase_this import PhraseThisCreate, PhraseThisUpdate


class CRUDPhraseThis(CRUDBase[PhraseThis, PhraseThisCreate, PhraseThisUpdate]):
    def get_by_keyword(self, db: Session, *, keyword: str, database: str) -> List[PhraseThis]:
        return (
            db.query(PhraseThis)
            .filter(and_(PhraseThis.keyword == keyword, PhraseThis.database == database))
            .all()
        )

    def create(
        self, db: Session, *, obj_in: List[PhraseThisCreate],
    ) -> List[PhraseThis]:
        for p in obj_in:
            obj_in_data = jsonable_encoder(p)
            db_obj = self.model(**obj_in_data)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        return obj_in


phrase_this = CRUDPhraseThis(PhraseThis)



