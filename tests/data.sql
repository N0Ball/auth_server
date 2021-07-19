INSERT INTO users (name, password, status)
VALUES
    ('default_user', '$2b$12$j4pNHP1Ni4sXa1NOrO8Ww.vs9/Fq0Sa39lfFBXIiozLeMGluS.yui', 1),
    ('one_description_user', 'test_password', 1),
    ('multy_description_user', 'test_password', 1),
    ('no_description_user', 'test_password', 1),
    ('disabled_user', "$2b$12$j4pNHP1Ni4sXa1NOrO8Ww.vs9/Fq0Sa39lfFBXIiozLeMGluS.yui", 0);

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