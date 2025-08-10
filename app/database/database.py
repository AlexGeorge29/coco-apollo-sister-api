from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config.configs import configs

# Moteur SQLAlchemy
Engine = create_engine(configs.DATABASE_URL, echo=True)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

# Base pour les modèles


# Dependency pour obtenir la session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
