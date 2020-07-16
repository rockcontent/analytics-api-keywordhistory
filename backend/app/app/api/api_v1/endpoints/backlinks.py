from typing import Any, List

from python_semrush.semrush import SemrushClient
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.config import settings

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

client = SemrushClient(key=settings.TOKEN_SEMRUSH)


@router.get("/backlinks_overview/{domain}/{target}",
            response_model=List[schemas.backlinks_overview.BacklinksOverview],
            description="This report provides a summary of backlinks, including their type, referring "
                        "domains and IP addresses for a domain, root domain, or URL.")
async def backlinks_overview(
        domain: str,
        target: str,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db)
) -> Any:

    backlinks_ovreview_data = crud.backlinks_overview.get_by_domain(db, domain=domain, target=target)

    if len(backlinks_ovreview_data) > 0:
        return backlinks_ovreview_data
    else:
        response = []
        backlinks = await client.backlinks_overview(domain, target)

        for b in backlinks:
            bk = {'domain': domain,
                  'target': target,
                  'total': int(b.get('total')),
                  'domains_num': int(b.get('domains_num')),
                  'ips_num': int(b.get('ips_num')),
                  'follows_num': int(b.get('follows_num')),
                  'nofollows_num': int(b.get('nofollows_num')),
                  'score': int(b.get('score')),
                  'trust_score': int(b.get('trust_score')),
                  'urls_num': int(b.get('urls_num')),
                  'ipclassc_num': int(b.get('ipclassc_num')),
                  'texts_num': int(b.get('texts_num')),
                  'forms_num': int(b.get('forms_num')),
                  'frames_num': int(b.get('frames_num')),
                  'images_num': int(b.get('images_num'))
            }

            response.append(bk)

        crud.backlinks_overview.create(db=db, obj_in=response)
        return response