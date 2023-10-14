#!/usr/bin/python3
"""Defines BaseModel class"""

import uuid
from datetime import datetime

class BaseModel:
     """
        BaseModel class that defines all common attributes/methods for other classes

        Args:
            *args: Not used.
            **kwargs: A dict of attributes.
    """
    def __init__(self):
        """Initialize new BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """updates the pub instance updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def __str__(self):
        """string representation of a BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """returns a dict containing all keys/values of __dict__ of instance"""
        _dict = {
            key: value if key not in ["created_at", "updated_at"] else value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            for key, value in self.__dict__.items()
        }
        _dict['__class__'] = self.__class__.__name__
        return _dict
