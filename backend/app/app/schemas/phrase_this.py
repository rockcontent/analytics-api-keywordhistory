from datetime import date

from pydantic import BaseModel


# Shared properties
class PhraseThis(BaseModel):
    keyword: str
    search_volume: int
    cpc: float
    competition: int
    number_results: int

    class Config:
        orm_mode = True


class PhraseThisCreate(PhraseThis):
    pass


class PhraseThisUpdate(PhraseThis):
    pass

