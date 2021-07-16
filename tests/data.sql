INSERT INTO users (name, password)
VALUES
    ('test1', 'test_password'),
    ('test2', 'test_password');

---

INSERT INTO user_descriptions (name)
VALUES
    ('email'),
    ('tag');

---

INSERT INTO user_informations (description_id, uid, information)
VALUES
    (1, 1, "test1.gmail.com"),
    (1, 2, "test2.gmail.com"),
    (2, 2, "good_user");