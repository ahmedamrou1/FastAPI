import models, schemas, utils
from sqlalchemy.orm import Session
from database import engine, get_db
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from typing import List

router = APIRouter(prefix="/users", tags=['Users'])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)  
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user.password = utils.hash(user.password)
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: str,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid post id")
    return user
