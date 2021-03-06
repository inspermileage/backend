from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database.base_class import Base
from src.models.car import Car
from src.models.track import Track


class Round(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    reason = Column(String, nullable=False)
    ref_date = Column(Date, nullable=False)
    track_id = Column(Integer, ForeignKey("track.id"), nullable=False)
    tracks = relationship(Track, primaryjoin=track_id == Track.id)
    car_id = Column(Integer, ForeignKey("car.id"), nullable=False)
    cars = relationship(Car, primaryjoin=car_id == Car.id)
