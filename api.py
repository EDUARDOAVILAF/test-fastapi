from typing import List
from fastapi import Depends, FastAPI
from schemas import Auto
import model
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from repository import create_auto, select_autos


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

# Eduard Update

# Jonathan Delete
