from sqlalchemy import Column, Date, Integer, String

from src.database.base_class import Base


class Car(Base):
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True, nullable=True)

    description = Column(String, unique=True, nullable=True)

    creation_date = Column(Date, nullable=False)
