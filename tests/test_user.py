import pytest

from fastapi.testclient import TestClient

@pytest.mark.parametrize(('id', 'name', 'infos'), (
    ('2', 'one_description_user', [{'description': 'email', 'information': 'test1@gmail.com'}]),
    ('3', 'multy_description_user', [{'description': 'email', 'information': 'test2@gmail.com'}, {'description': 'tag', 'information': 'good_user'}]),
    ('4', 'no_description_user', [])
))
def test_get_user_by_id(client: TestClient, db, id, name, infos):

    response = client.get(f'/user/{id}')
    assert 200 == response.status_code
    assert infos == response.json()['informations']
    sql = f"""
        SELECT `name` FROM `users` WHERE `uid` == {id}
    """
    assert name in db.execute(sql).fetchone()

def test_get_user_by_name(client: TestClient, db):

    response = client.get('/user/default_user')

def test_get_no_user_id(client: TestClient, db):

    response = client.get('user/100')
    assert 404 == response.status_code
    assert 'user not found' == response.json()['detail']