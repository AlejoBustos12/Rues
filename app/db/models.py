from sqlalchemy import Column, Integer, String, DateTime, Enum, JSON, UniqueConstraint, text
from sqlalchemy.sql import func
from app.db.database import Base
import enum


class StatusEnum(str, enum.Enum):
    PENDIENTE = "PENDIENTE"
    PROCESADO = "PROCESADO"
    ERROR = "ERROR"


class Company(Base):
    __tablename__ = "proceso_rues_test"
    __table_args__ = (
        UniqueConstraint("nit", name="uq_process_rues_nit"),
    )
    id = Column(Integer, primary_key=True, index=True)
    nit = Column(String(10), nullable=False, index=True)
    raw_payload = Column(JSON, nullable=True)
    status = Column(Enum(StatusEnum), nullable=False, server_default=text("'PENDIENTE'"))
    last_error = Column(String(1024),nullable=True)

    created_at= Column(DateTime(timezone=True), server_default=func.now())
    update_at= Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    