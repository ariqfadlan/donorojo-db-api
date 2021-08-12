"""
Contains database models
"""
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base

class TouristAttraction(Base):
    __tablename__ = "tourist_attraction"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    category = Column(String(255), nullable=False)

    address = relationship("Address", back_populates="tourist_attraction", uselist=False)
    location = relationship("Location", back_populates="tourist_attraction", uselist=False)

class Address(Base):
    __tablename__ = "address"

    tourist_attraction_id = Column(Integer, ForeignKey("tourist_attraction.id"), primary_key=True)
    subvillage = Column(String(255))
    village = Column(String(255))
    district = Column(String(255))
    regency = Column(String(255))
    province = Column(String(255))

    tourist_attraction = relationship("TouristAttraction", back_populates="address")


class Location(Base):
    __tablename__ = "location"

    tourist_attraction_id = Column(Integer, ForeignKey("tourist_attraction.id"), primary_key=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    tourist_attraction = relationship("TouristAttraction", back_populates="location")
