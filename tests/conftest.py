import os
import pytest

from fastapi.testclient import TestClient

from app.config.config import config, BASEDIR
config.set_mode("testing")

from app import create_app
from app.modules.database import get_db

@pytest.fixture
def app():

    app = create_app()

    yield app

@pytest.fixture
def client(app):
    return TestClient(app)

@pytest.fixture
def db():
    get_db.init_db()

    database = get_db()   

    with open(f"{BASEDIR}/tests/data.sql", 'rb') as f:
        _data_sql = f.read().decode('utf-8')

    for sql in _data_sql.split('---'):
        database.execute(sql)

    database.commit()

    try:
        yield database
    finally:
        database.close()

    get_db.del_db()
    