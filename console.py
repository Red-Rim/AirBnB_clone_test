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


    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """C-d command to exit the program\n"""
        print()
	return True

    def emptyline(self):
        """an empty line handling"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
