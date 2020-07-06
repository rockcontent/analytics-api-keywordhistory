from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


# client = SemrushClient(key='your_semrush_api_key')
# result = client.domain_ranks(domain='example.com')


@router.get("/phrase_all/{keyword}",
            response_model=List[schemas.phrase_all.PhraseAll],
            description="This report provides a summary of a keyword, including its volume, CPC, "
                        "competition, and the number of results in all regional databases.")
async def phrase_all(
        keyword: str,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    phrase_all = crud.phrase_all.get_by_keyword(db, keyword=keyword)

    if phrase_all is None:
        raise HTTPException(
            status_code=400, detail="The keyword doesn't exist"
        )
    return phrase_all


@router.get("/phrase_organic/{keyword}/{database}",
            response_model=List[schemas.phrase_organic.PhraseOrganic],
            description="This report lists domains that are ranking in Google"
                        " top 100 organic search results with a requested keyword.")
async def phrase_organic(
        keyword: str,
        database: str,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    phrase_organic = crud.phrase_organic.get_by_keyword(db, keyword=keyword, database=database)

    if phrase_organic is None:
        raise HTTPException(
            status_code=400, detail="The keyword doesn't exist"
        )
    return phrase_organic


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
    """
    Get a specific user by id.
    """
    phrase_this = crud.phrase_this.get_by_keyword(db, keyword=keyword, database=database)

    if phrase_this is None:
        raise HTTPException(
            status_code=400, detail="The keyword doesn't exist"
        )
    return phrase_this


@router.get("/phrase_related/{keyword}/{database}",
            response_model=List[schemas.phrase_related.PhraseRelated],
            description="This report provides an extended list of related keywords, synonyms, "
                        "and variations relevant to a queried term in a chosen database.")
async def phrase_related(
        keyword: str,
        database: str,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    phrase_related = crud.phrase_related.get_by_keyword(db, keyword=keyword, database=database)

    if phrase_related is None:
        raise HTTPException(
            status_code=400, detail="The keyword doesn't exist"
        )
    return phrase_related


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
    """
    Get a specific user by id.
    """
    phrase_fullsearch = crud.phrase_fullsearch.get_by_keyword(db, keyword=keyword, database=database)

    if phrase_fullsearch is None:
        raise HTTPException(
            status_code=400, detail="The keyword doesn't exist"
        )
    return phrase_fullsearch


@router.get("/phrase_adwords/{keyword}/{database}",
            response_model=List[schemas.phrase_adwords.PhraseAdwords],
            description="This report lists a domain’s competitors in paid search results.")
async def phrase_adwords(
        keyword: str,
        database: str,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    phrase_adwords = crud.phrase_adwords.get_by_keyword(db, keyword=keyword, database=database)

    if phrase_adwords is None:
        raise HTTPException(
            status_code=400, detail="The keyword doesn't exist"
        )
    return phrase_adwords


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
    """
    Get a specific user by id.
    """
    phrase_adwords_historical = crud.phrase_adwords_historical.get_by_keyword(db, keyword=keyword, database=database)

    if phrase_adwords_historical is None:
        raise HTTPException(
            status_code=400, detail="The keyword doesn't exist"
        )
    return phrase_adwords_historical


@router.get("/phrase_kdi/{keyword}/{database}",
            response_model=List[schemas.phrase_kdi.PhraseKdi],
            description="This report provides keyword difficulty, an index that helps to "
                        "estimate how difficult it would be to seize competitors' positions in "
                        "organic search within the Google top 100 with an indicated search term.")
async def phrase_adwords_kdi(
        keyword: str,
        database: str,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    phrase_kdi = crud.phrase_kdi.get_by_keyword(db, keyword=keyword, database=database)

    if phrase_kdi is None:
        raise HTTPException(
            status_code=400, detail="The keyword doesn't exist"
        )
    return phrase_kdi

