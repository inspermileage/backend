import random
import string

from src.crud.crud_track import create
from src.schemas.track import TrackCreate
from src.models.track import Track as TrackModel



def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def create_random_track(db: Session) -> TrackModel:
    name = random_lower_string()
    description = random_lower_string()

    item_in = TrackCreate(name=name, description=description)

    item = create(db_session=db, obj_in=item_in)
    return item
