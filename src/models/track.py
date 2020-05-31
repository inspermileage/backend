from sqlalchemy import Column, String, Integer

from src.database.base_class import Base


class Track(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
  