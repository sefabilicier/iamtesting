from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_invalid_email():
    response = client.post(
        "/users/register",
        json={"email": "invalid-email", "name": "Test"}
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid email format"


def test_valid_email():
    response = client.post(
        "/users/register",
        json={"email": "test@example.com", "name": "Test"}
    )

    assert response.status_code == 200