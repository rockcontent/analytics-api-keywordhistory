from pydantic import BaseModel


# Shared properties
class UrlOrganic(BaseModel):
    keyword: str
    search_volume: int
    cpc: float
    competition: int
    position: int
    url: str
    traffic: int
    traffic_cost: int
    number_results: int
    trends: int

    class Config:
        orm_mode = True


class UrlOrganicCreate(UrlOrganic):
    pass


class UrlOrganicUpdate(UrlOrganic):
    pass

