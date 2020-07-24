from typing import List, Optional
from sqlalchemy import and_
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.crud.base import CRUDBase
from app.models.domain_domains import DomainDomains
from app.schemas.domain_domains import DomainDomainsCreate, DomainDomainsUpdate


class CRUDDomainDomains(CRUDBase[DomainDomains, DomainDomainsCreate, DomainDomainsUpdate]):


    def get_by_domains(self, db: Session, *, domains: str, database: Optional[str] = None) -> List[DomainDomains]:
        since = datetime.now() - timedelta(days=30)
        return (
            db.query(DomainDomains)
            .filter(and_(DomainDomains.domains_query == domains, DomainDomains.database == database, DomainDomains.created_at >= since))
            .all()
        )

    # def create(
    #     self, db: Session, *, obj_in: List[DomainDomainsCreate],
    # ) -> List[DomainDomains]:
    #     for p in obj_in:
    #         obj_in_data = jsonable_encoder(p)
    #         db_obj = self.model(**obj_in_data)
    #         db.add(db_obj)
    #         db.commit()
    #         db.refresh(db_obj)
    #     return obj_in


domain_domains = CRUDDomainDomains(DomainDomains)



