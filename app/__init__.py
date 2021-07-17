from fastapi import FastAPI

from .config.config import config

def create_app():
    
    app = FastAPI(**config.get_mode().__dict__)

    from app.routes import base
    app.include_router(base.router)

    return app
