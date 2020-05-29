from pydantic import BaseModel, Field
from datetime import date, datetime, time
from enum import Enum
from typing import Optional



class Car2InDB(BaseModel):
    """
    This represents the object stored in the database, it is similar to the `/models/car`.
    """

    id: int
    name: str
    description: str
    creation_date: date
    class Config:
        orm_mode = True

class Car2Create(BaseModel):
    """
    This class models the request body for creating a new Car in the database.
    """
    
    name: Optional[str]=""
    description: Optional[str]= ""
    creation_date: Optional[date] = datetime.now().date()

class Car2Update(BaseModel):
    """
    This class models the request body for updating a existing Car in the database.
    """
    
    name: Optional[str]
    description: Optional[str]
    creation_date: Optional[date]

 