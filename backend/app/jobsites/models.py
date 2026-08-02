from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy import Enum, JSON
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship
from app.database.session import Base
from app.database.base_class import TimestampMixin
from app.jobsites.constants import GeofenceType


class Jobsite(Base, TimestampMixin):
    __tablename__ = "jobsites"

    __table_args__ = (
        UniqueConstraint(
            "company_id",
            "name",
            name="uq_company_jobsite_name"
        ),
    )   


    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    name = Column(String, nullable=False)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    radius = Column(Integer, default=100)
    geofence_type = Column(Enum(GeofenceType), default=GeofenceType.CIRCLE)
    polygon = Column(JSON, nullable=True)
    is_active = Column(Boolean, default=True)
    company = relationship("Company")