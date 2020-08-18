import random
import string
from typing import Dict, Generator

import pytest
from sqlalchemy.orm import Session

from src.crud.crud_track import (create, delete, read_all, read_one_by_name,
                                 update)
from src.crud.utils import ExistenceException, NonExistenceException
from src.database.session import Session
from src.models.track import Track as TrackModel
from src.schemas.track import TrackCreate, TrackUpdate


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))

def create_random_track(db: Session) -> TrackModel:
    name = random_lower_string()
    description = random_lower_string()

    item_in = TrackCreate(name=name, description=description)

    item = create(db_session=db, obj_in=item_in)
    return item
