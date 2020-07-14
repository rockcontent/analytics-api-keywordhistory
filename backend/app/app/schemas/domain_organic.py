from pydantic import BaseModel


# Shared properties
class DomainDomains(BaseModel):
    domain: str
    keyword: str
    search_volume: int
    cpc: str
    competition: int

    class Config:
        orm_mode = True


class DomainDomainsCreate(DomainDomains):
    pass


class DomainDomainsUpdate(DomainDomains):
    pass

