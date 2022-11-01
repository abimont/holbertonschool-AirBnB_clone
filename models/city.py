#!/usr/bin/python3
"""
Module ``city``
Class that inherits from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    Class that defines the city
    """

    state_id = ""
    name = ""
