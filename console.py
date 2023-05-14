#!/usr/bin/python3
""" Console Module """
import cmd
from shlex import split
import models
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class """
    classes = {"BaseModel": BaseModel,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Place": Place,
               "Review": Review,
               "User": User}

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ quit to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF to exit the program """
        print()
        return True

    def do_create(self, arg):
        """ creates new instance of Basemodel """
        lists = split(arg)
        if len(lists) == 0:
            print("** class name missing **")
        elif lists[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print(eval(lists[0])().id)
            storage.save()

    def do_show(self, arg):
        """ Prints the string representation of an
        instance based on the class name and id """
        lists = split(arg)
        if len(lists) == 0:
            print("** class name missing **")
        elif lists[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(lists) == 1:
            print("** instance id missing **")
        else:
            obj = models.storage.all()
            key = lists[0] + '.' + str(lists[1])
            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based
        on the class name and id """
        lists = split(arg)
        if len(lists) == 0:
            print("** class name missing **")
        elif lists[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(lists) == 1:
            print("** instance id missing **")
        else:
            obj = models.storage.all()
            key = lists[0] + '.' + lists[1]
            if key in obj:
                del obj[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name"""
        lists = split(arg)
        obj_list = []
        obj = models.storage.all()
        if len(lists) == 0:
            for key in obj:
                obj_list.append(str(obj[key]))
                print(obj_list)
        elif lists[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for key in obj:
                class_name = key.split('.')
                if class_name[0] == lists[0]:
                    obj_list. append(str(obj[key]))
            print(obj_list)

    def do_update(self, arg):
        """  Updates an instance based on the class
        name and id by adding or updating attribute"""
        lists = split(arg, " ")
        obj = models.storage.all()
        if len(lists) == 0:
            print("** class name missing **")
        elif lists[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(lists) == 1:
            print("** instance id missing **")
        elif len(lists) == 2:
            print("** attribute name missing **")
        elif len(lists) == 3:
            print("** value missing **")
        elif "{}.{}".format(lists[0], lists[1]) not in obj.keys():
            print("** no instance found **")
        key = lists[0] + '.' + lists[1]
        value = obj[key]
        try:
            value.__dict__[lists[2]] = eval(lists[3])
        except Exception:
            value.__dict__[lists[2]] = lists[3]
            value.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
