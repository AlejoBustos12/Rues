from fastapi import APIRouter,status, Header, HTTPException, Depends
from typing import Optional

from app.core.config import settings 
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.schemas.company import ProcessDataIn,UpdateStatusIn,CompanyOut,StatusEnum
from app.services import crud
from app.db import models as db_models


router = APIRouter(prefix="/api/v1",tags=["api_bot"])

#Validacion de la api KEY
async def validate_api_key(x_api_key: Optional[str]  = Header(None)):
    if settings.api_key and x_api_key != settings.api_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Api key incorrecta")

@router.post("/process-data", response_model = CompanyOut, status_code=status.HTTP_201_CREATED, dependencies=[Depends(validate_api_key)])
def process_data(payload_in: ProcessDataIn, db: Session = Depends(get_db)):
    
    try:

        company = crud.upsert_process_data(db,nit=payload_in.nit, payload= payload_in.payload)
        return CompanyOut(nit=company.nit, status=company.status.value,payload=company.raw_payload, last_error = company.last_error)

    except Exception as e:
        
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    