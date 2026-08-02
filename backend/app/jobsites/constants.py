from enum import Enum


class GeofenceType(str, Enum):
    CIRCLE = "CIRCLE"
    POLYGON = "POLYGON"
