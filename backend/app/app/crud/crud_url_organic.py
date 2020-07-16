from typing import List, Optional
from sqlalchemy import and_
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.url_organic import UrlOrganic
from app.schemas.url_organic import UrlOrganicCreate, UrlOrganicUpdate
from datetime import datetime, timedelta

class CRUDUrlOrganic(CRUDBase[UrlOrganic, UrlOrganicCreate, UrlOrganicUpdate]):

    def get_by_domain(self, db: Session, *, url: str, database: str) -> List[UrlOrganic]:
        since = datetime.now() - timedelta(days=30)
        return (
            db.query(UrlOrganic)
            .filter(and_(UrlOrganic.url == url,
                         UrlOrganic.database == database,
                         UrlOrganic.created_at >= since)
                    )
            .all()
        )

    def create(
        self, db: Session, *, obj_in: List[UrlOrganicCreate],
    ) -> List[UrlOrganic]:
        for p in obj_in:
            obj_in_data = jsonable_encoder(p)
            db_obj = self.model(**obj_in_data)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        return obj_in


url_organic = CRUDUrlOrganic(UrlOrganic)



