#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
import os

Base = object
if os.getenv("HBNB_TYPE_STORAGE") == "db":
    Base = declarative_base()


class BaseModel:
    """Adding attributes in class"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            # convert string rep to objects
            if 'created_at' in kwargs and kwargs['created_at'] is not None:
                self.created_at = datetime.strptime(self.created_at,
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs and kwargs['updated_at'] is not None:
                self.updated_at = datetime.strptime(self.updated_at,
                                                    '%Y-%m-%dT%H:%M:%S.%f')
        # if no id, generate new UUID
        if not getattr(self, 'id', None) is None:
            self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        for key, value in dictionary.items():
            if isinstance(value, datetime):
                dictionary[key] = value.isoformat()
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        storage.delete(self)
