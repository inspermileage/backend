from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from src.api.utils.db import get_db
from src.crud.utils import ExistenceException, NonExistenceException
from src.models.car import Car as CarModel

from src.crud.crud_car import create, delete, read_all, read_one, update

from src.schemas.car import CarCreate, CarInDB, CarUpdate


router = APIRouter()


@router.post("/", response_model=CarInDB)
def create_car(*, db: Session = Depends(get_db), car_in: CarCreate):
    """
    Inserts a car into the car table, given the request body.
    """
    try:
        created_car = create(db_session=db, obj_in=car_in)
    except ExistenceException as err:
        raise HTTPException(status_code=404, detail="Car not found")
    return created_car


@router.get("/", response_model=List[CarInDB])
def read_car(db: Session = Depends(get_db)):
    """
    Returns a list of all the car entries in the database.
    """

    return read_all(db_session=db)


@router.get("/{name}", response_model=CarInDB)
def read_car_by_name(*, db: Session = Depends(get_db), name: str):
    """
    Returns a Car specified by the name
    """

    try:
        existing_car = read_one(db_session=db, car_name=name)
    raise HTTPException(status_code=404, detail="Car not found")
    return existing_car


@router.put("/{car_id}", response_model=CarInDB)
def update_car(*, db: Session = Depends(get_db), car_id: int, car_info: CarUpdate):
    """
    Updates the Car specified by the ID field in the request body, with the rest of the body fields.
    """

   try:
        updated_car = update(db_session=db, car_id=car_id, obj_in=car_info)
    raise HTTPException(status_code=404, detail="Car not found")
    return updated_car


@router.delete("/{name}", response_model=CarInDB)
def delete_car(*, db: Session = Depends(get_db), name: str):
    """
    Deletes a Car specified by the name.
    """

    try:
        deleted_car = delete(db_session=db, car_name=name)
    raise HTTPException(status_code=404, detail="Car not found")
    return deleted_car
