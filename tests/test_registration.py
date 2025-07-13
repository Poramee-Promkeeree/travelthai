import pytest
from fastapi.testclient import TestClient
from travelthai.main import app

client = TestClient(app)

def test_registration():

    user_data = {"username": "testuser", "password": "testpass"}
    response = client.post("/auth/register", json=user_data)

    login_data = {"username": "testuser", "password": "testpass"}
    response = client.post("/auth/login", data=login_data)
    assert response.status_code == 200
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    reg_data = {
        "full_name": "Test User",
        "citizen_id": "1234567890123",
        "phone": "0812345678",
        "target_province": "Bangkok"
    }
    response = client.post("/travel/register", json=reg_data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["full_name"] == "Test User"
    assert data["citizen_id"] == "1234567890123"
    assert data["target_province"] == "Bangkok"
