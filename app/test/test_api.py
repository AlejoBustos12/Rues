import os
os.environ["API_KEY"] = "test-key"

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

headers = {
    "X-API-Key":"test-key"
}

def test_process_and_update():

    response_first_test = client.post("/api/v1/process-data",json={"nit":"900777755", "payload":{"razonsocial":"DIAC"}}, headers=headers)
    assert response_first_test.status_code in (200,201)
    
    body = response_first_test.json()
    assert body["nit"] =="900777755"
    assert body["status"] =="PENDIENTE"

    response_second_test = client.post("/api/v1/update-status", json={"nit": "900777755", "status": "PROCESADO"}, headers=headers)
    assert response_second_test.status_code == (200)
    assert response_second_test.json()['status'] == "PROCESADO"
