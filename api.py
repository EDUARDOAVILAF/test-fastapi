from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Auto(BaseModel):
    brand: str
    doors: int
    polarized: bool


cars = [
    Auto(brand='Mazda', doors=5, polarized=True),
    Auto(brand='Kia', doors=4, polarized=False),
]


@app.get('/cars')
async def lists() -> list[Auto]:
    return cars


@app.post('/cars')
async def create(car: Auto) -> Auto:
    # Sugar syntax
    exists = list(filter(lambda c: c.brand == car.brand, cars))
    if not exists:
        cars.append(car)
    return car


@app.put('/cars')
async def update(car: Auto) -> Auto:
    for c in cars:
        if c.brand == car.brand:
            c.doors = car.doors
            c.polarized = car.polarized
            return c


@app.delete('/cars')
async def delete(car: Auto) -> dict:
    for key, c in enumerate(cars):
        if c.brand == car.brand:
            cars.pop(key)
            return {'message': 'Delete successfully!'}
