from fastapi import APIRouter, Header, HTTPException, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app import crud, schemas

router = APIRouter(
    prefix='/beacon',
    tags=['beacon communication api'],
    responses={404: {"description": "Not found"}},
)

@router.put('/')
async def update_people_num(place: schemas.PlaceUpdate, x_beacon_token: str = Header(...),
                            db: Session = Depends(get_db)):
    db_place = crud.place.get(db, id=place.id)
    if db_place is None:
        raise HTTPException(status_code=404, detail="Invalid key")

    if x_beacon_token != db_place.token:
        raise HTTPException(status_code=401, detail="X-Beacon-Token invalid")

    return crud.place.update(db, db_obj=db_place, obj_in=place)
