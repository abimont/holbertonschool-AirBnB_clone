#!/usr/bin/python3
"""
Module ``console``
Class HBNBCommand that creates the console.
"""
import cmd
from models.base_model import BaseModel
import models
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """
    Class that contains the entry point of the command interpreter.
    """
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'Place',
               'City', 'Amenity', 'State', 'Review']

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Clean way to exit
        """
        return True

    def emptyline(self):
        """
        Empty line doesn't execute anything
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel and
        saves it (to the JSON file) and prints the id.
        """

        if len(line) <= 0:
            print("** class name missing **")
            return False
        elif line == "BaseModel":
            instance = BaseModel()
        elif line == "User":
            instance = User()
        elif line == "City":
            instance = City()
        elif line == "Place":
            instance = Place()
        elif line == "Amenity":
            instance = Amenity()
        elif line == "State":
            instance = State()
        elif line == "Review":
            instance = Review()
        else:
            print("** class doesn't exist **")
            return False

        instance.save()
        print(instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """

        myList = line.split()

        if len(myList) == 0:
            print("** class name missing **")
            return False
        if len(myList) == 1:
            print("** instance id missing **")
            return False

        instanceName, instanceId, *otherArgs = myList

        if instanceName not in self.classes:
            print("** class doesn't exist **")
            return False

        instance = models.storage.all().get(f'{instanceName}.{instanceId}')

        if not instance:
            print("** no instance found **")
            return False

        print(instance)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        """

        myList = line.split()

        if len(myList) == 0:
            print("** class name missing **")
            return False
        elif len(myList) == 1:
            print("** instance id missing **")
            return False

        instanceName, instanceId, *otherArgs = myList
        if instanceName not in self.classes:
            print("** class doesn't exist **")
            return False

        instance = models.storage.all().get(f'{instanceName}.{instanceId}')
        if not instance:
            print("** no instance found **")
            return False

        del models.storage.all()[f'{instanceName}.{instanceId}']
        models.storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """

        myDict = models.storage.all()
        if line:
            if line not in self.classes:
                print("** class doesn't exist **")
                return False
            else:
                for k, v in myDict.items():
                    if k.split('.')[0] == line:
                        print([str(v)])
        else:
            for k, v in myDict.items():
                print([str(v)])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """

        myList = line.split()
        myDict = models.storage.all()

        if len(myList) == 0:
            print("** class name missing **")
            return False
        elif len(myList) == 1:
            print("** instance id missing **")
            return False
        elif len(myList) == 2:
            print("** attribute name missing **")
            return False
        elif len(myList) == 3:
            print("** value missing **")
            return False

        instName, instId, instAttr, instVal, *otherArgs = myList
        if instName not in self.classes:
            print("** class doesn't exist **")
            return False

        instance = models.storage.all().get(f'{instName}.{instId}')
        if not instance:
            print("** no instance found **")
            return False

        instance.__dict__[instAttr] = instVal
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
