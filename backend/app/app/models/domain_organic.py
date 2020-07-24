from sqlalchemy import Column, Integer, String, DECIMAL, BigInteger

from app.db.base_class import Base


class DomainOrganic(Base):
    id = Column(Integer, primary_key=True, index=True)
    database = Column(String, index=True)
    keyword = Column(String, index=True)
    domain = Column(String, index=True, nullable=False)
    search_volume = Column(Integer, nullable=False, default=0)
    cpc = Column(DECIMAL, nullable=False, default=0.0)
    competition = Column(Integer, nullable=False, default=0)
    position = Column(Integer, nullable=False, default=0)
    previous_position = Column(Integer, nullable=False, default=0)
    position_difference = Column(Integer, nullable=False, default=0)
    url = Column(String, nullable=False)
    traffic = Column(DECIMAL, nullable=False, default=0.0)
    traffic_cost = Column(DECIMAL, nullable=False, default=0.0)
    number_results = Column(BigInteger, nullable=False, default=0)
    trends = Column(String, index=True, nullable=False)

    def get_unit_value(self):
        return 10