import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if os.getenv("PYTHON_ENV") == "production":
    DATABASE_URL = os.environ["DB_URL"]
else:
    DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
