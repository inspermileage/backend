from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.database.base_class import Base
from src.models.round import Round


class Car(Base):

 
    id= Column(Integer, primary_key=True, index=True)
    name= Column(String, nullable=True)
    description= Column(String, nullable=True)
    inst_vel=Column(float, nullable=False)
    ref_date: Column(Date, nullable=False)
    dist = Column(float, nullable=False)
    engine_temp = Column(float, nullable=False)
    time = Column(Date, nullable=False)
    energy_cons = Column(float, nullable=True)
    rpm = Column(Integer, nullable = False)
    batery = Column(Integer, nullable=True)
    round_id = Column(Integer, ForeignKey("round.id"))
    rounds = relationship(Round, primaryjoin=round_id == Round.id)
