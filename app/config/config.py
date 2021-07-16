import os
from dotenv import load_dotenv
load_dotenv()

BASEDIR = os.getcwd()
SECRET_KEY = os.getenv("SECRET_KEY")

def create_sqlite_uri(db_name):
    return "sqlite:///" + os.path.join(BASEDIR, 'tests', db_name)

class BaseConfig:
    SECRET_KEY = SECRET_KEY

class DevelopmentConfig(BaseConfig):
    MODE = "DEVELOPMENT"
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@ip:3306/tablename'

class TestingConfig(BaseConfig):
    MODE = "TESTING"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = create_sqlite_uri("test.db")

class Config:

    def set_mode(self, mode: str):
        self.mode = mode

    def get_mode(self):
        return {
            'development': DevelopmentConfig,
            'testing': TestingConfig,
        }.get(self.mode)

config = Config()