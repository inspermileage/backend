from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database.base_class import Base
from src.models.track import Track
from src.models.car2 import Car2

class Round(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    reason = Column(String, nullable=False)
    ref_date = Column(Date, nullable=False)
    track_id = Column(Integer, ForeignKey("track.id"))
    tracks = relationship(Track, primaryjoin=track_id == Track.id)
    car2_id = Column(Integer, ForeignKey("car2.id"))
    car2s = relationship(Car2, primaryjoin=car2_id == Car2.id)
