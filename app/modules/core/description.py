from fastapi import HTTPException
from sqlalchemy.sql.expression import desc

from app.modules.schemas import schemas
from app.modules.database import crud, models

def create_description(new_description: schemas.UserInfoDescriptionCreate) -> models.UserInfoDescription:
    
    if get_description_by_name(name=new_description.name, nullable=True) is not None:
        raise HTTPException(409, 'Description already exists')

    return crud.create_descriptions(new_description)


def get_description_by_id(id: int, nullable:bool = False) -> models.UserInfoDescription:

    description = crud.get_description(id=id)

    if description is None and not nullable:
        raise HTTPException(404, 'Description not found')

    return description

def get_description_by_name(name: str, nullable:bool = False) -> models.UserInfoDescription:

    description = crud.get_description(name=name)

    if description is None and not nullable:
        raise HTTPException(404, 'Description not found')

    return description
