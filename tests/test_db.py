def test_db_connection(db):
    sql = """
        SELECT * FROM users WHERE uid = 1
    """
    assert 'test1' in db.execute(sql).fetchone()