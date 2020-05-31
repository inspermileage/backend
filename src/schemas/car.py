from pydantic import BaseModel, Field
from datetime import date, datetime, time
from enum import Enum
from typing import Optional



class TelemetryInDB(BaseModel):
    """
    This represents the object stored in the database, it is similar to the `/models/car`.
    """

    id: int
    speed: float
    dist: float
    engine_temp: float
    ref_time:  time
    energy_cons: float
    rpm: int
    batery: int
    round_id: int
    class Config:
        orm_mode = True

class TelemetryCreate(BaseModel):
    """

    This class models the request body for creating a new Telemetry data in the database.

    """

   
    speed: float
    dist: float
    engine_temp: float
    ref_time:  Optional[time] = datetime.now().time()
    energy_cons: float
    rpm: int
    batery: int
    round_id: int

class TelemetryUpdate(BaseModel):
    """

    This class models the request body for updating a existing Telemtry data in the database.

    """

    
    speed: Optional[float]
    dist: Optional[float]
    engine_temp: Optional[float]
    ref_time: Optional[time]
    energy_cons: Optional[float]
    rpm: Optional[int]
    batery: Optional[int]
    round_id: Optional[int]
