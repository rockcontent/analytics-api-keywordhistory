from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class BacklinksOverview(Base):
    id = Column(Integer, primary_key=True, index=True)
    domain = Column(String, index=True, nullable=False)
    total = Column(Integer, nullable=False, default=0)
    domains_num = Column(Integer, nullable=False, default=0)
    ips_num = Column(Integer, nullable=False, default=0)
    follows_num = Column(Integer, nullable=False, default=0)
    nofollows_num = Column(Integer, nullable=False, default=0)
    score = Column(Integer, nullable=False, default=0)
    trust_score = Column(Integer, nullable=False, default=0)
    urls_num = Column(Integer, nullable=False, default=0)
    ipclassc_num = Column(Integer, nullable=False, default=0)
    texts_num = Column(Integer, nullable=False, default=0)
    forms_num = Column(Integer, nullable=False, default=0)
    frames_num = Column(Integer, nullable=False, default=0)
    images_num = Column(Integer, nullable=False, default=0)

