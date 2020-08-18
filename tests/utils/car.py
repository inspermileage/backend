import random
import string
from typing import Dict, Generator

import pytest
from sqlalchemy.orm import Session

from src.crud.crud_car import create, delete, read_all, read_one, update
from src.crud.utils import ExistenceException, NonExistenceException
from src.database.session import Session
from src.models.car import Car as CarModel
from src.schemas.car import CarCreate, CarUpdate


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))

def create_random_car(db: Session) -> CarModel:
    name = random_lower_string()
    description = random_lower_string()
    creation_date= "2020-06-04"

    item_in = CarCreate(name=name, description=description, creation_date=creation_date)

    item = create(db=db, car_in=item_in)
    return item
