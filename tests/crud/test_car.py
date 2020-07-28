from sqlalchemy.orm import Session
import random
import string
from typing import Dict
from src.crud.crud_car import (create, delete, read_all,
                               read_one, update)
from src.schemas.car import CarCreate,CarUpdate
from typing import Dict, Generator
from src.models.car import Car as CarModel

from src.crud.utils import ExistenceException, NonExistenceException


import pytest
from src.database.session import Session


@pytest.fixture(scope="session")
def db() -> Generator:
    yield Session()

def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def test_create_item(db: Session) -> CarModel:
    name = random_lower_string()
    description = random_lower_string()
    creation_date= "2020-06-04"

    item_in = CarCreate(name=name, description=description, creation_date=creation_date)

    item = create(db=db, car_in=item_in)
    assert item.name== name
    assert item.description == description
    assert item.id  is not None


def test_create_duplicate_item(db: Session) -> CarModel:
    name = random_lower_string()
    description = random_lower_string()
    creation_date= "2020-06-04"

    item_in = CarCreate(name=name, description=description, creation_date=creation_date)

    item = create(db=db, car_in=item_in)
    assert item.name== name
    assert item.description == description
    assert item.id  is not None
    with pytest.raises(ExistenceException) :

        second_item= create(db=db, car_in=item_in)
    

    

def test_read_all(db: Session) -> CarModel:
  
    read_item=read_all(db=db)

    assert type(read_item) == list




def test_read_one(db: Session) -> CarModel:
  
    name = random_lower_string()
    description = random_lower_string()
    creation_date= "2020-06-04"

    item_in = CarCreate(name=name, description=description, creation_date=creation_date)

    item = create(db=db, car_in=item_in)
    item_name= item.name
    read_item= read_one(db_session=db, name=item_name)
    assert read_item.description == description
    assert read_item.creation_date.strftime('%Y-%m-%d') == creation_date

def test_read_invalid_one(db: Session) -> CarModel:
  
    name='bla'
    with pytest.raises(NonExistenceException) :
        read_item= read_one(db_session=db, name=name)




def test_update(db: Session) -> CarModel:

    name = random_lower_string()
    description = random_lower_string()
    creation_date= "2020-06-04"
    item_in = CarCreate(name=name, description=description, creation_date=creation_date)
    item = create(db=db, car_in=item_in)
    item_id=item.id
    
    item_update= CarUpdate(name= random_lower_string(), description= random_lower_string())
    updated_car = update(db=db, car_id=item_id, car_info=item_update)

    assert updated_car.name == item_update.name
    assert updated_car.description== item_update.description


def test_update_invalid_one(db: Session) -> CarModel:
    
    item_id=1239083330988
    item_update= CarUpdate(name= random_lower_string(), description= random_lower_string())
    with pytest.raises(NonExistenceException) :

     updated_car = update(db=db, car_id=item_id, car_info=item_update)

    

   
def test_delete(db: Session) -> CarModel:

    name = random_lower_string()
    description = random_lower_string()
    creation_date= "2020-06-04"
    item_in = CarCreate(name=name, description=description, creation_date=creation_date)
    item = create(db=db, car_in=item_in)
    item_name=item.name
    
    delete_item= delete(db=db, name=item_name)

    assert delete_item.name== name

   
def test_delete_invalid_one(db: Session) -> CarModel:
  
    name='bla'
    with pytest.raises(NonExistenceException) :
        delete_item= delete(db=db, name=name)


    
