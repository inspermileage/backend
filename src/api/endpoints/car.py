from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from src.api.utils.db import get_db
from src.crud.utils import ExistenceException, NonExistenceException
from src.schemas.car import CarCreate, CarInDB, CarUpdate
from src.models.car import Car as CarModel

router = APIRouter()


@router.post("/", response_model=CarInDB)
def create_car(*, db: Session = Depends(get_db), car_in: CarCreate):
    """
    Inserts a car into the car table, given the request body.
    """
    try:
        obj_in_data = jsonable_encoder(car_in)
        db_obj = CarModel(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    except Exception as err:
        raise HTTPException(status_code=500, detail=err)


@router.get("/", response_model=List[CarInDB])
def read_car(db: Session = Depends(get_db)):
    """
    Returns a list of all the car entries in the database.
    """

    return db.query(CarModel).all()


@router.get("/{name}", response_model=CarInDB)
def read_car(*, db: Session = Depends(get_db), name: str):
    """
    Returns a Car specified by the name
    """

    car_obj = db.query(CarModel).filter(CarModel.name == name).first()
    if not car_obj:
        raise HTTPException(status_code=404, detail="Car not found")
    return car_obj


@router.put("/{car_id}", response_model=CarInDB)
def update_car(*, db: Session = Depends(get_db), car_id: int, car_info: CarUpdate):
    """
    Updates the Car specified by the name field in the request body, with the rest of the body fields.
    """

    # Tries to find the car by name
    car_obj = db.query(CarModel).filter(CarModel.id == car_id).first()
    if not car_obj:
        raise HTTPException(status_code=404, detail="Car not found")

    # Iterates request body and updates the car object
    obj_data = jsonable_encoder(car_obj)
    update_data = car_info.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(car_obj, field, update_data[field])
    db.add(car_obj)
    db.commit()
    db.refresh(car_obj)
    return car_obj


@router.delete("/{name}", response_model=CarInDB)
def delete_car(*, db: Session = Depends(get_db), name: str):
    """
    Deletes a Car specified by the name.
    """

    car_obj = db.query(CarModel).filter(CarModel.name == name).first()
    if not car_obj:
        raise HTTPException(status_code=404, detail="Car not found")

    db.delete(car_obj)
    db.commit()
    return car_obj
