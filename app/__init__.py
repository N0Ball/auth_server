from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker

from .config.config import config

def create_app():
    
    app = FastAPI(**config.get_mode().__dict__)

    from app.routes import base
    app.include_router(base.router)

    return app

from .modules.database import models

def get_db(engine):

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db(engine):
    models.Base.metadata.create_all(bind=engine)

def del_db(engine):
    models.Base.metadata.drop_all(bind=engine)
