from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    class COnfig:
        env_file=".env"

settings = Settings()