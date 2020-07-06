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
