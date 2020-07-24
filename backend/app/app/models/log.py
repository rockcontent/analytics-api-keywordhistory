from sqlalchemy import Column, Integer, String, Date
from app.db.base_class import Base


class Log(Base):
    id = Column(Integer, primary_key=True, index=True)
    search_data = Column(String, index=True, nullable=False)
    search_type = Column(String, index=True, nullable=False)
    num_rows = Column(Integer, nullable=False, default=0)
    source_response = Column(String, index=True, nullable=False, default=0.0)
    unit_cost = Column(Integer, nullable=False, default=0)
