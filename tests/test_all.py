#!/usr/bin/python3
"""
Module ``test_all``
Tests for all classes
"""


import unittest
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review


class TestAll(unittest.TestCase):
    """
    Test class for all classes of AirBnB clone project
    """

    def test_base(self):
        """
        Testing BaseModel
        """

        instance = BaseModel()
        self.assertEqual(
            str(instance), f'[BaseModel] ({instance.id}) {instance.__dict__}')

    def test_city(self):
        """
        Testing City
        """

        instance = City()
        self.assertEqual(instance.state_id, "")

    def test_state(self):
        """
        Testing State
        """

        instance = State()
        self.assertEqual(instance.name, "")

    def test_place(self):
        """
        Testing Place
        """

        instPlace = Place()
        self.assertEqual(instPlace.city_id, "")
        self.assertEqual(instPlace.number_rooms, 0)
        self.assertEqual(instPlace.amenity_ids, [])

    def test_amenity(self):
        """
        Testing Amenity
        """

        instance = Amenity()
        self.assertEqual(instance.name, "")

    def test_user(self):
        """
        Testing User
        """

        instUser = User()
        self.assertEqual(instUser.first_name, "")

    def test_review(self):
        """
        Testing Review attributes
        """

        instance = Review()
        self.assertEqual(instance.text, "")
