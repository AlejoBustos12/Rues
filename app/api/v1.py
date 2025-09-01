from fastapi import APIRouter

router = APIRouter(prefix="/api/v1",tags=["api_bot"])

@router.post("/process-data")
def process_data(payload_in):
    try:
        #Insertar data en bd
        pass

    except:
        pass