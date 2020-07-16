from typing import Dict, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from src.crud.utils import ExistenceException, NonExistenceException
from src.models.car import Car as CarModel
from src.models.round import Round as RoundModel
from src.schemas.car import CarCreate, CarUpdate
from src.schemas.round import RoundCreate, RoundUpdate


def create(*, db_session: Session, obj_in: RoundCreate) -> RoundModel:
    """Creates a row with new data in the Round table

    Args:
        db_session: a Session instance to execute queries in the database
        obj_in: a RoundCreate object with the data to be inserted in the table

    Returns:
        The object RoundModel that was inserted to the table

    Raises:
        ExistenceException: if there is a Round with the same name in the table
    """

    # Transforms object to dict
    in_data: Dict = jsonable_encoder(obj_in)

    # Unpacks dict values to the Round database model
    db_obj: RoundModel = RoundModel(**in_data)

    round_exists = db_session.query(RoundModel).filter(RoundModel.name == db_obj.name).first()

    if round_exists:
        raise ExistenceException(field=db_obj.name)

    # Inserts the round data to the database
    db_session.add(db_obj)
    db_session.commit()
    db_session.refresh(db_obj)
    return db_obj


def read_one(*, db_session: Session, round_id: int) -> RoundModel:
    """Fetches from the table, a Round specified by the id

    Args:
        db_session: a Session instance to execute queries in the database
        round_id: the id of the Round

    Returns:
       The object RoundModel found by the query

    Raises:
        NonExistenceException: if there is no round with the specified id
    """

    obj: RoundModel = db_session.query(RoundModel).filter(RoundModel.id == round_id).first()
    if not obj:
        raise NonExistenceException(field=str(round_id))
    return obj


def read_all(*, db_session: Session) -> List[RoundModel]:
    """Fetches all Rounds from the table

    Args:
        db_session: a Session instance to execute queries in the database

    Returns:
       A list with the objects RoundModel found by the query
    """

    obj_list: List[RoundModel] = db_session.query(RoundModel).all()
    return obj_list


def update(*, db_session: Session, round_id: int, obj_in: RoundUpdate) -> RoundModel:
    """Updates a Round from the table, specified by the id

    Args:
        db_session: a Session instance to execute queries in the database
        round_id: the id of the Round
        obj_in: a RoundUpdate object with the data to be updated in the round specified by id

    Returns:
        The object RoundModel updated by the query

    Raises:
        NonExistenceException: if there is no round with the specified id
    """

    round_exists: RoundModel = db_session.query(RoundModel).filter(
        RoundModel.id == round_id).first()
    if not round_exists:
        raise NonExistenceException(field=str(round_id))

    # Transforms object to dict
    existing_round: Dict = jsonable_encoder(round_exists)
    update_data = obj_in.dict(exclude_unset=True)

    for field in existing_round:
        if field in update_data:
            setattr(round_exists, field, update_data[field])

    db_session.add(round_exists)
    db_session.commit()
    db_session.refresh(round_exists)
    return round_exists


def delete(*, db_session: Session, round_id: int) -> RoundModel:
    """Deletes from the table, a Round specified by the id

    Args:
        db_session: a Session instance to execute queries in the database
        round_id: the id of the Round

    Returns:
       The object RoundModel deleted by the query

    Raises:
        NonExistenceException: if there is no round with the specified id
    """
    round_exists: RoundModel = db_session.query(RoundModel).filter(
        RoundModel.id == round_id).first()
    if not round_exists:
        raise NonExistenceException(field=str(round_id))

    db_session.delete(round_exists)
    db_session.commit()
    return round_exists

# def create(*, db_session: Session, obj_in: CarCreate) -> CarModel:
 
#     # Transforms object to dict
#     in_data: Dict = jsonable_encoder(obj_in)

#     # Unpacks dict values to the Round database model
#     db_obj: CarModel = CarModel(**in_data)

#     round_exists = db_session.query(CarModel).filter(CarModel.name == db_obj.name).first()

#     if round_exists:
#         raise ExistenceException(field=db_obj.name)

#     # Inserts the round data to the database
#     db_session.add(db_obj)
#     db_session.commit()
#     db_session.refresh(db_obj)
#     return db_obj
