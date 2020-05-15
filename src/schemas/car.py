from pydantic import BaseModel, Field
from datetime import date, datetime, time
from enum import Enum
from typing import Optional



class CarInDB(BaseModel):
    """
    This represents the object stored in the database, it is similar to the `/models/car`.
    """

    id: int
    name: str
    description: str
    inst_vel: float
    ref_date: date
    dist: float
    engine_temp: float
    time:  time
    energy_cons: float
    rpm: int
    batery: int
    round_id: int
    class Config:
        orm_mode = True

class CarCreate(BaseModel):
    """
    This class models the request body for creating a new Round in the database.
    """

    name: Optional[str]=""
    description: Optional[str]= ""
    inst_vel: float
    ref_date: Optional[date] = datetime.now().date()
    dist: float
    engine_temp: float
    time:  time
    energy_cons: float
    rpm: int
    batery: int
    round_id: int

class CarUpdate(BaseModel):
    """
    This class models the request body for updating a existing Round in the database.
    """

    name: Optional[str]
    description: Optional[str]
    inst_vel: Optional[float]
    ref_date: Optional[date]
    dist: Optional[float]
    engine_temp: Optional[float]
    time: Optional[time]
    energy_cons: Optional[float]
    rpm: Optional[int]
    batery: Optional[int]
    round_id: Optional[int]
