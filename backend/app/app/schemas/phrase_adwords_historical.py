from datetime import date
from pydantic import BaseModel


# Shared properties
class PhraseAdwordsHistorical(BaseModel):
    keyword: str
    domain: str
    date: date
    position: int
    url: str
    title: str
    description: str
    visible_url: str


    class Config:
        orm_mode = True


class PhraseAdwordsHistoricalCreate(PhraseAdwordsHistorical):
    pass


class PhraseAdwordsHistoricalUpdate(PhraseAdwordsHistorical):
    pass

