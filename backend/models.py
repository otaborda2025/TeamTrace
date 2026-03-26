from sqlalchemy import Column, Integer, String
import database

class Worker(database.Base):
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)