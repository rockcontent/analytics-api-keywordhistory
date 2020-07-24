from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import and_
from datetime import datetime, timedelta

from app.crud.base import CRUDBase
from app.models.backlinks_overview import BacklinksOverview
from app.schemas.backlinks_overview import BacklinksOverviewCreate, BacklinksOverviewUpdate


class CRUDBacklinksOverview(CRUDBase[BacklinksOverview, BacklinksOverviewCreate, BacklinksOverviewUpdate]):

    def get_by_domain(self, db: Session, *, domain: str, target: Optional[str] = None) -> List[BacklinksOverview]:
        since = datetime.now() - timedelta(days=30)
        if target is None:
            return (
                db.query(BacklinksOverview)
                .filter(and_(BacklinksOverview.domain == domain, BacklinksOverview.created_at >= since))
                .all()
            )
        return (
            db.query(BacklinksOverview)
                .filter(and_(BacklinksOverview.domain == domain, BacklinksOverview.target==target, BacklinksOverview.created_at >= since))
                .all()
        )

    # def create(
    #     self, db: Session, *, obj_in: List[BacklinksOverviewCreate],
    # ) -> List[BacklinksOverview]:
    #     for p in obj_in:
    #         obj_in_data = jsonable_encoder(p)
    #         db_obj = self.model(**obj_in_data)
    #         db.add(db_obj)
    #         db.commit()
    #         db.refresh(db_obj)
    #     return obj_in


backlinks_overview = CRUDBacklinksOverview(BacklinksOverview)



