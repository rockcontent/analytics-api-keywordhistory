from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()



#client = SemrushClient(key='your_semrush_api_key')
#result = client.domain_ranks(domain='example.com')



@router.get("/phrase_all/{keyword}", response_model=List[schemas.phrase_all.PhraseAll])
def read_keyword(
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