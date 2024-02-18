from flask import Flask
from app.route import animals_route
from app.route import employees_route
import os
from app.utils.database import db, migrate
from app.models import animals

app = Flask(__name__)

DATABASE_TYPE = os.getenv('DATABASE_TYPE')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
app.config["SQLALCHEMY_DATABASE_URI"] = f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(animals_route.animals_blueprint, url_prefix="/animals")
app.register_blueprint(employees_route.employees_blueprint, url_prefix="/employees")