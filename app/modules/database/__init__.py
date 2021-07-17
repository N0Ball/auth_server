from sqlalchemy.orm import sessionmaker, Session

from app.config.config import config
from app.modules.database import models
class Db:

    engine = config.get_mode().ENGINE

    def __call__(self) -> Session:

        TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        db = TestingSessionLocal()

        return db

    def init_db(self):
        models.Base.metadata.create_all(bind=self.engine)

    def del_db(self):
        models.Base.metadata.drop_all(bind=self.engine)

get_db = Db()