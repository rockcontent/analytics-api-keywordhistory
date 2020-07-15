from typing import Any, List

from python_semrush.semrush import SemrushClient
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.config import settings

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

client = SemrushClient(key=settings.TOKEN_SEMRUSH)


@router.get("/domain_domains/{domains}/{database}",
            response_model=List[schemas.domain_domains.DomainDomains],
            description="This report allows users to compare up to five domains by common keywords, "
                        "unique keywords, all keywords, or search terms that are unique to the "
                        "first domain.")
async def domain_domains(
        domains: str,
        database: str,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db)
) -> Any:

    domain_domains_data = crud.domain_domains.get_by_domains(db, domains=domains, database=database)

    if len(domain_domains_data) > 0:
        return domain_domains_data
    else:
        response = []
        domains = await client.domain_domains(domains, database=database)

        for d in domains:
            dm = {
                'database': database,
                'keyword': d.get('Keyword').encode('utf8'),
                'search_volume': int(d.get('Search Volume')),
                'cpc': d.get('CPC'),
                'competition': float(d.get('Competition')),
                'domains_query': domains
            }
            response.append(dm)

        crud.domain_domains.create(db=db, obj_in=response)
        return response


@router.get("/domain_organic/{domain}/{database}",
            response_model=List[schemas.domain_domains.DomainDomains],
            description="This report allows users to compare up to five domains by common keywords, "
                        "unique keywords, all keywords, or search terms that are unique to the "
                        "first domain.")
async def domain_organic(
        domain: str,
        database: str,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db)
) -> Any:

    domain_organic_data = crud.domain_organic.get_by_domain(db, domain=domain, database=database)

    if len(domain_organic_data) > 0:
        return domain_organic_data
    else:
        response = []
        domains = await client.domain_organic(domain, database=database)

        for d in domains:
            dm = {
                'domain': domain,
                'database': database,
                'keyword': d.get('Keyword').encode('utf8'),
                'position': int(d.get('Position')),
                'previous_position': int(d.get('Previous Position')),
                'position_difference': int(d.get('Position Difference')),
                'search_volume': int(d.get('Search Volume')),
                'cpc': d.get('CPC'),
                'competition': float(d.get('Competition')),
                'url': d.get('Url'),
                'traffic': float(d.get('Traffic (%)')),
                'traffic_cost': float(d.get('Traffic Cost (%)')),
                'number_results': int(d.get('Number of Results')),
                'trends': d.get('Trends')
            }
            response.append(dm)

        crud.domain_organic.create(db=db, obj_in=response)
        return response