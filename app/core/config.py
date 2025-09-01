#Las configuraciones y cargas de datos del .env ademas de las variables globales

from pydantic import BaseModel
from pydantic import field_validator
from typing import List
import os

class Settings(BaseModel):

    #Crear las propiedades de la clase
    database_url : str = os.getenv("DATABASE_URL","")
    api_key : str = os.getenv("DATABASE_URL","user-api-key")
    cors_origin : List[str] = [o.strip() for o in os.getenv("CORS_ORIGIN","*").split(";")]

    #cors   
    @field_validator("cors_origins")
    @classmethod
    def normalize_origins(cls, v:List[str]) -> List[str]:
        return [o for o in v if o]

settings = Settings()