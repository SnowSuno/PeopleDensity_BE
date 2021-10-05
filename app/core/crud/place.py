from sqlalchemy.orm import Session

from app.core import models, schemas

import string
import random

def get_place(db: Session, place_id: int):
    return db.query(models.Place).filter(models.Place.id == place_id).first()

def get_place_by_key(db: Session, key: str):
    return db.query(models.Place).filter(models.Place.key == key).first()

def get_places(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Place).offset(skip).limit(limit).all()

def create_place(db: Session, place: schemas.PlaceCreate):
    token = _generate_token()
    db_place = models.Place(key=place.key, token=token)
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place

def _generate_token(size=12, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
