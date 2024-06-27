import pytest
import logging
from fastapi.testclient import TestClient
from main import app, users_db, portefolio_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_db():
    users_db.clear()
    portefolio_db.clear()

@pytest.fixture
def caplog_fixture(caplog):
    caplog.set_level(logging.INFO)
    return caplog

def test_create_user_logs(caplog_fixture):
    response = client.post("/user/", json={"iduser": 1, "email": "test@example.com", "password": "password"})
    assert response.status_code == 200
    assert "User created: iduser=1 email='test@example.com' password='password'" in caplog_fixture.text

def test_read_user_logs(caplog_fixture):
    client.post("/user/", json={"iduser": 1, "email": "test@example.com", "password": "password"})
    response = client.get("/user/1")
    assert response.status_code == 200
    assert "User retrieved: iduser=1 email='test@example.com' password='password'" in caplog_fixture.text

def test_update_user_logs(caplog_fixture):
    client.post("/user/", json={"iduser": 1, "email": "test@example.com", "password": "password"})
    response = client.put("/user/1", json={"iduser": 1, "email": "new@example.com", "password": "newpassword"})
    assert response.status_code == 200
    assert "User updated: iduser=1 email='new@example.com' password='newpassword'" in caplog_fixture.text

def test_delete_user_logs(caplog_fixture):
    client.post("/user/", json={"iduser": 1, "email": "test@example.com", "password": "password"})
    response = client.delete("/user/1")
    assert response.status_code == 200
    assert "User deleted: 1" in caplog_fixture.text

def test_create_portefolio_logs(caplog_fixture):
    client.post("/user/", json={"iduser": 1, "email": "test@example.com", "password": "password"})
    response = client.post("/portefolio/", json={"id_portefolio": 1, "id_user": 1, "date": "2024-06-26", "price": 100.0, "in_or_out": True})
    assert response.status_code == 200
    assert "Portefolio created: id_portefolio=1 id_user=1 date='2024-06-26' price=100.0 in_or_out=True" in caplog_fixture.text

def test_read_portefolio_logs(caplog_fixture):
    client.post("/user/", json={"iduser": 1, "email": "test@example.com", "password": "password"})
    client.post("/portefolio/", json={"id_portefolio": 1, "id_user": 1, "date": "2024-06-26", "price": 100.0, "in_or_out": True})
    response = client.get("/portefolio/1")
    assert response.status_code == 200
    assert "Portefolio retrieved: id_portefolio=1 id_user=1 date='2024-06-26' price=100.0 in_or_out=True" in caplog_fixture.text

def test_update_portefolio_logs(caplog_fixture):
    client.post("/user/", json={"iduser": 1, "email": "test@example.com", "password": "password"})
    client.post("/portefolio/", json={"id_portefolio": 1, "id_user": 1, "date": "2024-06-26", "price": 100.0, "in_or_out": True})
    response = client.put("/portefolio/1", json={"id_portefolio": 1, "id_user": 1, "date": "2024-06-26", "price": 200.0, "in_or_out": False})
    assert response.status_code == 200
    assert "Portefolio updated: id_portefolio=1 id_user=1 date='2024-06-26' price=200.0 in_or_out=False" in caplog_fixture.text

def test_delete_portefolio_logs(caplog_fixture):
    client.post("/user/", json={"iduser": 1, "email": "test@example.com", "password": "password"})
    client.post("/portefolio/", json={"id_portefolio": 1, "id_user": 1, "date": "2024-06-26", "price": 100.0, "in_or_out": True})
    response = client.delete("/portefolio/1")
    assert response.status_code == 200
    assert "Portefolio deleted: 1" in caplog_fixture.text
