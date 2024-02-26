import json
import pytest
from app import create_app
from app.utils.database import db
from app.models.animals import Animals

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def test_client(app):
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_get_animals(client):
    response = client.get("/animals")
    assert response.status_code == 200

def test_get_animal_by_id(client):
    response = client.get("/animals/1")
    assert response.status_code == 200

def test_create_animals(client):
    data = {
        "name": "Test Animal",
        "age": 3,
        "type": "Mammal",
        "gender": "Female"
    }
    response = client.post("/animals", json=data)
    assert response.status_code == 200

def test_update_animal_by_id(client):
    data = {
        "name": "Updated Animal",
        "age": 4,
        "type": "Bird",
        "gender": "Male"
    }
    response = client.put("/animals/1", json=data)
    assert response.status_code == 200

def test_delete_animal_by_id(client):
    response = client.delete("/animals/1")
    assert response.status_code == 200
