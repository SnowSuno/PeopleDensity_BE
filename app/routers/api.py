from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.core import schemas, crud


router = APIRouter(
    prefix='/api',
    tags=['client side api'],
)


@router.get("/places/", response_model=List[schemas.Place])
async def read_places(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    places = crud.get_places(db, skip=skip, limit=limit)
    return places

@router.get("/places/{key}", response_model=schemas.Place)
async def read_place(key: str, db: Session = Depends(get_db)):
    db_place = crud.get_place_by_key(db, key=key)
    if db_place is None:
        raise HTTPException(status_code=404, detail="Invalid key")
    return db_place

