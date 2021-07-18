from . import get_db, models, schemas

db = get_db()

def create_user(user: schemas.UserCreate) -> models.User:
    db.add(user)
    db.commit()
    db.refresh()
    return user

def get_user_by_id(id: int) -> models.User:
    return db.query(models.User).filter(models.User.uid == id).first()

def get_user_by_name(name: str) -> models.User:
    return db.query(models.User).filter(models.User.uid == name).first()
    