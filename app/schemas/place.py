from typing import Optional

from pydantic import BaseModel

class PlaceBase(BaseModel):
    id: str

class PlaceCreate(PlaceBase):
    name: str
    token: Optional[str]

class PlaceUpdate(PlaceBase):
    current_num: int

class Place(PlaceBase):
    name: str
    current_num: int

    class Config:
        orm_mode = True

class AdminPlace(PlaceBase):
    name: str
    token: str
    current_num: int

    class Config:
        orm_mode = True
