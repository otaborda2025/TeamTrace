from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)