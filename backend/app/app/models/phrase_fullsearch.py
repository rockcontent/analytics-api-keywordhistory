from sqlalchemy import Column, Integer, String, Date, DECIMAL

from app.db.base_class import Base


class PhraseFullSearch(Base):
    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String, index=True, nullable=False)
    number_results = Column(Integer, nullable=False, default=0)
    cpc = Column(DECIMAL, nullable=False, default=0.0)
    competition = Column(Integer, nullable=False, default=0)
    search_volume = Column(Integer, nullable=False, default=0)
    trends = Column(String, index=True, nullable=True)
    database = Column(String, index=True, nullable=False)