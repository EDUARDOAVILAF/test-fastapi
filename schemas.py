from pydantic import BaseModel


class Auto(BaseModel):
    id: int
    brand: str
    doors: int
    polarized: bool
