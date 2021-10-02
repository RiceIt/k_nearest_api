from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

import database
import schemas
from models import SessionLocal


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/user/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = database.get_user(user_id=user_id, db=db)
    if not db_user:
        raise HTTPException(status_code=404, detail="Пользователь с таким ID не найден")
    return db_user


@app.get("/k_nearest/", response_model=list[schemas.User])
async def k_nearest(user_id: int, db: Session = Depends(get_db),
                    k: int = Query(..., ge=0), radius: float = Query(..., ge=0)):
    db_user = database.get_user(user_id=user_id, db=db)
    if not db_user:
        raise HTTPException(status_code=404, detail="Пользователь с таким ID не найден")
    return database.get_k_nearest(user=db_user, k=k, radius=radius, db=db)


@app.post("/user/", response_model=schemas.User)
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    db_user = database.get_user(user_id=user.id, db=db)
    if db_user:
        raise HTTPException(status_code=400, detail="Пользователь с таким ID уже существует")
    created_user = database.create_user(user=user, db=db)
    return created_user
