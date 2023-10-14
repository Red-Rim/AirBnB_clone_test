#!/usr/bin/python3
"""
Module of AIRBNB console
"""

import cmd
from models.base_model import BaseModel
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
