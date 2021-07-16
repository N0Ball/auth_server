import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.config import config, BASEDIR
config.set_mode("testing")
engine = create_engine(config.get_mode().SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})

from app import init_db, del_db, create_app

@pytest.fixture
def app():

    app = create_app()

    yield app

@pytest.fixture
def client(app):
    return TestClient(app)

@pytest.fixture
def db():
    del_db(engine)
    init_db(engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    database = TestingSessionLocal()
    

    with open(f"{BASEDIR}/tests/data.sql", 'rb') as f:
        _data_sql = f.read().decode('utf-8')

    for sql in _data_sql.split('---'):
        database.execute(sql)

    database.commit()

    return database