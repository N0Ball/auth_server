import pytest

from fastapi.testclient import TestClient

def test_login(client: TestClient, db):
    response = client.post(
        '/auth/token',
        data={
            'username': 'default_user',
            'password': 'passw0rd!'
        },
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    )

    assert 200 == response.status_code
    assert 'access_token' in response.json()

@pytest.mark.parametrize(('username', 'password', 'expected_value', 'status_code'), (
    ('none_exist_user', 'passw0rd!', 'user not found', 404),
    ('default_user', 'Incorrect password', 'Incorrect password', 422),
    ('disabled_user', 'passw0rd!', 'Inactive user', 422),
))
def test_login_failure(client: TestClient, db, username, password, expected_value, status_code):
    response = client.post(
        '/auth/token',
        data={
            'username': username,
            'password': password
        },
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    )

    assert status_code == response.status_code
    assert expected_value == response.json()['detail']