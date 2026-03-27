from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
import database

# Create the database file immediately
models.database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# This allows your React app to talk to your Python app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/workers")
def get_workers(db: Session = Depends(get_db)):
    return db.query(models.Worker).all()

@app.post("/workers")
def create_worker(name: str, location: str, db: Session = Depends(get_db)):
    new_worker = models.Worker(name=name, location=location)
    db.add(new_worker)
    db.commit()
    db.refresh(new_worker)
    return new_worker