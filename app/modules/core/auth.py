from datetime import datetime, timedelta

from jose import JWTError, jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.config.config import config, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
SECRET_KEY = config.get_mode().SECRET_KEY
from app.modules.lib import hash
from app.modules.schemas import schemas
from . import user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

    except JWTError:
        raise credentials_exception

    current_user = user.get_user(name=username, not_none=False)
    
    if current_user is None:
        raise credentials_exception

    return current_user

async def get_current_active_user(current_user: schemas.User = Depends(get_current_user)):

    if not current_user.status == 1:
        raise HTTPException(422, "Inactive user")

    return current_user

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def authenticate_user(username: str, password: str):

    current_user = user.get_user(name=username)
    if not hash.check_password(password, current_user.password):
        raise HTTPException(422, "Incorrect password")

    if not current_user.status == 1:
        raise HTTPException(422, "Inactive user")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": current_user.name}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}