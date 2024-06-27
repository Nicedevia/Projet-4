import pytest
from fastapi.testclient import TestClient
from maine.main import app, users_db, portefolio_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_db():
    users_db.clear()
    portefolio_db.clear()

def test_create_user():
    response = client.post("/user/", json={"iduser": 1, "email": "test@example.com", "password": "password"})
    assert response.status_code == 200
    assert response.json() == {"iduser": 1, "email": "test@example.com", "password": "password"}

def test_read_user():
    client.post("/user/", json={"iduser": 1, "email": "test@example.com", "password": "password"})
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json() == {"iduser": 1, "email": "test@example.com", "password": "password"}

def test_update_user():
    client.post("/user/", json={"iduser": 1, "email": "test@example.com", "password": "password"})
    response = client.put("/user/1", json={"iduser": 1, "email": "new@example.com", "password": "newpassword"})
    assert response.status_code == 200
    assert response.json() == {"iduser": 1, "email": "new@example.com", "password": "newpassword"}

def test_delete_user():
    client.post("/user/", json={"iduser": 1, "email": "test@example.com", "password": "password"})
    response = client.delete("/user/1")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted"}

def test_create_portefolio():
    client.post("/user/", json={"iduser": 1, "email": "test@example.com", "password": "password"})
    response = client.post("/portefolio/", json={"id_portefolio": 1, "id_user": 1, "date": "2024-06-26", "price": 100.0, "in_or_out": True})
    assert response.status_code == 200
    assert response.json() == {"id_portefolio": 1, "id_user": 1, "date": "2024-06-26", "price": 100.0, "in_or_out": True}

def test_read_portefolio():
    client.post("/user/", json={"iduser": 1, "email": "test@example.com", "password": "password"})
    client.post("/portefolio/", json={"id_portefolio": 1, "id_user": 1, "date": "2024-06-26", "price": 100.0, "in_or_out": True})
    response = client.get("/portefolio/1")
    assert response.status_code == 200
    assert response.json() == {"id_portefolio": 1, "id_user": 1, "date": "2024-06-26", "price": 100.0, "in_or_out": True}

def test_update_portefolio():
    client.post("/user/", json={"iduser": 1, "email": "test@example.com", "password": "password"})
    client.post("/portefolio/", json={"id_portefolio": 1, "id_user": 1, "date": "2024-06-26", "price": 100.0, "in_or_out": True})
    response = client.put("/portefolio/1", json={"id_portefolio": 1, "id_user": 1, "date": "2024-06-26", "price": 200.0, "in_or_out": False})
    assert response.status_code == 200
    assert response.json() == {"id_portefolio": 1, "id_user": 1, "date": "2024-06-26", "price": 200.0, "in_or_out": False}

def test_delete_portefolio():
    client.post("/user/", json={"iduser": 1, "email": "test@example.com", "password": "password"})
    client.post("/portefolio/", json={"id_portefolio": 1, "id_user": 1, "date": "2024-06-26", "price": 100.0, "in_or_out": True})
    response = client.delete("/portefolio/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Portefolio deleted"}
