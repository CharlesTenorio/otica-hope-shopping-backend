from core.configs import ConfigSetting
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
import sqlalchemy.orm as orm
from datetime import datetime
from models.grupo_prd_model import GrupoPrd


class SubGrupoPrd(ConfigSetting.DBBaseModel):
    __tablename__ = "sub_grupos_prd"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_grupo = Column(Integer, ForeignKey('grupos_prd.id'))  # Correção aqui
    tipo_grupo = orm.relationship('GrupoPrd', lazy='joined')
    name = Column(String(50), nullable=False, index=True, unique=True)
    active = Column(Boolean, nullable=False, default=True)
    dateCreated = Column(DateTime, nullable=False, default=datetime.now)
