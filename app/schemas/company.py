from pydantic import BaseModel
from pydantic import Field, constr
from typing import Optional,Dict,Any
from enum import Enum


class StatusEnum(str, Enum):
    PENDIENTE = "PENDIENTE"
    PROCESADO = "PROCESADO"
    ERROR = "ERROR"

class ProcessDataIn(BaseModel):
    nit: constr(strip_whitespace=True, min_length=9, max_length=10) = Field(..., examples=["890980777"])
    payload : Optional[Dict[str,Any]] = Field(default_factory=dict, examples=[{"razonSocial": "Nit Caldas"}])

class UpdateStatusIn(BaseModel):
    nit : constr(strip_whitespace=True, min_length=9, max_length=10)
    status : StatusEnum
    error: Optional[str] = Field(None, description="Mensaje de error si status=ERROR")

class CompanyOut(BaseModel):
    nit : str
    status : StatusEnum
    payload : Optional[dict]
    last_error : Optional[str]

    class Config:
        from_attributes = True