from sqlalchemy import Column, String, Integer

from .database import Base

class Place(Base):
    __tablename__ = 'place'

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, index=True)
    token = Column(String)

    current_num = Column(Integer, default=0)
