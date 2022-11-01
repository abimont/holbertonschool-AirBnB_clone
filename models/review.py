#!/usr/bin/python3
"""
Module ``review``
Class that inherits from BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class that cointains the review of the place
    """

    place_id = ""
    user_id = ""
    text = ""
