from typing import Any, List

from python_semrush.semrush import SemrushClient
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.config import settings

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

client = SemrushClient(key=settings.TOKEN_SEMRUSH)


@router.get("/url_organic/",
            response_model=List[schemas.url_organic.UrlOrganic],
            description="This report lists keywords that bring users "
                        "to a URL via Google top 100 organic search results.")
async def url_organic(
        url: str,
        database: str,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db)
) -> Any:

    url_organic_data = crud.url_organic.get_by_domain(db, url=url, database=database)

    if len(url_organic_data) > 0:
        return url_organic_data
    else:
        response = []
        urls = await client.url_organic(url, database=database)

        for u in urls:
            ur = {
                'url': url,
                'database': database,
                'keyword': u.get('Keyword').encode('utf8'),
                'position': int(u.get('Position')),
                'search_volume': int(u.get('Search Volume')),
                'cpc': u.get('CPC'),
                'competition': float(u.get('Competition')),
                'traffic': float(u.get('Traffic (%)')),
                'traffic_cost': float(u.get('Traffic Cost (%)')),
                'number_results': int(u.get('Number of Results')),
                'trends': u.get('Trends'),
                'serp_features': u.get('SERP Features')
            }
            response.append(ur)

        crud.url_organic.create(db=db, obj_in=response)
        return response
