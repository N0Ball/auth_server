import logging

from fastapi import FastAPI
from fastapi.logger import logger

gunicorn_logger = logging.getLogger('gunicorn.error')
logger.handlers = gunicorn_logger.handlers

from .config.config import config

def create_app():
    
    app = FastAPI(config=config.get_mode())

    logger.setLevel(app.extra['config'].LOG)

    from app.routes import base, auth, user, description
    app.include_router(base.router)
    app.include_router(auth.router)
    app.include_router(user.router)
    app.include_router(description.router)

    return app
