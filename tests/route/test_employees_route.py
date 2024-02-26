import json
import pytest
from app import app, db
from app.models.employees import Employees

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_get_employees(client):
    response = client.get("/employees")
    assert response.status_code == 200

def test_get_employee_by_id(client):
    response = client.get("/employees/1")
    assert response.status_code == 200

def test_create_employees(client):
    data = {
        "name": "Test Employee",
        "gender": "Male",
        "phone": 123456789,
        "address": "Test Address"
    }
    response = client.post("/employees", json=data)
    assert response.status_code == 200

def test_update_employees(client):
    data = {
        "name": "Updated Employee",
        "gender": "Female",
        "phone": 987654321,
        "address": "Updated Address"
    }
    response = client.put("/employees/1", json=data)
    assert response.status_code == 200

def test_delete_employees(client):
    response = client.delete("/employees/1")
    assert response.status_code == 200
