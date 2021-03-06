from typing import Dict, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from src.crud.utils import ExistenceException, NonExistenceException
from src.models.track import Track as TrackModel
from src.schemas.track import TrackCreate, TrackUpdate


def create(*, db_session: Session, obj_in: TrackCreate) -> TrackModel:
    """Creates a row with new data in the Track table

    Args:
        db_session: a Session instance to execute queries in the database
        obj_in: a TrackCreate object with the data to be inserted in the table

    Returns:
        The object TrackModel that was inserted to the table

    Raises:
        ExistenceException: if there is a Track with the same name in the table
    """

    # Transforms object to dict
    in_data: Dict = jsonable_encoder(obj_in)

    # Unpacks dict values to the Track database model
    db_obj: TrackModel = TrackModel(**in_data)

    track_exists = db_session.query(TrackModel).filter(
        TrackModel.name == db_obj.name).first()

    if track_exists:
        raise ExistenceException(field=db_obj.name)

    # Inserts the telemetry data to the database
    db_session.add(db_obj)
    db_session.commit()
    db_session.refresh(db_obj)
    return db_obj


def read_one_by_name(*, db_session: Session, Track_name: str) -> TrackModel:
    """Fetches from the table, a Track specified by the name

    Args:
        db_session: a Session instance to execute queries in the database
        telemetry_name: the name of the Track

    Returns:
       The object TrackModel found by the query

    Raises:
        NonExistenceException: if there is no Track with the specified name
    """

    obj: TrackModel = db_session.query(TrackModel).filter(
        TrackModel.name == Track_name).first()
    if not obj:
        raise NonExistenceException(field=str(Track_name))
    return obj


def read_all(*, db_session: Session) -> List[TrackModel]:
    """Fetches all Tracks from the table

    Args:
        db_session: a Session instance to execute queries in the database

    Returns:
       A list with the objects TrackModel found by the query
    """

    obj_list: List[TrackModel] = db_session.query(TrackModel).all()
    return obj_list


def update(*, db_session: Session, track_name: str, obj_in: TrackUpdate) -> TrackModel:
    """Updates a Track from the table, specified by the name

    Args:
        db_session: a Session instance to execute queries in the database
        track_name: the name of the Track
        obj_in: a TrackUpdate object with the data to be updated in the Track specified by id

    Returns:
        The object TrackModel updated by the query

    Raises:
        NonExistenceException: if there is no round with the specified id
    """

    track_exists: TrackModel = db_session.query(TrackModel).filter(
        TrackModel.name == track_name).first()
    if not track_exists:
        raise NonExistenceException(field=str(track_name))

    # Transforms object to dict
    existing_track: Dict = jsonable_encoder(track_exists)
    update_data = obj_in.dict(exclude_unset=True)

    for field in existing_track:
        if field in update_data:
            setattr(track_exists, field, update_data[field])

    db_session.add(track_exists)
    db_session.commit()
    db_session.refresh(track_exists)
    return track_exists


def delete(*, db_session: Session, track_name: str) -> TrackModel:
    """Deletes from the table, a Track specified by the name

    Args:
        db_session: a Session instance to execute queries in the database
        Track_name: the name of the Track

    Returns:
       The object TrackModel deleted by the query

    Raises:
        NonExistenceException: if there is no Track with the specified name
    """
    Track_exists: TrackModel = db_session.query(TrackModel).filter(
        TrackModel.name == track_name).first()
    if not Track_exists:
        raise NonExistenceException(field=str(track_name))

    db_session.delete(Track_exists)
    db_session.commit()
    return Track_exists
