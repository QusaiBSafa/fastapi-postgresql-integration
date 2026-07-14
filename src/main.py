from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/fastapi_db')

engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

Base.metadata.create_all(bind=engine)

@app.post('/items/', response_model=Item)
def create_item(item: Item):
    db: Session = SessionLocal()
    db.add(item)
    db.commit()
    db.refresh(item)
    db.close()
    return item

@app.get('/items/')
def read_items():
    db: Session = SessionLocal()
    items = db.query(Item).all()
    db.close()
    return items