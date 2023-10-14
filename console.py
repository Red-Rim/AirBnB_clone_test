#!/usr/bin/python3
"""
Module of AIRBNB console
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import shlex
import sys
import json


class HBNBCommand(cmd.Cmd):
    """
    define HBNBCommand class

    Classe Attributes:
        prompt (str): The prompt.
        classes_list (list): A list of all used class names.
    """

    prompt = "(hbnb) "
    classes_list = ["BaseModel", "User", "State", "City\
", "Amenity", "Place", "Review"]

    
    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """C-d command to exit the program\n"""
        return True

    def emptyline(self):
        """an empty line handling"""
