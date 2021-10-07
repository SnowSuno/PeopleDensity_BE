from sqlalchemy import Column, String, Integer

from app.database.base import Base

class Place(Base):
    id = Column(String(5), primary_key=True, index=True, unique=True)
    name = Column(String)
    token = Column(String)

    current_num = Column(Integer, default=0)
