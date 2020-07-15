from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Reason(str, Enum):
    """
    This class models the reasons that can stored at the reason column. If the input value is not one of these values,
    the object will not validate.
    """

    test = "Test"
    competition = "Competition"
    inspection = "Inspection"


class RoundInDB(BaseModel):
    """
    This represents the object stored in the database, it is similar to the `/models/round`.
    """

    id: int
    name: str
    description: str
    ref_date: date
    reason: Reason
    track_id: int
    car_id: int
    class Config:
        orm_mode = True


class RoundCreate(BaseModel):
    """
    This class models the request body for creating a new Round in the database.
    """

    name: str
    description: Optional[str] = ""
    reason: Reason
    ref_date: Optional[date] = datetime.now().date()
    track_id: int
    car_id: int

class RoundUpdate(BaseModel):
    """
    This class models the request body for updating a existing Round in the database.
    """

    name: Optional[str]
    description: Optional[str]
    reason: Optional[Reason]
    ref_date: Optional[date]
    track_id: Optional[int]
    car_id: Optional[int]
