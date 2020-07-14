from pydantic import BaseModel


# Shared properties
class DomainOrganic(BaseModel):
    keyword: str
    search_volume: int
    cpc: float
    competition: int
    position: int
    previous_position: int
    position_difference: int
    url: str
    traffic: int
    traffic_cost: int
    number_results: int
    trends: int

    class Config:
        orm_mode = True


class DomainOrganicCreate(DomainOrganic):
    pass


class DomainOrganicUpdate(DomainOrganic):
    pass

