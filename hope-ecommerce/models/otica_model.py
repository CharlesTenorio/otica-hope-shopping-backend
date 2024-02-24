from core.configs import ConfigSetting
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime

class Otica(ConfigSetting.DBBaseModel):
    __tablename__ = "otica"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_user = Column(String(50), nullable=False, unique=True)
    cnpj = Column(String(50), nullable=False, unique=True)
    name = Column(String(50), nullable=False, index=True),
    logo = Column(String(150), nullable=False),
    active = Column(Boolean, nullable=False, default=True)
    dateCreated = Column(DateTime, nullable=False, default=datetime.now)
    