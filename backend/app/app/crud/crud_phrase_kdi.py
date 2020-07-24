from typing import List
from sqlalchemy import and_
from fastapi.encoders import jsonable_encoder
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.phrase_kdi import PhraseKdi
from app.schemas.phrase_kdi import PhraseKdiCreate, PhraseKdiUpdate


class CRUDPhraseKdi(CRUDBase[PhraseKdi, PhraseKdiCreate, PhraseKdiUpdate]):
    def get_by_keyword(self, db: Session, *, keyword: str, database: str) -> List[PhraseKdi]:
        since = datetime.now() - timedelta(days=30)
        return (
            db.query(PhraseKdi)
            .filter(and_(PhraseKdi.keyword == keyword,
                         PhraseKdi.database == database,
                         PhraseKdi.created_at >= since))
            .all()
        )

    # def create(
    #     self, db: Session, *, obj_in: List[PhraseKdiCreate],
    # ) -> List[PhraseKdi]:
    #     for p in obj_in:
    #         obj_in_data = jsonable_encoder(p)
    #         db_obj = self.model(**obj_in_data)
    #         db.add(db_obj)
    #         db.commit()
    #         db.refresh(db_obj)
    #     return obj_in


phrase_kdi = CRUDPhraseKdi(PhraseKdi)



