from sqlmodel import create_engine, Session

from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    echo=settings.DEBUG,
    pool_size=settings.POOL_SIZE,
    max_overflow=settings.MAX_OVERFLOW,
    pool_pre_ping=settings.POOL_PRE_PING
)

def get_session():
    with Session(engine) as session:
        yield session