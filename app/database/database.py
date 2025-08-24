from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config.configs import configs

if configs.DATABASE_URL:
    Engine = create_engine(configs.DATABASE_URL, echo=True)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
