from sqlalchemy import Column, Integer, String, Date, DECIMAL, BigInteger

from app.db.base_class import Base


class PhraseRelated(Base):
    id = Column(Integer, primary_key=True, index=True)
    number_results = Column(BigInteger, nullable=False, default=0)
    cpc = Column(DECIMAL, nullable=False, default=0.0)
    competition = Column(Integer, nullable=False, default=0)
    search_volume = Column(Integer, nullable=False, default=0)
    keyword = Column(String, index=True, nullable=False)
    database = Column(String, index=True)
    trends = Column(String, index=True, nullable=True)
    related_relevance = Column(DECIMAL, index=False, default=0.0)
    keyword_search = Column(String, index=True, nullable=False)
