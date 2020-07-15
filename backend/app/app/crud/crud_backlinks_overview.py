from typing import List, Optional
from sqlalchemy import and_
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.domain_organic import DomainOrganic
from app.schemas.domain_organic import DomainOrganicCreate, DomainOrganicUpdate


class CRUDDomainOrganic(CRUDBase[DomainOrganic, DomainOrganicCreate, DomainOrganicUpdate]):

    def get_by_domain(self, db: Session, *, domain: str, database: Optional[str] = None) -> List[DomainOrganic]:
        return (
            db.query(DomainOrganic)
            .filter(and_(DomainOrganic.domain == domain, DomainOrganic.database == database))
            .all()
        )

    def create(
        self, db: Session, *, obj_in: List[DomainOrganicCreate],
    ) -> List[DomainOrganic]:
        for p in obj_in:
            obj_in_data = jsonable_encoder(p)
            db_obj = self.model(**obj_in_data)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        return obj_in


domain_organic = CRUDDomainOrganic(DomainOrganic)



