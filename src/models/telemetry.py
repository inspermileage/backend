from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.database.base_class import Base
from src.models.round import Round


class Telemetry(Base):
    id= Column(Integer, primary_key=True, index=True)
    speed=Column(Float, nullable=False)
    distance = Column(Float, nullable=False)
    engine_temp = Column(Float, nullable=False)
    creation_time = Column(DateTime, default=func.now(), nullable=False)
    energy_cons = Column(Float, nullable=True)
    rpm = Column(Integer, nullable = False)
    battery = Column(Integer, nullable=True)
    round_id = Column(Integer, ForeignKey("round.id"))
    rounds = relationship(Round, primaryjoin=round_id == Round.id)

