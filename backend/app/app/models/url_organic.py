from sqlalchemy import Column, Integer, String, DECIMAL, BigInteger

from app.db.base_class import Base


class UrlOrganic(Base):
    id = Column(Integer, primary_key=True, index=True)
    database = Column(String, index=True)
    keyword = Column(String, index=True)
    search_volume = Column(Integer, nullable=False, default=0)
    cpc = Column(DECIMAL, nullable=False, default=0.0)
    competition = Column(Integer, nullable=False, default=0)
    position = Column(Integer, nullable=False, default=0)
    url = Column(String, nullable=False)
    traffic = Column(DECIMAL, nullable=False, default=0.0)
    traffic_cost = Column(DECIMAL, nullable=False, default=0.0)
    number_results = Column(BigInteger, nullable=False, default=0)
    trends = Column(String, index=True, nullable=False)
    serp_features = Column(String, nullable=False, default=0)

    def get_unit_value(self):
        return 10