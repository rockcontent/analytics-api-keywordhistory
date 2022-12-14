from sqlalchemy import Column, Integer, String, Date, DECIMAL, BigInteger

from app.db.base_class import Base


class PhraseFullSearch(Base):
    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String, index=True, nullable=False)
    number_results = Column(BigInteger, nullable=False, default=0)
    cpc = Column(DECIMAL, nullable=False, default=0.0)
    competition = Column(Integer, nullable=False, default=0)
    search_volume = Column(Integer, nullable=False, default=0)
    trends = Column(String, index=True, nullable=True)
    database = Column(String, index=True, nullable=False)
    keyword_search = Column(String, index=True, nullable=False)

    def get_unit_value(self):
        return 20