from typing import Any, List, Optional
from datetime import datetime

from python_semrush.semrush import SemrushClient
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.config import settings

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

client = SemrushClient(key=settings.TOKEN_SEMRUSH)


@router.get("/phrase_all/{keyword}/{database}",
            response_model=List[schemas.phrase_all.PhraseAll],
            description="This report provides a summary of a keyword, including its volume, CPC, "
                        "competition, and the number of results in all regional databases.")
async def phrase_all(
        keyword: str,
        database: str,
        display_limit: int = None,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db)
) -> Any:

    async def update_from_serp_api(db, keyword, database, **kwargs):
        response = []
        keywords = await client.phrase_all(keyword, database=database, **kwargs)

        for k in keywords:
            kw = {
                'date': str(datetime.strptime(k.get('Date'), '%Y%m%d').date()),
                'database': k.get('Database'),
                'keyword': k.get('Keyword').encode('utf8'),
                'search_volume': int(k.get('Search Volume')),
                'cpc': k.get('CPC'),
                'competition': float(k.get('Competition'))
            }
            response.append(kw)

        crud.phrase_all.delete_by_keyword(db, keyword=keyword, database=database)
        crud.phrase_all.create(db=db, obj_in=response)
        return response


    phrase_all_data = crud.phrase_all.get_by_keyword(db, keyword=keyword, database=database)
    if display_limit:
        if len(phrase_all_data) >= display_limit:
            return phrase_all_data[:display_limit]
        else:
            return await update_from_serp_api(db, keyword, database, display_limit=display_limit)
    else:
        if len(phrase_all_data) > 0:
            return phrase_all_data
        else:
            return await update_from_serp_api(db, keyword, database)
    

@router.get("/phrase_organic/{keyword}/{database}",
            response_model=List[schemas.phrase_organic.PhraseOrganic],
            description="This report lists domains that are ranking in Google"
                        " top 100 organic search results with a requested keyword.")
async def phrase_organic(
        keyword: str,
        database: str,
        display_limit: int = None,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db),
) -> Any:

    async def update_from_serp_api(db, keyword, database, **kwargs):
        response = []

        keywords = await client.phrase_organic(keyword, database, **kwargs)
        for k in keywords:
            kw = {
                'keyword': keyword,
                'domain': k.get('Domain'),
                'url': k.get('Url'),
                'database': database
            }
            response.append(kw)

        crud.phrase_organic.delete_by_keyword(db, keyword=keyword, database=database)
        crud.phrase_organic.create(db, obj_in=response)
        return response

    phrase_organic_data = crud.phrase_organic.get_by_keyword(db, keyword=keyword, database=database)

    if display_limit:
        if len(phrase_organic_data) >= display_limit:
            return phrase_organic_data[:display_limit]
        else:
            return await update_from_serp_api(db, keyword, database, display_limit=display_limit)
    else:
        if len(phrase_organic_data) > 0:
            return phrase_organic_data
        else:
            return await update_from_serp_api(db, keyword, database)

@router.get("/phrase_this/{keyword}/{database}",
            response_model=List[schemas.phrase_this.PhraseThis],
            description="This report provides a summary of a keyword, including its volume, "
                        "CPC, competition, and the number of results in a chosen regional database.")
async def phrase_this(
        keyword: str,
        database: str,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db),
) -> Any:

    phrase_this_data = crud.phrase_this.get_by_keyword(db, keyword=keyword, database=database)

    if len(phrase_this_data) > 0:
        return phrase_this_data
    else:
        response = []
        keywords = await client.phrase_this(keyword, database)
        for k in keywords:
            kw = {
                'keyword': k.get('Keyword'),
                'search_volume': int(k.get('Search Volume')),
                'cpc': float(k.get('CPC')),
                'competition': float(k.get('Competition')),
                'number_results': int(k.get('Number of Results')),
                'database': database
            }
            response.append(kw)

        crud.phrase_this.create(db, obj_in=response)
        return response


@router.get("/phrase_related/{keyword}/{database}",
            response_model=List[schemas.phrase_related.PhraseRelated],
            description="This report provides an extended list of related keywords, synonyms, "
                        "and variations relevant to a queried term in a chosen database.")
