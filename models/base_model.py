#!/usr/bin/python3
"""Module containing the base class"""
import uuid
from datetime import datetime

class BaseModel():
    """Base class for all future classes"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        '''Assign the current datetime when an instance is created'''
        self.create_at = datetime.now()
        '''Give the current datetime when an object is changed'''
        self.update_at = datetime.now()

    def __str__(self):
        """String method to return prettier version of the BaseModel"""
        return ("[{}] ({}) <{}>".format(type(self).__name__, self.id,
                                        self.__dict__))

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        ret = self.__dict__

        ret["__class__"] = type(self).__name__
