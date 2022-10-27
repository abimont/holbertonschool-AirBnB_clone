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
    __object = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__object

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        Args:
            - obj: object to convert in dictionary
        """

        FileStorage.__object[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        """"
        Serializes __objects to the JSON file (path: __file_path)
        """

        with open(FileStorage.__file_path, "w+", encoding="UTF-8") as file:
            dic = {k: v.to_dict() for k, v in FileStorage.__object.items()}
            json.dump(dic, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects only if
        the JSON file (__file_path) exists otherwise, do nothing
        """
        from models.base_model import BaseModel
        if not os.path.isfile(FileStorage.__file_path):
            return
        try:
            with open(FileStorage.__file_path) as file:
                loaded = json.load(file)
                for k, v in loaded.items():
                    obj = eval(v["__class__"])(**v)
                    FileStorage.__object[k] = obj
        except Exception:
            pass
