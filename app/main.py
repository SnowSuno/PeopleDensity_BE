from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

from app.core import models
from app.core.models.database import SessionLocal, engine

from app.routers import api
from app.internal import beacon, admin


def get_application():
    models.Base.metadata.create_all(bind=engine)

    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(api.router)
    _app.include_router(beacon.router)
    _app.include_router(admin.router)

    return _app


app = get_application()


@app.get('/')
async def root():
    return {"message": "ksa density api endpoint"}
