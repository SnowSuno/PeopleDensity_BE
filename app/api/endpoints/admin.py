from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app import crud, schemas

from app.core.config import settings

security = HTTPBasic()
async def authorize_admin(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != settings.ADMIN_ID or credentials.password != settings.ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Admin auth failed")

router = APIRouter(
    prefix='/admin',
    tags=["admin api for data handling"],
    dependencies=[Depends(authorize_admin)],
    responses={401: {"description": "Authentication failed"}},
)

@router.get('/')
async def admin_root():
    return {"message": "admin root"}

@router.post('/places/', response_model=schemas.AdminPlace)
async def create_place(place: schemas.PlaceCreate, db: Session = Depends(get_db)):
    db_place = crud.place.get(db, id=place.id)
    if db_place:
        raise HTTPException(status_code=400, detail="ID already exists")
    return crud.place.create(db, obj_in=place)

@router.get("/places/", response_model=List[schemas.AdminPlace])
async def read_places(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    places = crud.place.get_multi(db, skip=skip, limit=limit)
    return places

@router.get("/places/{id}", response_model=schemas.AdminPlace)
async def read_place(id: str, db: Session = Depends(get_db)):
    db_place = crud.place.get(db, id=id)
    if db_place is None:
        raise HTTPException(status_code=404, detail="Invalid key")
    return db_place
