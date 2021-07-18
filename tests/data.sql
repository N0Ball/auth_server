INSERT INTO users (name, password, status)
VALUES
    ('one_description_user', 'test_password', 1),
    ('multy_description_user', 'test_password', 1),
    ('no_description_user', 'test_password', 1);

---

INSERT INTO information_descriptions (name)
VALUES
    ('email'),
    ('tag');

---

INSERT INTO user_informations (description_id, uid, information)
VALUES
    (1, 1, "test1.gmail.com"),
    (1, 2, "test2.gmail.com"),
    (2, 2, "good_user");