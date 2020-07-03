from sqlalchemy import Column, Integer, String, Date, DECIMAL

from app.db.base_class import Base


class PhraseOrganic(Base):
    id = Column(Integer, primary_key=True, index=True)
    database = Column(String, index=True)
    keyword = Column(String, index=True, nullable=False)
    domain = Column(String, index=True, nullable=False)
    url = Column(String, index=True, nullable=False)
