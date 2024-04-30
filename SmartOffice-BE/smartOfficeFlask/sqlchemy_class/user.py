from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from sqlchemy_class.database_config import Base, engine


# 用户基本信息
class OfficeUser(Base):
    __tablename__ = 'office_user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, name, password, update_time=None):
        self.name = name
        self.password = password
        if update_time is None:
            update_time = datetime.now()
        self.update_time = update_time

    def to_json(self):
        obj_dict = self.__dict__.copy()
        obj_dict.pop('_sa_instance_state', None)
        return obj_dict




class OfficeUserInfo(Base):
    __tablename__ = 'office_user_info'

    user_id = Column(Integer, primary_key=True)
    zone1_light = Column(String(50), nullable=False)
    zone1_fancoil = Column(String(50), nullable=False)
    zone2_light = Column(String(50), nullable=False)
    zone2_fancoil = Column(String(50), nullable=False)
    office_pau = Column(String(50), nullable=False)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class OfficeUserLog(Base):
    __tablename__ = 'office_user_log'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, primary_key=True)
    start_time_1 = Column(DateTime, nullable=False)
    start_time_2 = Column(DateTime, nullable=False)
    end_time_1 = Column(DateTime, nullable=False)
    end_time_2 = Column(DateTime, nullable=False)

    def to_json(self):
        obj_dict = self.__dict__.copy()
        obj_dict.pop('_sa_instance_state', None)
        return obj_dict



Base.metadata.create_all(engine)
