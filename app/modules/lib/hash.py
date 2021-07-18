import bcrypt
import base64
import hashlib

def hash_password(password: str) -> str:
    length_modified_hash = base64.b64encode(hashlib.sha256(password.encode()).digest())
    return bcrypt.hashpw(length_modified_hash, bcrypt.gensalt()).decode('utf-8')

def check_password(password: str, target: str) -> bool:
    length_modified_hash = base64.b64encode(hashlib.sha256(password.encode()).digest())
    return bcrypt.checkpw(length_modified_hash, target)