from uuid import uuid4
from flask import Blueprint, request, jsonify
from app.services.person_services import Person_service
from app.utils.database import db
from app.models.person import Person
from app.utils.api_response import api_response
from app.routes.schema.update_person import update_person_request
bp = Blueprint("persons", __name__)

@bp.route("/", methods=['GET'])
def get_persons():
    person_service = Person_service()
    persons = person_service.get_all_persons()
    return api_response(
        status_code=200,
        message="Success!",
        data=persons
    )

@bp.route("/<string:number>", methods=['GET'])
def get_person_by_number(number):
    return Person_service().get_person_by_number(number=number)

@bp.route("/", methods=['GET', 'POST'])
def create_person():
    try:
        person = Person()
        data = request.json
        person.id = uuid4()
        person.name = data["name"]
        person.age = data["age"]
        person.email = data["email"]

        # person.name = "Manusia biasa"
        # person.age = 69
        # person.email = "biasabiasa@mail.com"
        print(person.serialize())
        db.session.add(person)
        db.session.commit()
        return 'success', 201
    except Exception as e:
        return e.__str__(), 500

@bp.route('/<int:number>', methods=['PUT'])
def update_person(number):
    try:
        data = request.json
        # update_person_request = update_person_request(**data)
        # print(update_person_request)
        person = Person()
        person.name = data["name"]
        person.age = data["age"]
        person.email = data["email"]
        person_service = Person_service()

        person2 = person_service.get_person_by_number(number)
        print(person2)
        response = person_service.update_person(person_id=person2["id"], person_data=person)

        return api_response(
            status_code=200,
            data=response,
            message="Successfully Updated Data"
        )
    except Exception as ex:
        return str(ex), 500

@bp.route('/<int:number>', methods=['DELETE'])
def deletePerson(number):
    try:
        deleted = Person_service().delete_person(number=number)

        if deleted > 0:
            return f'Successfully deleted {deleted} rows', 200
        else:
            return 'Nothing deleted'
    except Exception as ex:
        return str(ex), 500
