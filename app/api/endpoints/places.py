from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db

from app import crud, schemas

router = APIRouter(
    prefix='/places',
    tags=['client side api'],
)


@router.get("/", response_model=List[schemas.Place])
async def read_places(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    places = crud.place.get_multi(db, skip=skip, limit=limit)
    return places

@router.get("/{key}", response_model=schemas.Place)
async def read_place(key: str, db: Session = Depends(get_db)):
    db_place = crud.place.get_by_key(db, key=key)
    if db_place is None:
        raise HTTPException(status_code=404, detail="Invalid key")
    return db_place

