import json
from json.decoder import JSONDecodeError

from app import logger

def get_role(role_string: str) -> list:

    try:
        current_role: list = json.loads(role_string)
    except JSONDecodeError as e:
        logger.error(f'decode user role fails: {e}')        
        
    return json.dumps(current_role)