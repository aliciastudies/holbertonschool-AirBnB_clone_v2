#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import os

class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        # place_amenities = represent a relationship Many-To-Many with Place
        place_amenities = relationship("Place", secondary="place_amenity",
                                       backref="amenities")
        # Primary link with place then second is place_amenity as specified
    else:
        name = ""
