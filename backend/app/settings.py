from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    backend_cors_origins: list[str] = []
