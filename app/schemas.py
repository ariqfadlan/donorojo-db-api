"""
Contains data schema
Used for validation
"""
from pydantic import BaseModel

class AddressBase(BaseModel):
    subvillage: str
    village: str
    district: str
    regency: str
    province: str

class Address(AddressBase):
    tourist_attraction_id: int

    class Config:
        orm_mode = True

class LocationBase(BaseModel):
    latitude: float
    longitude: float

class Location(LocationBase):
    tourist_attraction_id: int

    class Config:
        orm_mode = True

class TouristAttraction(BaseModel):
    id: int
    name: str
    category: str
    address: Address
    location: Location

    class Config:
        orm_mode = True

class TouristAttractionDocs(BaseModel):
    id: int
    name: str
    category: str
    address: AddressBase
    location: LocationBase

class GeneralException(BaseModel):
    detail: str

class LocationQR(BaseModel):
    data: str
