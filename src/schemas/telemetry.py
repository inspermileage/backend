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
    distance: float
    engine_temp: float
    creation_time :  datetime
    energy_cons: float
    rpm: int
    battery: int
    round_id: int

   # telemtery_timestamp: datetime
    class Config:
        orm_mode = True

class TelemetryCreate(BaseModel):
    """
    This class models the request body for creating a new Telemetry data in the database.
    """


    speed: float
    distance: float
    engine_temp: float
    creation_time : datetime=datetime.now().timestamp()
    energy_cons: float
    rpm: int
    battery: int
    #telemetry_timestamp: Optional[time] = datetime.now()
    round_id: int

class TelemetryOutDB(BaseModel):

    id: int
    class Config:
        orm_mode = True

# class TelemetryUpdate(BaseModel):
#     """
#     This class models the request body for updating a existing Telemtry data in the database.
#     """

    
#     speed: Optional[float]
#     distance: Optional[float]
#     engine_temp: Optional[float]
#     energy_cons: Optional[float]
#     rpm: Optional[int]
#     battery: Optional[int]
#    # telemetry_timestamp: Optional[datetime]
#     round_id: Optional[int]
