import pytest

from fastapi.testclient import TestClient
from app.modules.lib import hash

EXPIRED_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkZWZhdWx0X3VzZXIiLCJleHAiOjE2MjY2NTU1MTB9.3aTp1HAxuNTqu8bhmDr_fe9vQYFjkw8SCUWIpS7yvWs'

def test_add_new_user(client: TestClient, db):
    response = client.post(
        '/user/create',
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
        '/user/create',
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
        '/user/create',
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

@pytest.mark.parametrize(('id', 'name', 'infos'), (
    ('2', 'one_description_user', [{'description': 'email', 'information': 'test1@gmail.com'}]),
    ('3', 'multy_description_user', [{'description': 'email', 'information': 'test2@gmail.com'}, {'description': 'tag', 'information': 'good_user'}]),
    ('4', 'no_description_user', [])
))
def test_get_user_by_id(client: TestClient, db, id, name, infos):

    response = client.get(f'/user/search/{id}')
    assert 200 == response.status_code
    assert infos == response.json()['informations']
    sql = f"""
        SELECT `name` FROM `users` WHERE `uid` == {id}
    """
    assert name in db.execute(sql).fetchone()

def test_get_user_by_name(client: TestClient, db):

    response = client.get('/user/search/default_user')

    assert 200 == response.status_code
    assert 'default_user' in response.json()['name']

def test_get_no_user_id(client: TestClient, db):

    response = client.get('user/search/100')
    assert 404 == response.status_code
    assert 'user not found' == response.json()['detail']

def test_get_me_with_login(client: TestClient, login):

    response = client.get(
        'user/me/',
        headers={
            'Authorization': f'Bearer {login["access_token"]}'
        }
    )

    assert 200 == response.status_code
    assert 'default_user' == response.json()['name']

def test_get_me_with_expired_token(client: TestClient, db):

    response = client.get(
        'user/me/',
        headers={
            'Authorization': f'Bearer {EXPIRED_TOKEN}'
        }
    )

    assert 401 == response.status_code
    assert 'Could not validate credentials' == response.json()['detail']