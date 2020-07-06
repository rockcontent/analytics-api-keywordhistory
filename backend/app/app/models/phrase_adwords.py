from sqlalchemy import Column, Integer, String, DECIMAL

from app.db.base_class import Base


class PhraseAdwords(Base):
    id = Column(Integer, primary_key=True, index=True)
    domain = Column(String, index=True, nullable=False)
    url = Column(String, index=True, nullable=False)
    visible_url = Column(String, index=True, nullable=False)
    keyword = Column(String, index=True, nullable=False)
    database = Column(String, index=True, nullable=False)