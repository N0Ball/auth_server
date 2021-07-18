def test_db_connection(db):
    sql = """
        SELECT * FROM users WHERE uid = 1
    """
    assert 'one_description_user' in db.execute(sql).fetchone()