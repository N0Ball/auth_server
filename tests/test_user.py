import pytest

from fastapi.testclient import TestClient

@pytest.mark.parametrize(('url', 'name', 'infos'), (
    ('/user/1', 'one_description_user', [{'description': 'email', 'information': 'test1.gmail.com'}]),
    ('/user/2', 'multy_description_user', [{'description': 'email', 'information': 'test2.gmail.com'}, {'description': 'tag', 'information': 'good_user'}]),
    ('/user/3', 'no_description_user', [])
))
def test_get_user_by_id(client: TestClient, db, url, name, infos):

    result = client.get(url)
    assert 200 == result.status_code
    assert name == result.json()['name']
    assert infos == result.json()['informations']

def test_get_no_user(client: TestClient, db):

    result = client.get('user/100')
    assert 404 == result.status_code
    assert 'user not found' == result.json()['detail']