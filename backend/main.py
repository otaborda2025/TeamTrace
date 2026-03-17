from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models
from . import database

# Create the actual database file and tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency to get a database connection
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/workers")
def read_workers(db: Session = Depends(get_db)):
    return db.query(models.Worker).all()

@app.post("/workers")
def create_worker(name: str, location: str, db: Session = Depends(get_db)):
    new_worker = models.Worker(name=name, location=location)
    db.add(new_worker)
    db.commit()
    db.refresh(new_worker)
    return new_worker