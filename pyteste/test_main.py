import sys
import os
import pytest
import logging
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from main import app
from database.connextion import Base, get_db
from project.models.models import User, Portfolio

# Utilisez une base de données en mémoire pour les tests
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

client = TestClient(app)

@pytest.fixture(scope="module")
def db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(autouse=True)
def clear_db():
    with TestingSessionLocal() as db:
        db.query(User).delete()
        db.query(Portfolio).delete()
        db.commit()

@pytest.fixture
def caplog_fixture(caplog):
    caplog.set_level(logging.INFO)
    return caplog

def test_create_user_logs(caplog_fixture):
    response = client.post("/auth/users/", json={"email": "test@example.com", "password": "password"})
    assert response.status_code == 200
    assert "User created: email='test@example.com'" in caplog_fixture.text

def test_read_user_logs(caplog_fixture):
    client.post("/auth/users/", json={"email": "test@example.com", "password": "password"})
    response = client.get("/auth/users/")
    assert response.status_code == 200
    assert "Users retrieved" in caplog_fixture.text

def test_create_user():
    response = client.post("/auth/users/", json={"email": "test@example.com", "password": "password123"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_read_users():
    client.post("/auth/users/", json={"email": "test@example.com", "password": "password"})
    response = client.get("/auth/users/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

def test_create_portfolio_logs(caplog_fixture):
    client.post("/auth/users/", json={"email": "test@example.com", "password": "password"})
    response = client.post("/auth/portfolios/", json={"user_id": 1, "category": "Investment", "date": "2024-06-26", "price": 100.0})
    assert response.status_code == 200
    assert "Portfolio created: user_id=1 category='Investment' date='2024-06-26' price=100.0" in caplog_fixture.text

def test_read_portfolios_logs(caplog_fixture):
    client.post("/auth/users/", json={"email": "test@example.com", "password": "password"})
    client.post("/auth/portfolios/", json={"user_id": 1, "category": "Investment", "date": "2024-06-26", "price": 100.0})
    response = client.get("/auth/portfolios/")
    assert response.status_code == 200
    assert "Portfolios retrieved" in caplog_fixture.text

def test_create_portfolio():
    client.post("/auth/users/", json={"email": "test@example.com", "password": "password"})
    response = client.post("/auth/portfolios/", json={"user_id": 1, "category": "Investment", "date": "2024-06-26", "price": 100.0})
    assert response.status_code == 200
    data = response.json()
    assert data["category"] == "Investment"
    assert "id" in data

def test_read_portfolios():
    client.post("/auth/users/", json={"email": "test@example.com", "password": "password"})
    client.post("/auth/portfolios/", json={"user_id": 1, "category": "Investment", "date": "2024-06-26", "price": 100.0})
    response = client.get("/auth/portfolios/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
