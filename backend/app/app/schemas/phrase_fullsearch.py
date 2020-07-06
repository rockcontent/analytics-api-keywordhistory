from datetime import date
from pydantic import BaseModel


# Shared properties
class PhraseFullsearch(BaseModel):
    keyword: str
    number_results: int
    cpc: float
    competition: int
    search_volume: int
    trends: str

    class Config:
        orm_mode = True


class PhraseFullsearchCreate(PhraseFullsearch):
    pass


class PhraseFullsearchUpdate(PhraseFullsearch):
    pass

