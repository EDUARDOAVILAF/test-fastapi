from typing import List
from fastapi import Depends, FastAPI
from schemas import Auto
import model
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from repository import create_auto, select_autos, update_auto, delete_auto


model.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/cars')
async def get(db: Session = Depends(get_db)) -> List[Auto]:
    return select_autos(db)


@app.post("/cars", response_model=Auto)
async def create(auto: Auto, db: Session = Depends(get_db)) -> Auto:
    return create_auto(db, auto)

@app.delete('/cars/{card_id}')
async def delete(card_id: int, db: Session = Depends(get_db)) -> dict:
   return delete_auto(db, card_id)

@app.put("/cars/{car_id}")
async def update(
    car_id: int, auto: Auto, db: Session = Depends(get_db)
) -> Auto:
    return update_auto(db, auto, car_id)
