from sqlalchemy import Column, Integer, String, Date

from app.db.base_class import Base


class PhraseAdwordsHistorical(Base):
    id = Column(Integer, primary_key=True, index=True)
    database = Column(String, index=True)
    keyword = Column(String, index=True, nullable=False)
    domain = Column(String, index=True, nullable=False)
    date = Column(Date, nullable=False)
    position = Column(Integer, default=0, nullable=False)
    url = Column(String, index=True, nullable=False)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    visible_url = Column(String, index=True, nullable=False)

    def get_unit_value(self):
        return 100