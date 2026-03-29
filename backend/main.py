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

@app.delete("/workers/{worker_id}")
def delete_worker(worker_id: int, db: Session = Depends(get_db)):
    # 1. Look for the worker in the database
    db_worker = db.query(models.Worker).filter(models.Worker.id == worker_id).first()
    
    # 2. If it's not there, tell the user
    if db_worker is None:
        return {"message": "Worker not found"}
        
    # 3. If it is there, delete it and save
    db.delete(db_worker)
    db.commit()
    return {"message": f"Worker {worker_id} deleted successfully"}


@app.put("/workers/{worker_id}")
def update_worker(worker_id: int, name: str, location: str, db: Session = Depends(get_db)):
    # 1. Look for the worker in the database
    db_worker = db.query(models.Worker).filter(models.Worker.id == worker_id).first()
    
    # 2. If it's not there, tell the user
    if db_worker is None:
        return {"message": "Worker not found"}
        
    # 3. If it is there, update the fields
    db_worker.name = name
    db_worker.location = location
    
    # 4. Save the changes to the database
    db.commit()
    db.refresh(db_worker)
    return {"message": f"Worker {worker_id} updated successfully"}