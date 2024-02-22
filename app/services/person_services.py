from app.models.person import Person
from app.repositories.person_repository import Person_repo
class Person_service:
    def __init__(self) -> None:
        self.person_repo = Person_repo()
    
    def get_all_persons(self):
        return [person.serialize() for person in self.person_repo.get_all_persons()]
    
    def get_person_by_number(self, number):
        person = self.person_repo.get_person_by_number(number=number)
        return person.serialize()
    
    def update_person(self, person_id, person_data):
        updated_person = self.person_repo.update_person(person_id, person_data)
        return updated_person.serialize()
    
    def delete_person(self, number):
        response = self.person_repo.delete_person(number)
        return response