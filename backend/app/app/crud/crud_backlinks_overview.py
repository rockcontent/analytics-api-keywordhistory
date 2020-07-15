from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.backlinks_overview import BacklinksOverview
from app.schemas.backlinks_overview import BacklinksOverviewCreate, BacklinksOverviewUpdate


class CRUDBacklinksOverview(CRUDBase[BacklinksOverview, BacklinksOverviewCreate, BacklinksOverviewUpdate]):

    def get_by_domain(self, db: Session, *, domain: str) -> List[BacklinksOverview]:
        return (
            db.query(BacklinksOverview)
            .filter(BacklinksOverview.domain == domain)
            .all()
        )

    def create(
        self, db: Session, *, obj_in: List[BacklinksOverviewCreate],
    ) -> List[BacklinksOverview]:
        for p in obj_in:
            obj_in_data = jsonable_encoder(p)
            db_obj = self.model(**obj_in_data)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        return obj_in


backlinks_overview = CRUDBacklinksOverview(BacklinksOverview)



