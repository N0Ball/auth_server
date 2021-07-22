import os
from dotenv import load_dotenv
load_dotenv()

from sqlalchemy import create_engine

BASEDIR = os.getcwd()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def create_sqlite_uri(db_name):
    return "sqlite:///" + os.path.join(BASEDIR, 'tests', db_name)

class BaseConfig:
    SECRET_KEY = SECRET_KEY
    ALGORITHM = ALGORITHM
    MODE = "Default"
    ENGINE = "No Engine"
    LOG = "DEBUG"

class DevelopmentConfig(BaseConfig):
    tablename = os.getenv('AUTH_SERVICE_DB')
    username = os.getenv('AUTH_USER')
    password = os.getenv('AUTH_PASSWORD')
    MODE = "DEVELOPMENT"
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{username}:{password}@localhost:3306/{tablename}'
    ENGINE = create_engine(SQLALCHEMY_DATABASE_URI)

class TestingConfig(BaseConfig):
    MODE = "TESTING"
    SECRET_KEY = "SECRET_KEY"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = create_sqlite_uri("test.db")
    ENGINE = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})

class Config:

    def set_mode(self, mode: str):
        self.mode = mode

    def get_mode(self) -> BaseConfig:
        return {
            'development': DevelopmentConfig,
            'testing': TestingConfig,
        }.get(self.mode)

config = Config()