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
    creation_date: date
    class Config:
        orm_mode = True

class CarCreate(BaseModel):
    """
    This class models the request body for creating a new Car in the database.
    """
    
    name:str =""
    description: Optional[str]= ""
    creation_date: Optional[date] = datetime.now().date()

class CarUpdate(BaseModel):
    """
    This class models the request body for updating a existing Car in the database.
    """
    
    name: Optional[str]
    description: Optional[str]
    creation_date: Optional[date]

 