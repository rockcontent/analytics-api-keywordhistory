from datetime import date
from pydantic import BaseModel


# Shared properties
class PhraseKdi(BaseModel):
    keyword: str
    keyword_dificult_index: float

    class Config:
        orm_mode = True


class PhraseKdiCreate(PhraseKdi):
    pass


class PhraseKdiUpdate(PhraseKdi):
    pass

