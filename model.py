from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class Auto(Base):
    __tablename__ = 'autos'
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(45), nullable=False)
    doors = Column(Integer, nullable=False)
    polarized = Column(Boolean)
