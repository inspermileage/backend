from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from src.api.utils.db import get_db
from src.crud.crud_car import create, delete, read_all, read_one_by_id, read_one_by_date, update
from src.crud.utils import ExistenceException, NonExistenceException
from src.schemas.car import CarCreate, CarInDB, CarUpdate

router = APIRouter()


@router.get("/", response_model=List[CarInDB])
def read_cars(db: Session = Depends(get_db)):
    """
    Returns a list of all the round entries in the database.
    """

    return read_all(db_session=db)


@router.get("/{car_id}", response_model=CarInDB)
def read_car(*, db: Session = Depends(get_db), car_id: int):
    """
    Returns a Round specified by the id.
    """

    try:
        existing_round = read_one_by_id(db_session=db, car_id=car_id)
    except NonExistenceException as err:
        raise HTTPException(status_code=404, detail=err.message)
    return existing_round


@router.get("/{car_data_teste}", response_model=CarInDB)
def read_car(*, db: Session = Depends(get_db), car_ref_date: date):
    """
    Returns a Round specified by the date.
    """

    try:
        existing_round = read_one_by_date(db_session=db, car_ref_date=car_ref_date)
    except NonExistenceException as err:
        raise HTTPException(status_code=404, detail=err.message)
    return existing_round


@router.post("/", response_model=CarInDB)
def create_car(*, db: Session = Depends(get_db), car_in: CarCreate):
    """
    Inserts a round into the Car table, given the request body.
    """
    try:
        created_car = create(db_session=db, obj_in=car_in)
    except ExistenceException as err:
        raise HTTPException(status_code=303, detail=err.message)
    return created_car


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
    
@router.delete("/{car_id}", response_model=CarInDB)
def delete_car(*, db: Session = Depends(get_db), car_id: int):
    """
    Deletes a Car specified by the name.
    """

    try:
        deleted_car = delete(db_session=db, car_id=car_id)
    except NonExistenceException as err:
        raise HTTPException(status_code=303, detail=err.message)
    return deleted_car
