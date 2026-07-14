from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from .main import SessionLocal, Item

router = APIRouter()

@router.post('/items/', response_model=Item)
def create_item(item: Item):
    db: Session = SessionLocal()
    db.add(item)
    db.commit()
    db.refresh(item)
    db.close()
    return item

@router.get('/items/')
def read_items():
    db: Session = SessionLocal()
    items = db.query(Item).all()
    db.close()
    return items

@router.get('/items/{item_id}', response_model=Item)
def read_item(item_id: int):
    db: Session = SessionLocal()
    item = db.query(Item).filter(Item.id == item_id).first()
    db.close()
    if item is None:
        raise HTTPException(status_code=404, detail='Item not found')
    return item