from fastapi import APIRouter

from .endpoints import admin, beacon, places

router = APIRouter()
router.include_router(admin.router)
router.include_router(beacon.router)
router.include_router(places.router)