async def phrase_related(
        keyword: str,
        database: str,
        display_limit: int = None,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db),
) -> Any:

    async def update_from_serp_api(db, keyword, database, **kwargs):
        response = []
        keywords = await client.phrase_related(keyword, database, **kwargs)

        for k in keywords:
            kw = {
                'keyword': k.get('Keyword'),
                'number_results': int(k.get('Number of Results')),
                'cpc': float(k.get('CPC')),
                'competition': float(k.get('Competition')),
                'search_volume': int(k.get('Search Volume')),
                'trends': k.get('Trends'),
                'related_relevance': float(k.get('Related Relevance')),
                'database': database,
                'keyword_search': keyword
            }
            response.append(kw)

        crud.phrase_related.delete_by_keyword(db, keyword=keyword, database=database)
        crud.phrase_related.create(db, obj_in=response)
        return response

    phrase_related_data = crud.phrase_related.get_by_keyword(db, keyword=keyword, database=database)

    if display_limit:
        if len(phrase_related_data) >= display_limit:
            return phrase_related_data[:display_limit]
        else:
            return await update_from_serp_api(db, keyword, database, display_limit=display_limit)
    else:
        if len(phrase_related_data) > 0:
            return phrase_related_data
        else:
            return await update_from_serp_api(db, keyword, database)


@router.get("/phrase_fullsearch/{keyword}/{database}",
            response_model=List[schemas.phrase_fullsearch.PhraseFullsearch],
            description="The report provides a list of broad matches and alternate search queries, "
                        "including particular keywords or keyword expressions.")
async def phrase_fullsearch(
        keyword: str,
        database: str,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db),
) -> Any:

    phrase_fullsearch_data = crud.phrase_fullsearch.get_by_keyword(db, keyword=keyword, database=database)

    if len(phrase_fullsearch_data) > 0:
        return phrase_fullsearch_data
    else:
        response = []
        keywords = await client.phrase_fullsearch(keyword, database)

        for k in keywords:
            kw = {
                'keyword': k.get('Keyword'),
                'number_results': int(k.get('Number of Results')),
                'cpc': float(k.get('CPC')),
                'competition': float(k.get('Competition')),
                'search_volume': int(k.get('Search Volume')),
                'trends': k.get('Trends'),
                'database': database,
                'keyword_search': keyword
            }
            response.append(kw)
        return crud.phrase_fullsearch.create(db, obj_in=response)

    return phrase_fullsearch_data


@router.get("/phrase_adwords/{keyword}/{database}",
            response_model=List[schemas.phrase_adwords.PhraseAdwords],
            description="This report lists a domain’s competitors in paid search results.")
async def phrase_adwords(
        keyword: str,
        database: str,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db),
) -> Any:

    phrase_adwords_data = crud.phrase_adwords.get_by_keyword(db, keyword=keyword, database=database)

    if len(phrase_adwords_data) > 0:
        return phrase_adwords_data
    else:
        response = []
        keywords = await client.phrase_adwords(keyword, database)

        for k in keywords:
            kw = {
                'domain': k.get('Domain'),
                'visible_url': k.get('Visible Url'),
                'keyword': keyword,
                'database': database
            }
            response.append(kw)
        return crud.phrase_adwords.create(db, obj_in=response)


@router.get("/phrase_adwords_historical/{keyword}/{database}",
            response_model=List[schemas.phrase_adwords_historical.PhraseAdwordsHistorical],
            description="This report shows keywords a domain has bid on in the "
                        "last 12 months and its positions in paid search results.")
async def phrase_adwords_historical(
        keyword: str,
        database: str,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db),
) -> Any:

    phrase_adwords_historical_data = crud.phrase_adwords_historical.get_by_keyword(db, keyword=keyword, database=database)

    if len(phrase_adwords_historical_data) > 0:
        return phrase_adwords_historical_data
    else:
        response = []
        keywords = await client.phrase_adwords_historical(keyword, database)

        for k in keywords:
            kw = {
                'domain': k.get('Domain'),
                'date': str(datetime.strptime(k.get('Date'), '%Y%m%d').date()),
                'position': int(k.get('Position')),
                'url': k.get('Url'),
                'title': k.get('Title'),
                'description': k.get('Description'),
                'visible_url': k.get('Visible Url'),
                'keyword': keyword
            }
            response.append(kw)
        return crud.phrase_adwords_historical.create(db, obj_in=response)


@router.get("/phrase_kdi/{keyword}/{database}",
            response_model=List[schemas.phrase_kdi.PhraseKdi],
            description="This report provides keyword difficulty, an index that helps to "
                        "estimate how difficult it would be to seize competitors' positions in "
                        "organic search within the Google top 100 with an indicated search term.")
async def phrase_kdi(
        keyword: str,
        database: str,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db),
) -> Any:

    phrase_kdi_data = crud.phrase_kdi.get_by_keyword(db, keyword=keyword, database=database)

    if len(phrase_kdi_data) > 0:
        return phrase_kdi_data
    else:
        response = []
        keywords = await client.phrase_kdi(keyword, database)

        for k in keywords:
            kw = {
                'keyword': k.get('Keyword'),
                'keyword_difficulty_index': float(k.get('Keyword Difficulty Index')),
                'database': database
            }
            response.append(kw)
        return crud.phrase_kdi.create(db, obj_in=response)
