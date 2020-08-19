from typing import Generator

import pytest

from src.crud.crud_track import (create, delete, read_all, read_one_by_name,
                                 update)
from src.crud.utils import ExistenceException, NonExistenceException
from src.database.session import Session
from src.models.track import Track as TrackModel
from src.schemas.track import TrackCreate, TrackUpdate
from tests.utils.randomString import random_lower_string


@pytest.fixture(scope="session")
def db() -> Generator:
    yield Session()


def test_create_item(db: Session) -> TrackModel:
    name = random_lower_string()
    description = random_lower_string()

    item_in = TrackCreate(name=name, description=description)

    item = create(db_session=db, obj_in=item_in)
    assert item.name == name
    assert item.description == description
    assert item.id is not None


def test_create_duplicate_item(db: Session) -> TrackModel:
    name = random_lower_string()
    description = random_lower_string()

    item_in = TrackCreate(name=name, description=description)

    item = create(db_session=db, obj_in=item_in)
    assert item.name == name
    assert item.description == description
    assert item.id is not None
    with pytest.raises(ExistenceException):
        create(db_session=db, obj_in=item_in)


def test_read_all(db: Session) -> TrackModel:
    read_item = read_all(db_session=db)
    assert type(read_item) == list


def test_read_one(db: Session) -> TrackModel:
    name = random_lower_string()
    description = random_lower_string()

    item_in = TrackCreate(name=name, description=description)

    item = create(db_session=db, obj_in=item_in)
    item_name = item.name
    read_item = read_one_by_name(db_session=db, Track_name=item_name)
    assert read_item.description == description


def test_read_invalid_one(db: Session) -> TrackModel:
    name = 'errorErrorError'
    with pytest.raises(NonExistenceException):
        read_one_by_name(db_session=db, Track_name=name)


def test_update(db: Session) -> TrackModel:
    name = random_lower_string()
    description = random_lower_string()
    item_in = TrackCreate(name=name, description=description)
    create(db_session=db, obj_in=item_in)

    item_update = TrackUpdate(
        name=random_lower_string(), description=random_lower_string())
    updated_track = update(db_session=db, track_name=name, obj_in=item_update)

    assert updated_track.name == item_update.name
    assert updated_track.description == item_update.description


def test_update_invalid_one(db: Session) -> TrackModel:
    name = "errorError yes Mistake"
    item_update = TrackUpdate(
        name=random_lower_string(), description=random_lower_string())
    with pytest.raises(NonExistenceException):
        update(db_session=db, track_name=name, obj_in=item_update)


def test_delete(db: Session) -> TrackModel:

    name = random_lower_string()
    description = random_lower_string()
    item_in = TrackCreate(name=name, description=description)
    item = create(db_session=db, obj_in=item_in)
    item_name = item.name

    delete_item = delete(db_session=db, track_name=item_name)

    assert delete_item.name == name


def test_delete_invalid_one(db: Session) -> TrackModel:

    name = 'bla'
    with pytest.raises(NonExistenceException):
        delete(db_session=db, track_name=name)
