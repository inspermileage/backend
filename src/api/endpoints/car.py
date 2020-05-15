from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.api.utils.db import get_db
from src.crud.crud_rounds import create, delete, read_all, read_one, update
from src.crud.utils import ExistenceException, NonExistenceException
from src.schemas.car import CarCreate, CarInDB, CarUpdate

router = APIRouter()


@router.delete("/{car_id}", response_model=CarInDB)
def delete_round(*, db: Session = Depends(get_db), car_id: int):
    """
    Deletes a Round specified by the name.
    """

    try:
        deleted_car = delete(db_session=db, car_id=car_id)
    except NonExistenceException as err:
        raise HTTPException(status_code=303, detail=err.message)
    return deleted_car
