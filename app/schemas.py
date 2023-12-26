from pydantic import BaseModel, EmailStr
from typing import Optional

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

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    email: EmailStr
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None