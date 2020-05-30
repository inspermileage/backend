from typing import Dict, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import date
from src.crud.utils import ExistenceException, NonExistenceException
from src.models.Telemetry import Telemetry as TelemetryModel
from src.schemas.Telemetry import TelemetryCreate, TelemetryUpdate


def create(*, db_session: Session, obj_in: TelemetryCreate) -> TelemetryModel:
    """Creates a row with new data in the Telemetry table

    Args:
        db_session: a Session instance to execute queries in the database
        obj_in: a TelemetryCreate object with the data to be inserted in the table

    Returns:
        The object TelemetryModel that was inserted to the table

    Raises:
        ExistenceException: if there is a Telemetry with the same name in the table
    """

    # Transforms object to dict
    in_data: Dict = jsonable_encoder(obj_in)

    # Unpacks dict values to the Telemetry database model
    db_obj: TelemetryModel = TelemetryModel(**in_data)

    telemetryelemetry_exists = db_session.query(TelemetryModel).filter(TelemetryModel.name == db_obj.name).first()

    if Telemetry_exists:
        raise ExistenceException(field=db_obj.name)

    # Inserts the telemetry data to the database
    db_session.add(db_obj)
    db_session.commit()
    db_session.refresh(db_obj)
    return db_obj


def read_one_by_id(*, db_session: Session, telemetryTelemetry_id: int) -> TelemetryModel:
    """Fetches from the table, a Telemetry specified by the id

    Args:
        db_session: a Session instance to execute queries in the database
        telemetry_id: the id of the Telemetry

    Returns:
       The object TelemetryModel found by the query

    Raises:
        NonExistenceException: if there is no Telemetry with the specified id
    """

    obj: TelemetryModel = db_session.query(TelemetryModel).filter(TelemetryModel.id == Telemetry_id).first()
    if not obj:
        raise NonExistenceException(field=str(Telemetry_id))
    return obj


def read_one_by_date(*, db_session: Session, telemetryelemetry_ref_date: date) ->TelemetryModel:
    """Fetches from the table, a Telemetry specified by the id

    Args:
        db_session: a Session instance to execute queries in the database
        telemetry_id: the id of the Telemetry

    Returns:
       The object TelemetryModel found by the query

    Raises:
        NonExistenceException: if there is no telemetry with the specified id
    """

    obj: TelemetryModel = db_session.query(TelemetryModel).filter(TelemetryModel.id == Telemetry_id).first()
    if not obj:
        raise NonExistenceException(field=str(telemetry_ref_date))
    return obj

    


def read_all(*, db_session: Session) -> List[TelemetryModel]:
    """Fetches all Telemetry from the table

    Args:
        db_session: a Session instance to execute queries in the database

    Returns:
       A list with the objects TelemetryModel found by the query
    """

    obj_list: List[TelemetryModel] = db_session.query(TelemetryModel).all()
    return obj_list


def update(*, db_session: Session, Telemetry_id: int, obj_in: TelemetryUpdate) -> TelemetryModel:
    """Updates a Car from the table, specified by the id

    Args:
        db_session: a Session instance to execute queries in the database
        car_id: the id of the Telemetry
        obj_in: a TelemetryUpdate object with the data to be updated in the Telemetry specified by id

    Returns:
        The object TelemetryModel updated by the query

    Raises:
        NonExistenceException: if there is no telemetry with the specified id
    """

    Telemetry_exists: TelemetryModel = db_session.query(TelemetryModel).filter(
        TelemetryModel.id == Telemetry_id).first()
    if not Telemetry_exists:
        raise NonExistenceException(field=str(Telemetry_id))

    # Transforms object to dict
    existing_Telemetry: Dict = jsonable_encoder(Telemetry_exists)
    update_data = obj_in.dict(exclude_unset=True)

    for field in existing_Telemetry:
        if field in update_data:
            setattr(Telemetry_exists, field, update_data[field])

    db_session.add(Telemetry_exists)
    db_session.commit()
    db_session.refresh(Telemetry_exists)
    return Telemetry_exists


def delete(*, db_session: Session, Telemetry_id: int) -> TelemetryModel:
    """Deletes from the table, a Telemetry specified by the id

    Args:
        db_session: a Session instance to execute queries in the database
        Telemetry_id: the id of the Telemetry

    Returns:
       The object TelemetryModel deleted by the query

    Raises:
        NonExistenceException: if there is no Telemetry with the specified id
    """
    Telemetry_exists: TelemetryModel = db_session.query(TelemetryModel).filter(
        TelemetryModel.id == Telemetry_id).first()
    if not Telemetry_exists:
        raise NonExistenceException(field=str(Telemetry_id))

    db_session.delete(Telemetry_exists)
    db_session.commit()
    return Telemetry_exists
