from datetime import datetime
from pydantic import BaseModel


class TelemetryInDB(BaseModel):
    """
    This represents the object stored in the database, it is similar to the `/models/Telemetry`.
    """

    id: int
    speed: float
    distance: float
    engine_temp: float
    creation_time: datetime
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
    creation_time: datetime = datetime.now().timestamp()
    energy_cons: float
    rpm: int
    battery: int
    round_id: int


class TelemetryOutDB(BaseModel):

    id: int

    class Config:
        orm_mode = True
