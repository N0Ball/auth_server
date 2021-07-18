import pytest

from fastapi.testclient import TestClient

from app.modules.lib import hash

def test_add_new_user(client: TestClient, db):
    response = client.post(
        '/auth/register',
        json={
            'name': 'new-user',
            'password': 'passw0rd!'
        },
        headers={'Content-Type': 'application/json'}
    )

    assert 200 == response.status_code

    sql = """
        SELECT `name`, `password` FROM `users` WHERE `name` == 'new-user'
    """
    username, password = db.execute(sql).fetchone()

    assert username == 'new-user'
    assert hash.check_password('passw0rd!', password)

def test_add_exist_user(client: TestClient, db):
    response = client.post(
        '/auth/register',
        json={
            'name': 'default_user',
            'password': 'passw0rd!'
        },
        headers={'Content-Type': 'application/json'}
    )
    
    assert 409 == response.status_code

    sql = """
        SELECT `password` FROM `users` WHERE `name` == 'default_user'
    """
    assert 'passw0rd!' not in db.execute(sql).fetchone()

@pytest.mark.parametrize(("username", "password", "expected_value"),(
    ("user_name_failed!", "user_name_with_invalid_charactor_1", 'username has to'),
    ("us", "user_name_too_short_1", 'username has to'),
    ("0user"*26, "user_name_start_with_number", 'username has to'),
    ("a"*26, "user_name_too_long_1", 'username has to'),
    ("password_no_number", "password", 'password has to'),
    ("password_no_letter", "123456789", 'password has to'),
    ("password_too_short", "2sh0rt", 'password has to')
))
def test_creat_user_validation_failed(client: TestClient, db, username, password, expected_value):
    response = client.post(
        '/auth/register',
        json={
            'name': username,
            'password': password
        },
        headers={'Content-Type': 'application/json'}
    )

    assert 422 == response.status_code
    assert expected_value in response.json()['detail']
    sql = f"""
        SELECT * FROM `users` WHERE `name` == '{username}'
    """
    assert [] == db.execute(sql).fetchall()