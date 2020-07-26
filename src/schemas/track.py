from typing import Optional

from pydantic import BaseModel, Field


class TrackInDB(BaseModel):
    """
    This represents the object stored in the database, it is similar to the `/models/track`.
    """

    id: int
    name: str
    description: str

    class Config:
        orm_mode = True


class TrackOutDB(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class TrackCreate(BaseModel):
    """
    THis class models the request body for creating a new Track in the database.
    """

    name: str = Field(..., title="Name", description=f"Must be a unique name")
    description: str = Field(None, title="Description")


class TrackUpdate(BaseModel):
    """
    This class models the request body for updating a existing Track in the database.
    """

    name: str = Field(..., title="Name", description=f"Name of the round to be updated")
    description: Optional[str] = Field(..., title="Description")