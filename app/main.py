from .config.config import config
from app import create_app

config.set_mode("development")
app = create_app()