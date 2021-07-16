def test_health(client):

    with client:
        response = client.get('/check_health')
        assert response.status_code == 200
        assert response.json() == {"detail": "Everything is normal"}