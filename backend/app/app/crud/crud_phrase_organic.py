from typing import List
from sqlalchemy import and_
from fastapi.encoders import jsonable_encoder
from datetime import timedelta, datetime

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.phrase_organic import PhraseOrganic
from app.schemas.phrase_organic import PhraseOrganicCreate, PhraseOrganicUpdate


class CRUDPhraseOrganic(CRUDBase[PhraseOrganic, PhraseOrganicCreate, PhraseOrganicUpdate]):
    def get_by_keyword(self, db: Session, *, keyword: str, database: str) -> List[PhraseOrganic]:
        since = datetime.now() - timedelta(days=30)
        return (
            db.query(PhraseOrganic)
            .filter(and_(PhraseOrganic.keyword == keyword,
                         PhraseOrganic.database == database,
                         PhraseOrganic.created_at >= since))
            .all()
        )


    def delete_by_keyword(self, db: Session, *, keyword: str, database: str) -> bool:
        return (
            db.query(PhraseOrganic)
            .filter(and_(PhraseOrganic.keyword == keyword, PhraseOrganic.database == database))
            .delete()
        )

phrase_organic = CRUDPhraseOrganic(PhraseOrganic)



