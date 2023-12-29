import models, schemas, utils, oauth2
from sqlalchemy.orm import Session
from database import engine, get_db
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from typing import List


router = APIRouter(prefix="/people", tags=['People'])




@router.get("/", response_model=List[schemas.Person])
def test_posts(db: Session = Depends(get_db)):
    people = db.query(models.Person).all()
    return people

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Person)
def add_person(person: schemas.CreatePerson, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
   print(user_id)
   new_person = models.Person(**person.model_dump())
   db.add(new_person)
   db.commit()
   db.refresh(new_person)
   return new_person

@router.get("/{id}", response_model=schemas.PersonResponse)
def view_person(id: str,db: Session = Depends(get_db)): 
    result = db.query(models.Person).filter(models.Person.id == id).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid post id")
    return result
    

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_person(id: str, db: Session = Depends(get_db), user: int = Depends(oauth2.get_current_user)):
    print(user)
    result = db.query(models.Person).filter(models.Person.id == id)
    if not result.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid post id")
    result.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", status_code= status.HTTP_205_RESET_CONTENT, response_model=schemas.PersonResponse)
def update_person(id: str, new_content: schemas.UpdatePerson,db: Session = Depends(get_db), user: int = Depends(oauth2.get_current_user)):
    print(user)
    query = db.query(models.Person).filter(models.Person.id == id)
    person = query.first()
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid post id")
    query.update(new_content.model_dump(), synchronize_session=False)
    db.commit()
    person = query.first()
    return person