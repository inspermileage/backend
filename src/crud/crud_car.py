from typing import Dict, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import date
from src.crud.utils import ExistenceException, NonExistenceException
from src.models.car import Car as CarModel
from src.schemas.car import CarCreate, CarUpdate



def create(*, db_session: Session, obj_in: CarCreate) -> CarModel:
    """Creates a row with new data in the Car table

    Args:
        db_session: a Session instance to execute queries in the database
        obj_in: a CarCreate object with the data to be inserted in the table

    Returns:
        The object CarModel that was inserted to the table

    Raises:
        ExistenceException: if there is a Car with the same name in the table
    """

    # Transforms object to dict
    in_data: Dict = jsonable_encoder(obj_in)

    # Unpacks dict values to the Car database model
    db_obj: CarModel = CarModel(**in_data)

    car_exists = db_session.query(CarModel).filter(CarModel.name == db_obj.name).first()

    if car_exists:
        raise ExistenceException(field=db_obj.name)

    # Inserts the car data to the database
    db_session.add(db_obj)
    db_session.commit()
    db_session.refresh(db_obj)
    return db_obj


def read_one_by_id(*, db_session: Session, car_id: int) -> CarModel:
    """Fetches from the table, a Car specified by the id

    Args:
        db_session: a Session instance to execute queries in the database
        Car_id: the id of the Car

    Returns:
       The object CarModel found by the query

    Raises:
        NonExistenceException: if there is no Car with the specified id
    """

    obj: CarModel = db_session.query(CarModel).filter(CarModel.id == car_id).first()
    if not obj:
        raise NonExistenceException(field=str(car_id))
    return obj


def read_one_by_date(*, db_session: Session, car_ref_date: date) -> CarModel:
    """Fetches from the table, a Car specified by the id

    Args:
        db_session: a Session instance to execute queries in the database
        car_id: the id of the Car

    Returns:
       The object CarModel found by the query

    Raises:
        NonExistenceException: if there is no car with the specified id
    """

    obj: CarModel = db_session.query(CarModel).filter(CarModel.id == car_id).first()
    if not obj:
        raise NonExistenceException(field=str(car_ref_date))
    return obj

    


def read_all(*, db_session: Session) -> List[CarModel]:
    """Fetches all Cars from the table

    Args:
        db_session: a Session instance to execute queries in the database

    Returns:
       A list with the objects CarModel found by the query
    """

    obj_list: List[CaModel] = db_session.query(CarModel).all()
    return obj_list


def update(*, db_session: Session, car_id: int, obj_in: CarUpdate) -> CarModel:
    """Updates a Car from the table, specified by the id

    Args:
        db_session: a Session instance to execute queries in the database
        car_id: the id of the Car
        obj_in: a CarUpdate object with the data to be updated in the Car specified by id

    Returns:
        The object CarModel updated by the query

    Raises:
        NonExistenceException: if there is no car with the specified id
    """

    Car_exists: CarModel = db_session.query(CarModel).filter(
        CarModel.id == car_id).first()
    if not Car_exists:
        raise NonExistenceException(field=str(car_id))

    # Transforms object to dict
    existing_car: Dict = jsonable_encoder(car_exists)
    update_data = obj_in.dict(exclude_unset=True)

    for field in existing_car:
        if field in update_data:
            setattr(car_exists, field, update_data[field])

    db_session.add(car_exists)
    db_session.commit()
    db_session.refresh(car_exists)
    return car_exists


def delete(*, db_session: Session, car_id: int) -> CarModel:
    """Deletes from the table, a Car specified by the id

    Args:
        db_session: a Session instance to execute queries in the database
        Car_id: the id of the Car

    Returns:
       The object CarModel deleted by the query

    Raises:
        NonExistenceException: if there is no car with the specified id
    """
    car_exists: CarModel = db_session.query(CarModel).filter(
        CarModel.id == car_id).first()
    if not car_exists:
        raise NonExistenceException(field=str(car_id))

    db_session.delete(car_exists)
    db_session.commit()
    return car_exists
