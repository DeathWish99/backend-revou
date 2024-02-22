from flask import Flask
from app.routes import animal, employee, persons, users
import os
from app.utils.database import db
app = Flask(__name__)

DATABASE_TYPE = os.getenv('DATABASE_TYPE')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_PORT = os.getenv('DATABASE_PORT')
app.config['SQLALCHEMY_DATABASE_URI'] = f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

db.init_app(app)

app.register_blueprint(persons.bp, url_prefix='/v1/persons')
app.register_blueprint(users.example, url_prefix='/v1/example')
# app.register_blueprint(animal.animalBp, url_prefix='/animal')
# app.register_blueprint(employee.employeeBp, url_prefix='/employee')