from database import Base
from sqlalchemy import TIMESTAMP, Column, Date, ForeignKey, Integer, String, column, text


class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True, nullable=False) 
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birthday = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

