from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Optional, Dict,Any


from app.db import models 

def upsert_process_data(db:Session, *, nit: str, payload: Optional[Dict[str,Any]] = None) -> models.Company:
    
    payload = payload or {}
    company = db.query(models.Company).filter(models.Company.nit == nit).first()

    if company:
        company.raw_payload = payload
    else:
        company = models.Company(nit=nit,raw_payload = payload, status= models.StatusEnum.PENDIENTE)
        db.add(company)

    try:
        db.commit()
    except IntegrityError: 
        db.rollback()
        raise

    db.refresh(company)

    return company


def update_status(db:Session, *, nit:str, status: models.StatusEnum, error: Optional[str] = None) -> models.Company:
    company = db.query(models.Company).filter(models.Company.nit == nit).first()
    
    if not company :
        raise ValueError("No se encontro el NIT")
    
    company.status =status
    company.last_error = error
    
    db.commit()
    db.refresh(company)

    return company

def get_company(db:Session, *, nit:str) -> Optional[models.Company]:
    return db.query(models.Company).filter(models.Company.nit == nit).first()