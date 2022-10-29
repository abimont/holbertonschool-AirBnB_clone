#!/usr/bin/pyton3
"""
Module ``base_model``
BaseModel class for command interpreter
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """
    Class that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method

        Args:
            - args: unused parameter
            - kwargs: each key of this dictionary is an attribute name
        """

        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(self.created_at,
                                                '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(self.updated_at,
                                                '%Y-%m-%dT%H:%M:%S.%f')

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

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
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """

        inst_dict = self.__dict__.copy()
        inst_dict['created_at'] = self.created_at.isoformat()
        inst_dict['updated_at'] = self.updated_at.isoformat()
        inst_dict['__class__'] = self.__class__.__name__
        return inst_dict
