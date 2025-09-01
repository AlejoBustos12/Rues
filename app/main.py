from fastapi import FastAPI
from app.api.v1 import router as api_router

app = FastAPI(title="Api para consulta del RUES",version="1.0.0")



#Routers
app.include_router(api_router)


@app.get("/")
async def health():
    return {"status":"ok. api is runnig"}