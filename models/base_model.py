#!/usr/bin/pyton3
"""
Module ``base_model``
BaseModel class for command interpreter
"""


from datetime import datetime
import uuid


class BaseModel:
    """
    Class that defines all common attributes/methods for other classes
    """

    def __init__(self):
        """
        Constructor method
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        __str__ method that returns a class description
        """

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with the
        current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """

        inst_dict = self.__dict__.copy()
        inst_dict['__class__'] = type(self).__name__
        inst_dict['created_at'] = self.created_at.isoformat()
        inst_dict['updated_at'] = self.updated_at.isoformat()
        return inst_dict
