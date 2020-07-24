from sqlalchemy import Column, Integer, String, DECIMAL, BigInteger

from app.db.base_class import Base


class PhraseThis(Base):
    id = Column(Integer, primary_key=True, index=True)
    database = Column(String, index=True)
    keyword = Column(String, index=True, nullable=False)
    search_volume = Column(Integer, nullable=False, default=0)
    cpc = Column(DECIMAL, nullable=False, default=0.0)
    competition = Column(Integer, nullable=False, default=0)
    number_results = Column(BigInteger, nullable=False, default=0)

    def get_unit_value(self):
        return 10
