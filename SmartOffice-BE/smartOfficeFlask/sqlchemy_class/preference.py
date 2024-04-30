from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from sqlchemy_class.database_config import Base, engine


class OfficeUserInfo(Base):
    __tablename__ = 'office_device_pin_out'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    pin0 = Column(String(50), nullable=False)
    pin1 = Column(String(50), nullable=False)
    pin2 = Column(String(50), nullable=False)
    pin3 = Column(String(50), nullable=False)
    pin4 = Column(String(50), nullable=False)
    pin5 = Column(String(50), nullable=False)
    pin6 = Column(String(50), nullable=False)
    pin7 = Column(String(50), nullable=False)
    pin8 = Column(String(50), nullable=False)
    pin9 = Column(String(50), nullable=False)
    pin10 = Column(String(50), nullable=False)
    pin11 = Column(String(50), nullable=False)
    pin12 = Column(String(50), nullable=False)
    pin13 = Column(String(50), nullable=False)
    pin14 = Column(String(50), nullable=False)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)

Base.metadata.create_all(engine)
