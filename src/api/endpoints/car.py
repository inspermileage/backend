from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.api.utils.db import get_db
from src.crud.utils import ExistenceException, NonExistenceException

from src.crud.crud_car import (create, delete, read_all,
                               read_one, update)

from src.schemas.car import CarCreate, CarInDB, CarUpdate


router = APIRouter()


@router.post("/", response_model=CarInDB)
def create_car(*, db: Session = Depends(get_db), car_in: CarCreate):
    """
    Inserts a car into the car table, given the request body.
    """
    try:
        created_car = create(db=db, car_in=car_in)
    except ExistenceException as err:
        raise HTTPException(status_code=303, detail=err.message)
    return created_car


@router.get("/", response_model=List[CarInDB])
def read_car(db: Session = Depends(get_db)):
    """
    Returns a list of all the car entries in the database.
    """

    return read_all(db=db)


@router.get("/{car_name}", response_model=CarInDB)
def read_car_by_name(*, db: Session = Depends(get_db), car_name: str):
    """
    Returns a Car specified by the name
    """

    try:
        existing_car = read_one(db_session=db, name=car_name)
    except NonExistenceException as err:
        raise HTTPException(status_code=404, detail=err.message)
    return existing_car


@router.put("/{car_id}", response_model=CarInDB)
def update_car(*, db: Session = Depends(get_db), car_id: int, car_info: CarUpdate):
    """
    Updates the Car specified by the ID field in the request body, with the rest of the body fields.
    """

    try:
        updated_car = update(db=db, car_id=car_id, car_info=car_info)
    except NonExistenceException as err:
        raise HTTPException(status_code=404, detail=err.message)
    return updated_car


@router.delete("/{name}", response_model=CarInDB)
def delete_car(*, db: Session = Depends(get_db), name: str):
    """
    Deletes a Car specified by the name.
    """

    try:
        deleted_car = delete(db=db, name=name)
    except NonExistenceException as err:
        raise HTTPException(status_code=303, detail=err.message)
    return deleted_car
