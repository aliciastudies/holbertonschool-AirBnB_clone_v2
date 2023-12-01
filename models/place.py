#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, null
from sqlalchemy import Table, MetaData
from sqlalchemy.orm import relationship, backref
import os


metadata = MetaData()


class Place(BaseModel, Base):
    """ Place class """
    __tablename__ = 'places'
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True, default=null())
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True, default=null())
        longitude = Column(Float, nullable=True, default=null())
        amenity_ids = []

        # Relationship with User
        # user = relationship("User",
        # backref=backref("places", cascade="all, delete-orphan"))
        # Relationship with City
        # cities = relationship("City",
        # backref=backref("places", cascade="all, delete-orphan"))

        # Relationship with Review
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")

    else:
        @property
        def reviews(self):
            """
            Getter attribute to return a list of Review instances with place_id
            equals to the current Place.id
            """
            from models import storage
            review_dict = storage.all(Review)
            review_list = []
            for key, value in review_dict.items():
                if self.id == value.place_id:
                    review_list.append(value)
            return review_list
