from typing import List

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
    description: str
    information: str

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    status: int
    role: str
    descriptions: List[UserInfo]

    class Config:
        orm_mode = True

class UserInfoDescription(UserInfoDescriptionBase):
    users: List[User]

    class Config:
        orm_mode = True
