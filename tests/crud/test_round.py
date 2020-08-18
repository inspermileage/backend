from typing import Generator
import pytest
from src.database.session import Session
from src.crud.crud_rounds import create, delete, read_all, read_one, update
from src.crud.utils import ExistenceException, NonExistenceException
from src.models.round import Round as RoundModel
from src.schemas.round import RoundCreate, RoundUpdate
from tests.utils.car import create_random_car
from tests.utils.randomString import random_lower_string
from tests.utils.track import create_random_track


@pytest.fixture(scope="session")
def db() -> Generator:
    yield Session()


def test_create_item(db: Session) -> RoundModel:
    # creates one car and one track in table
    car = create_random_car(db)
    track = create_random_track(db)
    name = random_lower_string()
    description = random_lower_string()
    reason = "Test"
    ref_date = "2020-08-01"
    track_id = track.id
    car_id = car.id

    item_in = RoundCreate(name=name, description=description, reason=reason,
                          ref_date=ref_date, track_id=track_id, car_id=car_id)

    item = create(db_session=db, obj_in=item_in)
    assert item.name == name
    assert item.description == description
    assert item.reason == reason
    assert item.track_id == track_id
    assert item.car_id == car_id
    assert item.id is not None


def test_create_duplicate_item(db: Session) -> RoundModel:
    # creates one car and one track in table
    car = create_random_car(db)
    track = create_random_track(db)
    name = random_lower_string()
    description = random_lower_string()
    reason = "Test"
    ref_date = "2020-08-01"
    track_id = track.id
    car_id = car.id

    item_in = RoundCreate(name=name, description=description, reason=reason,
                          ref_date=ref_date, track_id=track_id, car_id=car_id)

    item = create(db_session=db, obj_in=item_in)
    assert item.name == name
    assert item.description == description
    assert item.reason == reason
    assert item.track_id == track_id
    assert item.car_id == car_id
    assert item.id is not None
    with pytest.raises(ExistenceException):
        create(db_session=db, obj_in=item_in)


def test_read_all(db: Session) -> RoundModel:
    read_item = read_all(db_session=db)
    assert type(read_item) == list


def test_read_one(db: Session) -> RoundModel:
    # creates one car and one track in table
    car = create_random_car(db)
    track = create_random_track(db)
    name = random_lower_string()
    description = random_lower_string()
    reason = "Test"
    ref_date = "2020-08-01"
    track_id = track.id
    car_id = car.id

    item_in = RoundCreate(name=name, description=description, reason=reason,
                          ref_date=ref_date, track_id=track_id, car_id=car_id)

    item = create(db_session=db, obj_in=item_in)
    item_id = item.id
    read_item = read_one(db_session=db, round_id=item_id)
    assert read_item.name == name
    assert read_item.description == description
    assert read_item.reason == reason
    assert read_item.track_id == track_id
    assert read_item.car_id == car_id


def test_read_invalid_one(db: Session) -> RoundModel:
    item_id = 0
    with pytest.raises(NonExistenceException):
        read_one(db_session=db, round_id=item_id)


def test_update(db: Session) -> RoundModel:
    # creates one car and one track in table
    car = create_random_car(db)
    track = create_random_track(db)

    name = random_lower_string()
    description = random_lower_string()
    reason = "Test"
    ref_date = "2020-08-01"
    track_id = track.id
    car_id = car.id

    item_in = RoundCreate(name=name, description=description, reason=reason,
                          ref_date=ref_date, track_id=track_id, car_id=car_id)

    item = create(db_session=db, obj_in=item_in)

    item_update = RoundUpdate(name=random_lower_string(), description=random_lower_string(), reason=reason,
                              ref_date=ref_date, track_id=track_id, car_id=car_id)
    updated_round = update(db_session=db, round_id=item.id, obj_in=item_update)

    assert updated_round.name == item_update.name
    assert updated_round.description == item_update.description


def test_update_invalid_one(db: Session) -> RoundModel:
    item_id = 123456789
    item_update = RoundUpdate(
        name=random_lower_string(), description=random_lower_string())
    with pytest.raises(NonExistenceException):
        update(db_session=db, round_id=item_id, obj_in=item_update)


def test_delete(db: Session) -> RoundModel:
    # creates one car and one track in table
    car = create_random_car(db)
    track = create_random_track(db)

    name = random_lower_string()
    description = random_lower_string()
    reason = "Test"
    ref_date = "2020-08-01"
    track_id = track.id
    car_id = car.id

    item_in = RoundCreate(name=name, description=description, reason=reason,
                          ref_date=ref_date, track_id=track_id, car_id=car_id)
    item = create(db_session=db, obj_in=item_in)
    item_id = item.id

    delete_item = delete(db_session=db, round_id=item_id)

    assert delete_item.name == name


def test_delete_invalid_one(db: Session) -> RoundModel:

    item_id = 987654321
    with pytest.raises(NonExistenceException):
        delete(db_session=db, round_id=item_id)
