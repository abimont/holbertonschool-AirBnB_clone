#!/usr/bin/python3
"""
Module ``file_storage``
Class FileStorage for JSON serialization and deserialization
"""
import json
import os


class FileStorage:
    """
    Class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        Args:
            - obj: object to convert in dictionary
        """

        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """"
        Serializes __objects to the JSON file (path: __file_path)
        """

        with open(FileStorage.__file_path, "w", encoding="UTF-8") as file:
            dic = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dic, file, indent=4)

    def reload(self):
        """
        Deserializes the JSON file to __objects only if
        the JSON file (__file_path) exists otherwise, do nothing
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.review import Review
        from models.city import City
        from models.amenity import Amenity

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path) as file:
                loaded = json.load(file)
                for k, v in loaded.items():
                    obj = eval(v["__class__"])(**v)
                    self.__objects[k] = obj
        else:
            return
