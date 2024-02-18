from flask import Blueprint, jsonify, request
from ..utils.database import db
from app.models.employees import Employees


def app():
   from app import app

employees_blueprint = Blueprint('employees_endpoint', __name__)

# get list of employee
@employees_blueprint.route("/", methods=["GET"])
def get_employees():
  try:
    employee = Employees.query.all()

    return  [employees.as_dict() for employees in employee], 200
  except Exception as e:
    return e, 500

# route to get an employee by ID
@employees_blueprint.route("/<int:employees_id>", methods=["GET"])
def get_animal_by_id(employees_id):
    try:
        employees = Employees.query.get(employees_id)

        if employees:
            return employees.as_dict(), 200
        else:
            return {"message": "employees not found"}, 404

    except Exception as e:
        return e, 500  

# create employee
@employees_blueprint.route("/", methods=["POST"])
def create_employees():
  try:
    data = request.json

    employees = Employees()
    employees.name = data["name"]
    employees.gender = data["gender"]
    employees.phone = data["phone"]
    employees.address = data["address"]
    db.session.add(employees)
    db.session.commit()
    return  'berhasil', 200
  except Exception as e:
    return e, 500

# update employees by id
@employees_blueprint.route("/<int:employees_id>", methods=["PUT"])
def update_animals(employees_id):
    try:
        if request.content_type != 'application/json':
            return jsonify(message="Content-Type must be 'application/json'"), 415

        employees = Employees.query.get(employees_id)

        if not employees:
            return jsonify(message="employees not found"), 404

        data = request.get_json()

        if not data:
            return jsonify(message="No input data provided"), 400

        employees.id = data.get("id")
        employees.name = data.get("name")
        employees.gender = data.get("gender")
        employees.phone = data.get("phone")
        employees.address = data.get("address")

        db.session.commit()
        return jsonify(message="employees updated successfully"), 200
    except Exception as e:
        return jsonify(message=str(e)), 500

# delete employee
@employees_blueprint.route("/<int:employees_id>", methods=["DELETE"])
def delete_animals_by_id(employees_id):
  try:
      employees = Employees.query.get(employees_id)

      if not employees:
          return {"message": "employees not found"}, 404

      db.session.delete(employees)
      db.session.commit()
      return {"message": "employees deleted successfully"}, 200
  except Exception as e:
        return str(e), 500

