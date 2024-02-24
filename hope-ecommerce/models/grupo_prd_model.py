from core.configs import ConfigSetting
from sqlalchemy import Column, Integer, String, DateTime, Boolean
import sqlalchemy as sa
from datetime import datetime
from models.otica_model import Otica
import sqlalchemy.orm as orm


class GrupoPrd(ConfigSetting.DBBaseModel):
    __tablename__ = "grupos_prd"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_otica = Column(Integer, sa.ForeignKey('otica.id'))
    tipo_otica = orm.relationship('Otica', lazy='joined')  # Correção aqui
    name = Column(String(50), nullable=False, index=True, unique=True)
    active = Column(Boolean, nullable=False, default=True)
    dateCreated = Column(DateTime, nullable=False, default=datetime.now)
