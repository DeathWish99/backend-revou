from app.utils.database import db
import uuid

class Person(db.Model):
    __tablename__ = "person"
    id=db.Column(db.UUID, primary_key = True, default=uuid.uuid4)
    name=db.Column(db.String(100), nullable= True)
    age=db.Column(db.Integer, nullable=True)
    email=db.Column(db.String(100), nullable= True)
    number=db.Column(db.Integer, db.Identity())
    is_deleted=db.Column(db.Boolean, default=False)
    
    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "age": self.age,
                "email" : self.email,
                "number" : self.number,
                "is_deleted": self.is_deleted}
    
    def listToDict(self, persons):
        personList2 = []

        for person in persons:
            personList2.append({'id':person.id,'name':person.name,'email':person.email, 'age':person.age})
        
        return personList2