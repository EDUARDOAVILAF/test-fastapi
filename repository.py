from sqlalchemy.orm import Session
from model import Auto as AutoModel
from schemas import Auto


def select_autos(db: Session):
    return db.query(AutoModel).all()


def create_auto(db: Session, auto: Auto):
    db_auto = AutoModel(
        brand=auto.brand, doors=auto.doors, polarized=auto.polarized
    )
    db.add(db_auto)
    db.commit()
    db.refresh(db_auto)
    return db_auto


def update_auto(db: Session, auto: Auto, auto_id: int):
    db_auto = db.query(AutoModel).filter_by(id=auto_id).first()
    db_auto.doors = auto.doors
    db_auto.polarized = auto.polarized
    db.add(db_auto)
    db.commit()
    db.refresh(db_auto)
    return db_auto


def delete_auto(db: Session, auto_id: int):
    db_auto = db.query(AutoModel).filter_by(id=auto_id).delete()
    db.commit()
    return {"delete": "success"}