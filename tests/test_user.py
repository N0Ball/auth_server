import pytest

from fastapi.testclient import TestClient

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
        'user/me/',
        headers={
            'Authorization': f'Bearer {access_token("disabled_user")}'
        }
    )

    assert 400 == response.status_code