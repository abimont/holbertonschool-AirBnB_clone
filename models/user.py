#!/usr/bin/python3
"""
Module ``user``
User attributes
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User that inherits from BaseModel
    This class has the user data
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
