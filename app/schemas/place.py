from typing import Optional

from pydantic import BaseModel

class PlaceBase(BaseModel):
    key: str

class PlaceCreate(PlaceBase):
    token: Optional[str]

class PlaceUpdate(PlaceBase):
    current_num: int

class Place(PlaceBase):
    id: int
    current_num: int

    class Config:
        orm_mode = True

class AdminPlace(PlaceBase):
    id: int
    token: str
    current_num: int

    class Config:
        orm_mode = True
