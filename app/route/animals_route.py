from flask import Blueprint, jsonify, request
from ..utils.database import db
from app.models.animals import Animals


def app():
   from app import app

animals_blueprint = Blueprint('animals_endpoint', __name__)


# get list all animals
@animals_blueprint.route("/", methods=["GET"])
def get_animals():
  try:
    animal = Animals.query.all()

    return  [animals.as_dict() for animals in animal], 200
  except Exception as e:
    return e, 500
  
# route to get an animal by ID
@animals_blueprint.route("/<int:animals_id>", methods=["GET"])
def get_animal_by_id(animals_id):
    try:
        animals = Animals.query.get(animals_id)

        if animals:
            return animals.as_dict(), 200
        else:
            return {"message": "Animals not found"}, 404

    except Exception as e:
        return e, 500  

# create animals
@animals_blueprint.route("/", methods=["POST"])
def create_animals():
  try:
    data = request.json

    animals = Animals()
    animals.name = data["name"]
    animals.age = data["age"]
    animals.type = data["type"]
    animals.gender = data["gender"]
    db.session.add(animals)
    db.session.commit()
    return  'berhasil', 200
  except Exception as e:
    return e, 500
  
# update animals by id
@animals_blueprint.route("/<int:animals_id>", methods=["PUT"])
def update_animal_by_id(animals_id):
    try:
        if request.content_type != 'application/json':
            return jsonify(message="Content-Type must be 'application/json'"), 415

        animals = Animals.query.get(animals_id)

        if not animals:
            return jsonify(message="Animals not found"), 404

        data = request.get_json()

        if not data:
            return jsonify(message="No input data provided"), 400

        animals.id = data.get("id")
        animals.name = data.get("name")
        animals.age = data.get("age")
        animals.type = data.get("type")
        animals.gender = data.get("gender")

        db.session.commit()
        return jsonify(message="Animals updated successfully"), 200
    except Exception as e:
        return jsonify(message=str(e)), 500

# delete employee
@animals_blueprint.route("/<int:animals_id>", methods=["DELETE"])
def delete_animal_by_id(animals_id):
    try:
        animals = Animals.query.get(animals_id)

        if not animals:
            return {"message": "Animal not found"}, 404

        db.session.delete(animals)
        db.session.commit()
        return {"message": "Animal deleted successfully"}, 200
    except Exception as e:
        return str(e), 500
