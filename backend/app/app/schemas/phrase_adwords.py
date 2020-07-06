from pydantic import BaseModel


# Shared properties
class PhraseAdwords(BaseModel):
    keyword: str
    domain: str
    visible_url: str

    class Config:
        orm_mode = True


class PhraseAdwordsCreate(PhraseAdwords):
    pass


class PhraseAdwordsUpdate(PhraseAdwords):
    pass

