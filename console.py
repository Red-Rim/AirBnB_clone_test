#!/usr/bin/python3
"""define console module for AirBnB clone"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, l):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, l):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, l):
        """Create a new instance of a class, save it, and print the id"""
        if not l:
            print("** class name missing **")
        elif l not in storage.classes:
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[l]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, l):
        """Print the string representation of an instance"""
        args = l.split()
        if not l:
            print("** class name missing **")
        elif args[0] not in storage.all():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + '.' + args[1]
            objects = storage.all()
            if obj_key in objects:
                print(objects[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, l):
        """Deletes an instance based on the class name and id"""
        args = l.split()
        if not l:
            print("** class name missing **")
        elif args[0] not in storage.all():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + '.' + args[1]
            objects = storage.all()
            if obj_key in objects:
                del objects[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, l):
        """Print all string representations of instances"""
        objects = storage.all()
        if not l:
            print([str(obj) for obj in objects.values()])
        elif l not in storage.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in objects.items() if key.split('.')[0] == l])

    def do_update(self, l):
        """Update an instance based on the class name and id"""
        args = l.split()
        if not l:
            print("** class name missing **")
        elif args[0] not in storage.all():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj_key = args[0] + '.' + args[1]
            objects = storage.all()
            if obj_key in objects:
                obj = objects[obj_key]
                atr_name = args[2]
                atr_value = args[3]
                if atr_name in obj.__class__.__dict__:
                    atr_value = type(obj.__class__.__dict__[atr_name])(atr_value)
                    setattr(obj, atr_name, atr_value)
                    obj.save()
                else:
                    print("** attribute doesn't exist **")
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

