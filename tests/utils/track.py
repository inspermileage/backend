from sqlalchemy.orm import Session
import random
import string
from typing import Dict
from src.crud.crud_track import (create, delete, read_all, read_one_by_name, update)
from src.schemas.track import TrackCreate,TrackUpdate
from typing import Dict, Generator
from src.models.track import Track as TrackModel
from src.crud.utils import ExistenceException, NonExistenceException
import pytest
from src.database.session import Session

def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))

def create_random_track(db: Session) -> TrackModel:
    name = random_lower_string()
    description = random_lower_string()

    item_in = TrackCreate(name=name, description=description)

    item = create(db_session=db, obj_in=item_in)
    return item
    