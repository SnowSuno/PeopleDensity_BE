from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    DATABASE_URL: Union[PostgresDsn, str]

    @validator("DATABASE_URL", pre=True)
    def patch_database_url(cls, v: str):
        return v.replace("postgres://", "postgresql://", 1)

    ADMIN_ID: str
    ADMIN_PASSWORD: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
