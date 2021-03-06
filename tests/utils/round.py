import random
import string

from src.crud.crud_rounds import create
from src.database.session import Session
from src.models.round import Round as RoundModel
from src.schemas.round import RoundCreate
from tests.utils.car import create_random_car
from tests.utils.track import create_random_track


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def create_random_round(db: Session) -> RoundModel:
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
    return item
