from pydantic import BaseModel


# Shared properties
class BacklinksOverview(BaseModel):
    total: int
    domains_num: int
    ips_num: int
    follows_num: int
    nofollows_num: int
    score: int
    trust_score: int
    urls_num: int
    ipclassc_num: int
    texts_num: int
    forms_num: int
    frames_num: int
    images_num: int

    class Config:
        orm_mode = True


class BacklinksOverviewCreate(BacklinksOverview):
    pass


class BacklinksOverviewUpdate(BacklinksOverview):
    pass

