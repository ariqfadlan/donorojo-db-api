"""
Contains controllers for interacting with database
and other methods.
"""
from io import BytesIO
from decimal import Decimal
from sqlalchemy.orm import Session
import segno

from .models import Address, Location, TouristAttraction

def get_tourist_attractions(skip: int, limit: int, db: Session):
    return db.query(TouristAttraction).offset(skip).limit(limit).all()

def get_tourist_attraction(db: Session, row_id: int):
    return db.query(TouristAttraction).filter(TouristAttraction.id == row_id).first()

def get_address_by_id(db: Session, row_id: int):
    return db.query(Address).filter(Address.tourist_attraction_id == row_id).first()

def get_location_by_id(db: Session, row_id: int):
    return db.query(Location).filter(Location.tourist_attraction_id == row_id).first()

def generate_qrcode(lat: Decimal, long: Decimal, prefix: str = "geo:") -> BytesIO:
    coordinate = f"{lat},{long}"
    data = f"{prefix}{coordinate}"
    buffer = BytesIO()
    qr_image = segno.make(data, micro=False)
    qr_image.save(buffer, kind="png", scale=4)
    buffer.seek(0)
    return buffer
