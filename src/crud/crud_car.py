from typing import Dict, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import date
from src.crud.utils import ExistenceException, NonExistenceException
from src.models.car import Car as CarModel
from src.schemas.car import CarCreate
 

def create(*, db: Session, car_in: CarCreate) -> CarModel:
    """Creates a row with new data in the Car table

    Args:
        db: a Session instance to execute queries in the database
        obj_in: a CarCreate object with the data to be inserted in the table

    Returns:
        The object CarModel that was inserted to the table

    Raises:
        HTTPException 
    """

    # Transforms object to dict
    obj_in_data: Dict = jsonable_encoder(car_in)

    # Unpacks dict values to the Telemetry database model
    db_obj: CarModel = CarModel(**obj_in_data)

    # Inserts the car data to the database
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def read_all(*, db: Session) -> List[CarModel]:
    """Fetches all Car from the table

    Args:
        db: a Session instance to execute queries in the database

    Returns:
       A list with the objects CarModel found by the query
    """

    obj_list: List[CarModel] = db.query(CarModel).all()
    return obj_list


def read_one(*, db: Session, name:str) -> CarModel:
    """Fetches from the table, a Car specified by the name

    Args:
        db: a Session instance to execute queries in the database
        name: the name of the Car

    Returns:
       The object CarModel found by the query

    Raises:
        HTTPException: if Car is not found
    """
    car_obj = db.query(CarModel).filter(CarModel.name == name).first()
    if not car_obj:
        raise HTTPException(status_code=404, detail="Car not found")
    return car_obj

def update(*, db: Session, car_id: int, car_info: CarUpdate) -> CarModel:
    
    # Tries to find the car by id
    car_obj = db.query(CarModel).filter(CarModel.id == car_id).first()
    if not car_obj:
        raise HTTPException(status_code=404, detail="id not found")

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


def delete(*, db: Session, name: str) -> CarModel:
    
    car_obj = db.query(CarModel).filter(CarModel.name == name).first()

    if not car_obj:
        raise HTTPException(status_code=404, detail="Car not found")

    db.delete(car_obj)
    db.commit()
    return car_obj
