from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from src.api.utils.db import get_db
from src.crud.utils import ExistenceException, NonExistenceException
from src.schemas.car2 import Car2Create, Car2InDB, Car2Update
from src.models.car2 import Car2 as Car2Model

router = APIRouter()


@router.post("/", response_model=Car2InDB)
def create_car2(*, db: Session = Depends(get_db), car2_in: Car2Create):
    """
    Inserts a car2 into the car2 table, given the request body.
    """
    try:
        obj_in_data = jsonable_encoder(car2_in)
        db_obj = Car2Model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    except Exception as err:
        raise HTTPException(status_code=500, detail=err)


@router.get("/", response_model=List[Car2InDB])
def read_car2(db: Session = Depends(get_db)):
    """
    Returns a list of all the car2 entries in the database.
    """

    return db.query(Car2Model).all()


@router.get("/{name}", response_model=Car2InDB)
def read_car2(*, db: Session = Depends(get_db), name: str):
    """
    Returns a Car2 specified by the name
    """

    car2_obj = db.query(Car2Model).filter(Car2Model.name == name).first()
    if not car2_obj:
        raise HTTPException(status_code=404, detail="Car2 not found")
    return car2_obj


@router.put("/", response_model=Car2InDB)
def update_car2(*, db: Session = Depends(get_db), car2_info: Car2Update):
    """
    Updates the Car specified by the name field in the request body, with the rest of the body fields.
    """

    # Tries to find the car by name
    car2_obj = db.query(Car2Model).filter(Car2Model.name == car2_info.name).first()
    if not car2_obj:
        raise HTTPException(status_code=404, detail="Ca not found")

    # Iterates request body and updates the car object
    obj_data = jsonable_encoder(car2_obj)
    update_data = car2_info.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(car2_obj, field, update_data[field])
    db.add(car2_obj)
    db.commit()
    db.refresh(car2_obj)
    return car2_obj


@router.delete("/{name}", response_model=Car2InDB)
def delete_car2(*, db: Session = Depends(get_db), name: str):
    """
    Deletes a Car specified by the name.
    """

    car2_obj = db.query(Car2Model).filter(Car2Model.name == name).first()
    if not car2_obj:
        raise HTTPException(status_code=404, detail="Car2 not found")

    db.delete(car2_obj)
    db.commit()
    return car2_obj
