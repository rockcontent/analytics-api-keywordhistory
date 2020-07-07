from datetime import date

from pydantic import BaseModel


# Shared properties
class PhraseOrganic(BaseModel):
    domain: str
    url: str
    keyword: str

    class Config:
        orm_mode = True


class PhraseOrganicCreate(PhraseOrganic):
    pass


class PhraseOrganicUpdate(PhraseOrganic):
    pass

