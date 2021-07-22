import pytest

from fastapi.testclient import TestClient

@pytest.mark.parametrize(('id', 'name', 'infos'), (
    ('2', 'one_description_user', [{'description': 'email', 'information': 'test1@gmail.com', 'user': 'one_description_user'}]),
    ('3', 'multy_description_user', [{'description': 'email', 'information': 'test2@gmail.com', 'user': 'multy_description_user'}, {'description': 'tag', 'information': 'good_user', 'user': 'multy_description_user'}]),
    ('4', 'no_description_user', [])
))
def test_get_user_by_id(client: TestClient, db, id, name, infos, access_token):

    response = client.get(
        f'/user/search/{id}',
        headers={
            'Authorization': f'Bearer {access_token("admin_user")}'
        }
    )
    assert 200 == response.status_code
    assert infos == response.json()['informations']
    sql = f"""
        SELECT `name` FROM `users` WHERE `uid` == {id}
    """
    assert name in db.execute(sql).fetchone()

def test_get_user_by_name(client: TestClient, db, access_token):

    response = client.get(
        '/user/search/default_user',
        headers={
            'Authorization': f'Bearer {access_token("admin_user")}'
        }
    )

    assert 200 == response.status_code
    assert 'default_user' in response.json()['name']
@pytest.mark.parametrize(('id', 'expected', 'name'),(
    (100, [404, 'user not found'], 'admin_user'),
    ("no_such_user", [404, 'user not found'], 'admin_user'),
    (1, [403, 'Operation is forbidden'], 'default_user'),
))
def test_get_user_failure(client: TestClient, db, access_token, id, expected, name):

    response = client.get(
        f'/user/search/{id}',
        headers={
            'Authorization': f'Bearer {access_token(name)}'
        }
    )
    assert expected[0] == response.status_code
    assert expected[1] == response.json()['detail']

def test_get_me_with_login(client: TestClient, access_token, db):

    response = client.get(
        'user/me/',
        headers={
            'Authorization': f'Bearer {access_token("default_user")}'
        }
    )

    assert 200 == response.status_code
    assert 'default_user' == response.json()['name']

def test_get_me_with_expired_token(client: TestClient, db, access_token):

    response = client.get(
        'user/me/',
        headers={
            'Authorization': f'Bearer {access_token("default_user", expires=True)}'
        }
    )

    assert 401 == response.status_code
    assert 'Could not validate credentials' == response.json()['detail']

def test_get_me_with_disabled_user(client: TestClient, db, access_token):
    response = client.get(
        'user/me',
        headers={
            'Authorization': f'Bearer {access_token("disabled_user")}'
        }
    )

    assert 422 == response.status_code

def test_get_all_user(client: TestClient, db, access_token):

    response = client.get(
        'user/all',
        headers={
            'Authorization': f'Bearer {access_token("admin_user")}'
        }
    )

    assert 200 == response.status_code
    assert 'default_user' == response.json()[0]['name']

@pytest.mark.parametrize(('username', 'expected'),(
    ('default_user', [403, 'Operation is forbidden']),
    ('disabled_admin', [422, 'Inactive user'])
))
def test_get_all_user_failed(client: TestClient, db, access_token, username, expected):
    response = client.get(
        'user/all',
        headers={
            'Authorization': f'Bearer {access_token(username)}'
        }
    )
    
    assert expected[0] == response.status_code
    assert expected[1] == response.json()['detail']