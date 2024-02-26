import pytest
from app import create_app
from app.utils.database import db

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()
