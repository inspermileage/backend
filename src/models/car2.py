from sqlalchemy import Column, Date, ForeignKey, Integer, String
from src.database.base_class import Base 


class Car2(Base):
 
    id= Column(Integer, primary_key=True, index=True)
    name= Column(String, nullable=True)
    description= Column(String, nullable=True)
    creation_date= Column(Date, nullable=False)
  