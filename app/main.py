from fastapi import FastAPI
from app.api.v1 import router as api_router

from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.database import Base, engine

app = FastAPI(title="Api para consulta del RUES",version="1.0.0")

Base.metadata.create_all(bind=engine)

#CORS 
if settings.cors_origin ==["*"]:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],

    )
else:
       app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origin,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],

    )

#Routers
app.include_router(api_router)

@app.get("/")
async def health():
    return {"status":"ok. api is runnig"}