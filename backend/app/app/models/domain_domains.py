from sqlalchemy import Column, Integer, String, Date, DECIMAL

from app.db.base_class import Base


class DomainDomains(Base):
    id = Column(Integer, primary_key=True, index=True)
    database = Column(String, index=True)
    keyword = Column(String, index=True, nullable=False)
    domains_query = Column(String, index=True, nullable=False)
    domain = Column(String, index=True, nullable=False)
    search_volume = Column(Integer, nullable=False, default=0)
    cpc = Column(DECIMAL, nullable=False, default=0.0)
    competition = Column(Integer, nullable=False, default=0)

    def get_unit_value(self):
        return 80