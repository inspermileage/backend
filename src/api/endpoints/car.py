from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.api.utils.db import get_db
from src.crud.crud_rounds import create, delete, read_all, read_one, update
from src.crud.utils import ExistenceException, NonExistenceException
from src.schemas.car import CarCreate, CarInDB, CarUpdate

router = APIRouter()


@router.put("/", response_model=CarInDB)
def update_car(*, db: Session = Depends(get_db), car_id: int, car_info: CarUpdate):
    """
    Updates the Car specified by id, with the body request fields.
    """
    try:
        updated_car = update(db_session=db, car_id=car_id, obj_in=car_info)
    except NonExistenceException as err:
        raise HTTPException(status_code=303, detail=err.message)
    return updated_car
