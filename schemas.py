from typing import Optional
from pydantic import BaseModel


class Auto(BaseModel):
    id: Optional[int] = None
    brand: str
    doors: int
    polarized: bool
