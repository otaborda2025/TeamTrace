from pydantic import BaseModel
from app.jobsites.constants import GeofenceType


class JobsiteCreate(BaseModel):
    name: str
    address: str | None = None
    latitude: float
    longitude: float
    radius: int = 100


class JobsiteUpdate1(BaseModel):
    name: str | None = None
    address: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    radius: int | None = None
    is_active: bool | None = None

class JobsiteUpdate(BaseModel):
    name: str | None = None
    address: str="6200 Lyndon B Johnson Fwy"
    latitude: float=-87.45
    longitude: float=90.23 
    radius: int=150
    is_active: bool=True


class JobsiteResponse(BaseModel):

    id: int
    company_id: int
    name: str
    address: str | None
    latitude: float
    longitude: float
    radius: int
    geofence_type: GeofenceType
    is_active: bool

    class Config:
        from_attributes = True