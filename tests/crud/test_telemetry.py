from sqlalchemy.orm import Session
from src.crud.crud_telemetry import (create,read_one_by_id, read_all, delete) 
                           
from src.schemas.telemetry import TelemetryCreate
from typing import Dict, Generator
from src.models.telemetry import Telemetry as TelemetryModel
from tests.utils.round import create_random_round
from src.crud.utils import ExistenceException, NonExistenceException

import pytest
from src.database.session import Session

@pytest.fixture(scope="session")
def db_session() -> Generator:
    yield Session()


def test_create_item(db_session: Session) -> TelemetryModel:
    round=create_random_round(db_session)
    speed= 24.4
    distance= 120.7
    engine_temp= 20.3
    creation_time =  "2020-11-04 00:05:23"
    energy_cons= 27.9
    rpm= 800
    battery= 60
    round_id=round.id
    item_in = TelemetryCreate(speed=speed, distance=distance, engine_temp=engine_temp, creation_time=creation_time, energy_cons=energy_cons, rpm=rpm, battery=battery,round_id=round_id)

    item = create(db_session=db_session, obj_in=item_in)
    assert item.speed== speed
    assert item.distance == distance
    assert item.engine_temp == engine_temp
    assert item.creation_time.strftime("%Y-%m-%d %H:%M:%S") == creation_time
    assert item.energy_cons == energy_cons
    assert item.rpm == rpm
    assert item.battery == battery
    assert item.id  is not None


def test_read_one_by_id(db_session: Session) -> TelemetryModel:
    round=create_random_round(db_session)
    speed= 24.4
    distance= 120.7
    engine_temp= 20.3
    creation_time =  "2020-11-04 00:05:23"
    energy_cons= 27.9
    rpm= 800
    battery= 60
    round_id=round.id
    item_in = TelemetryCreate(speed=speed, distance=distance, engine_temp=engine_temp, creation_time=creation_time, energy_cons=energy_cons, rpm=rpm, battery=battery,round_id=round_id)
    item = create(db_session=db_session, obj_in=item_in)
    item_id= item.id
    read_item= read_one_by_id(db_session=db_session, Telemetry_id=item_id)
    assert read_item.speed== speed
    assert read_item.distance == distance
    assert read_item.engine_temp == engine_temp
    assert read_item.creation_time.strftime("%Y-%m-%d %H:%M:%S") == creation_time
    assert read_item.energy_cons == energy_cons
    assert read_item.rpm == rpm
    assert read_item.battery == battery


def test_read_all(db_session: Session) -> TelemetryModel:
  
    read_item=read_all(db_session=db_session)

    assert type(read_item) == list


def test_delete(db_session: Session) -> TelemetryModel:
    round=create_random_round(db_session)
    speed= 24.4
    distance= 120.7
    engine_temp= 20.3
    creation_time =  "2020-11-04 00:05:23.283+00:00"
    energy_cons= 27.9
    rpm= 800
    battery= 60
    round_id=round.id
    item_in = TelemetryCreate(speed=speed, distance=distance, engine_temp=engine_temp, creation_time=creation_time, energy_cons=energy_cons, rpm=rpm, battery=battery,round_id=round_id)
    item = create(db_session=db_session, obj_in=item_in)
    item_id=item.id
    
    delete_item= delete(db_session=db_session, telemetry_id=item_id)

    assert delete_item.id == item_id