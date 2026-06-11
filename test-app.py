from app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_all():
    response = client.get("/get/all")

    assert response.status_code == 200