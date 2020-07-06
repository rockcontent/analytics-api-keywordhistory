from typing import List
from sqlalchemy import and_

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.phrase_organic import PhraseOrganic
from app.schemas.phrase_organic import PhraseOrganicCreate, PhraseOrganicUpdate


class CRUDPhraseOrganic(CRUDBase[PhraseOrganic, PhraseOrganicCreate, PhraseOrganicUpdate]):
    def get_by_keyword(self, db: Session, *, keyword: str, database: str) -> List[PhraseOrganic]:
        return (
            db.query(PhraseOrganic)
            .filter(and_(PhraseOrganic.keyword == keyword, PhraseOrganic.database == database))
            .all()
        )


phrase_organic = CRUDPhraseOrganic(PhraseOrganic)



