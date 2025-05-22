from pydantic import BaseSettings
from typing import List

class Settings(BaseSettings):
    azure_tenant: str
    azure_client_id: str
    api_audience: str
    jwks_url: str
    log_level: str = "INFO"
    cors_origins: List[str] = ["http://localhost:8001"]
    database_url: str  # Postgres connection URL

    class Config:
        env_file = ".env"

settings = Settings()
