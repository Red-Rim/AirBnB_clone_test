#!/usr/bin/python3
"""Define FileStorage Class"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
import json
import os
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    """
    FileStorage class to data

    Attributes:
        __file_path (str): the file to save obj to
        __objects (dict): A dictionary to store instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """stores an object on the objects dictionary"""
        objt = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objt, obj.id)] = obj

    def save(self):
        """Serialize __objects to  JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)
