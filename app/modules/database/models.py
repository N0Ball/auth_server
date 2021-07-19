from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from .db import Base


class User(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=True, nullable=False, index=True)
    password = Column(String(128), comment="hashed password")
    status = Column(Integer, default=1, nullable=False, comment="0: deleted, 1: active")
    roles = Column(String(512), default='["default"]', nullable=False, comment="List of roles the user has")
    create_time = Column(DateTime, default=datetime.utcnow)
    update_time = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    informations = relationship("UserInfo", back_populates="user_relation")


class UserInfo(Base):
    __tablename__ = "user_informations"

    id = Column(Integer, primary_key=True, index=True)
    description_id = Column(Integer, ForeignKey("information_descriptions.id"), index=True)
    uid = Column(Integer, ForeignKey("users.uid"), index=True)
    information = Column(String(512))
    create_time = Column(DateTime, default=datetime.utcnow)
    update_time = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    description_relation = relationship("UserInfoDescription")
    description = association_proxy('description_relation', 'name')
    user_relation = relationship("User")
    user = association_proxy('user_relation', 'name')

class UserInfoDescription(Base):
    __tablename__ = "information_descriptions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=True, nullable=False, index=True)
    create_time = Column(DateTime, default=datetime.utcnow)
    update_time = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    information_relation = relationship("UserInfo", back_populates='description_relation')
    users = association_proxy('information_relation', 'user')
    

