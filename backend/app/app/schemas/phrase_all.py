from typing import Optional
from datetime import date, datetime, time, timedelta

from pydantic import BaseModel


# Shared properties
class PhraseAll(BaseModel):
    date: date
    database: str
    keyword: str
    search_volume: int
    cpc: str
    competition: int

    class Config:
        orm_mode = True


class PhraseAllCreate(PhraseAll):
    pass


class PhraseAllUpdate(PhraseAll):
    pass

