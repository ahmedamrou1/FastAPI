from pydantic import BaseModel

class Person(BaseModel):
    first_name: str
    last_name: str
    birthday: str
    gender: str
    email: str
    phone_number: str
    class Config:
        orm_mode = True

class CreatePerson(Person):
    pass

class UpdatePerson(Person):
    pass


class PersonResponse(BaseModel):
    first_name: str
    last_name: str
    birthday: str
    gender: str
    email: str
    phone_number: str
    class Config:
        orm_mode = True