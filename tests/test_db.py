def test_db_connection(db):
    sql = """
        SELECT * FROM users WHERE uid = 1
    """
    assert 'default_user' in db.execute(sql).fetchone()