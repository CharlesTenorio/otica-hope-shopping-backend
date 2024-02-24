from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class OticaSchema(BaseModel):
    id: Optional[int]
    id_user: str
    cnpj: str
    name: str = Field(..., max_length=50)
    logo: str = Field(..., max_length=150)
    active: bool = True
    dateCreated: datetime

    class Config:
        orm_mode = True
