from app.models.person import Person
from app.utils.database import db


class Person_repo():
    def get_all_persons(self):
        return Person.query.filter(Person.is_deleted != True).all()

    def get_person_by_number(self, number):
        return Person.query.filter(Person.number == number).first()

    def update_person(self, id, person):
        person_obj = Person.query.get(id)
        person_obj.name = person.name
        person_obj.age = person.age
        person_obj.email = person.email

        db.session.add(person_obj)
        db.session.commit()
        return person_obj
    
    def delete_person(self, number):
        person_obj = Person.query.filter(Person.number == number).delete()

        db.session.commit()
        return person_obj