def test_config(client):
    assert "TESTING" is client.app.extra['config'].MODE

def test_db_uri(client):
    assert "auth_server/tests/test.db" in client.app.extra['config'].SQLALCHEMY_DATABASE_URI