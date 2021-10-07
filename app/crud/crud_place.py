import string
import random

from sqlalchemy.orm import Session

from .base import CRUDBase
from app.models.place import Place
from app.schemas.place import PlaceCreate, PlaceUpdate


class CRUDPlace(CRUDBase[Place, PlaceCreate, PlaceUpdate]):
    def get_by_key(
        self, db: Session, *, key: str
    ) -> Place:
        return db.query(self.model).filter(Place.key == key).first()

    def create(self, db: Session, *, obj_in: PlaceCreate) -> Place:
        if obj_in.token is None:
            obj_in.token = self._generate_token()

        return super(CRUDPlace, self).create(db, obj_in=obj_in)

    @staticmethod
    def _generate_token(size=12, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


place = CRUDPlace(Place)
