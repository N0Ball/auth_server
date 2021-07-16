from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .db import Base


class User(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=True, nullable=False, index=True)
    password = Column(String(128), comment="hashed password")
    status = Column(Integer, default=True, comment="0: deleted, 1: active")
    roles = Column(String, default='[]', comment="List of roles the user has")
    create_time = Column(DateTime, default=datetime.utcnow)
    update_time = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    informations = relationship("UserInfo", back_populates="user")


class UserInfo(Base):
    __tablename__ = "user_informations"

    id = Column(Integer, primary_key=True, index=True)
    description_id = Column(Integer, ForeignKey("user_descriptions.id"), index=True)
    uid = Column(Integer, ForeignKey("users.uid"), index=True)
    information = Column(String(50))
    create_time = Column(DateTime, default=datetime.utcnow)
    update_time = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    description = relationship("UserInfoDescription")

class UserInfoDescription(Base):
    __tablename__ = "user_descriptions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)
    create_time = Column(DateTime, default=datetime.utcnow)
    update_time = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    users = relationship("User", secondary="UserInfo")
    

