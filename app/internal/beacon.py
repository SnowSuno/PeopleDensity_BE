from fastapi import APIRouter, Header, HTTPException, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.core import schemas, crud


router = APIRouter(
    prefix='/internal',
    tags=['beacon communication api'],
    responses={404: {"description": "Not found"}},
)

@router.put('/')
async def update_people_num(place: schemas.PlaceUpdate, x_beacon_token: str = Header(...),
                            db: Session = Depends(get_db)):
    db_place = crud.get_place_by_key(db, key=place.key)
    if db_place is None:
        raise HTTPException(status_code=404, detail="Invalid key")

    if x_beacon_token != db_place.token:
        raise HTTPException(status_code=401, detail="X-Beacon-Token invalid")

    db_place.current_num = place.current_num
    db.commit()
    db.refresh(db_place)
    return db_place



