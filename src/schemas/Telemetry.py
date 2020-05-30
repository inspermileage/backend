import datetime
from datetime import date, datetime, time
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class TelemetryInDB(BaseModel):
    """
    This represents the object stored in the database, it is similar to the `/models/car`.
    """

    id: int
    speed: float
    dist: float
    engine_temp: float
    telemetry_timestamp:  time
    energy_cons: float
    rpm: int
    batery: int
   # telemtery_timestamp: datetime
    class Config:
        orm_mode = True

class TelemetryCreate(BaseModel):
    """
    This class models the request body for creating a new Telemetry data in the database.
    """

   
    speed: float
    dist: float
    engine_temp: float
    telemetry_timestamp:  Optional[time] = datetime.now().time()
    energy_cons: float
    rpm: int
    batery: int
    #telemetry_timestamp: Optional[time] = datetime.now()
    round_id: int

class TelemetryUpdate(BaseModel):
    """
    This class models the request body for updating a existing Telemtry data in the database.
    """

    
    speed: Optional[float]
    dist: Optional[float]
    engine_temp: Optional[float]
    telemetry_timestamp: Optional[time]
    energy_cons: Optional[float]
    rpm: Optional[int]
    batery: Optional[int]
   # telemetry_timestamp: Optional[datetime]
    round_id: Optional[int]
