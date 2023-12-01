#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, null
from sqlalchemy import Table, MetaData
from sqlalchemy.orm import relationship, backref
import os


metadata = MetaData()

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column('place_id', String(60), ForeignKey("places.id"),
    primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey("amenities.id"),
    primary_key=True, nullable=False)
    )

class Place(BaseModel, Base):
    """ Place class """
    __tablename__ = 'places'

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
    amenities = relationship("Amenity", secondary="place_amenity",
                                viewonly=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
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

        @property
        def amenities(self):
            """
            returns list of Amenity instances base on atrribute amenity_ids
            that contains all Amenity.id linked to Place
            """
            from models import storage
            amenity_values = storage.all(Amenity).values()
            amenity_list = []
            for amenity in amenity_values:
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list
        
        @amenities.setter
        def amenities(self, value):
            """
            handles append for adding Amenity.id to attribute amenity_ids
            """
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)

