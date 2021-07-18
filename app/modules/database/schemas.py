from typing import List, Optional

from pydantic import BaseModel

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    password: str

class UserInfoBase(BaseModel):
    information: str

class UserInfoCreate(UserInfoBase):
    uid: int
    description_id: int

class UserInfoDescriptionBase(BaseModel):
    name: str

class UserInfoCreate(UserInfoDescriptionBase):
    pass

class UserInfo(UserInfoBase):
    information: str
    description: str

    class Config:
        orm_mode = True

class User(UserBase):
    uid: int
    status: int
    role: Optional[str] = None

    informations: List[UserInfo]

    class Config:
        orm_mode = True

class UserInfoDescription(UserInfoDescriptionBase):
    users: List[str]
    information: str

    class Config:
        orm_mode = True
