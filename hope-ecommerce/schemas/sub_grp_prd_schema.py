from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from models.grupo_prd_model import GrupoPrdSchema

class SubGrupoPrdSchema(BaseModel):
    id: Optional[int]
    id_grupo: int
    tipo_grupo: GrupoPrdSchema
    name: str = Field(..., max_length=50)
    active: bool = True
    dateCreated: datetime

    class Config:
        orm_mode = True
