from sqlalchemy import Column, Date, Time, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.database.base_class import Base
from src.models.round import Round


class Telemetry(Base):

    id= Column(Integer, primary_key=True, index=True)
    speed=Column(Float, nullable=False)
    dist = Column(Float, nullable=False)
    engine_temp = Column(Float, nullable=False)
    telemetry_timestamp = Column(Time, nullable=False)
    energy_cons = Column(Float, nullable=True)
    rpm = Column(Integer, nullable = False)
    batery = Column(Integer, nullable=True)
    creation_timestamp= Column(DateTime, default=func.now(), nullable=False)
    round_id = Column(Integer, ForeignKey("round.id"))
    rounds = relationship(Round, primaryjoin=round_id == Round.id)
    

