from datetime import date
from pydantic import BaseModel


# Shared properties
class PhraseRelated(BaseModel):
    keyword: str
    number_results: int
    cpc: float
    competition: int
    search_volume: int
    trends: str
    related_relevance: float

    class Config:
        orm_mode = True


class PhraseRelatedCreate(PhraseRelated):
    pass


class PhraseRelatedUpdate(PhraseRelated):
    pass

