def test_config(client):
    assert "TESTING" is client.app.extra["MODE"]