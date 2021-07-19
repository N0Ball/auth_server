INSERT INTO users (name, password, status, roles)
VALUES
    ('default_user', '$2b$12$j4pNHP1Ni4sXa1NOrO8Ww.vs9/Fq0Sa39lfFBXIiozLeMGluS.yui', 1, '["default"]'),
    ('one_description_user', 'test_password', 1, '["default"]'),
    ('multy_description_user', 'test_password', 1, '["default"]'),
    ('no_description_user', 'test_password', 1, '["default"]'),
    ('disabled_user', "$2b$12$j4pNHP1Ni4sXa1NOrO8Ww.vs9/Fq0Sa39lfFBXIiozLeMGluS.yui", 0, '["default"]'),
    ('admin_user', "$2b$12$j4pNHP1Ni4sXa1NOrO8Ww.vs9/Fq0Sa39lfFBXIiozLeMGluS.yui", 1, '["admin"]')

---

INSERT INTO information_descriptions (name)
VALUES
    ('email'),
    ('tag');

---

INSERT INTO user_informations (description_id, uid, information)
VALUES
    (1, 1, "defualt@gmail.com"),
    (1, 2, "test1@gmail.com"),
    (1, 3, "test2@gmail.com"),
    (2, 3, "good_user");