from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "FAST cavAPI"
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    ALGORITHM: str = "HS256"
    DEBUG: bool = True
    POOL_SIZE: int = 5
    MAX_OVERFLOW: int = 10
    POOL_PRE_PING: bool = True

    @property
    def DATABASE_URL(self) -> str:
        return f"mariadb+mariadbconnector://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()