from sqlalchemy import Column, Integer, String, DECIMAL

from app.db.base_class import Base


class PhraseKdi(Base):
    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String, index=True, nullable=False)
    keyword_difficulty_index = Column(DECIMAL, default=0.0)
    database = Column(String, nullable=False)

    def get_unit_value(self):
        return 50