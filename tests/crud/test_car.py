from sqlalchemy.orm import Session

from src.crud.crud_car import (create, delete, read_all,
                               read_one, update)
from src.schemas.car import CarCreate,CarUpdate
from typing import Dict, Generator
from src.models.car import Car as CarModel

import pytest
from src.database.session import Session


@pytest.fixture(scope="session")
def db() -> Generator:
    yield Session()


def test_create_item(db: Session) -> CarModel:
    name = 'testebia'
    description = 'testandoo'
    creation_date= "2020-06-04"

    item_in = CarCreate(name=name, description=description, creation_date=creation_date)

    item = create(db=db, car_in=item_in)
    assert item.name== name
    assert item.description == description
    assert item.id  is not None



