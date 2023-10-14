#!/usr/bin/python3
"""
Build the BaseModel Class
"""
import uuid
import models
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        _dict = {
            key: value if key not in ["created_at", "updated_at"] else value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            for key, value in self.__dict__.items()
        }
        _dict['__class__'] = self.__class__.__name__
        return _dict
