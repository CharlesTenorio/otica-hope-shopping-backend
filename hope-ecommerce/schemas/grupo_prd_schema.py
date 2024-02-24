from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from otica_schema import OticaSchema


class GrupoPrdSchema(BaseModel):
    id: Optional[int]
    id_otica: int
    tipo_otica: OticaSchema
    name: str = Field(..., max_length=50)
    active: bool = True
    dateCreated: datetime

    class Config:
        orm_mode = True