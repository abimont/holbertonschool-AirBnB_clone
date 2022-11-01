#!/usr/bin/python3
"""
Module ``test_place``
Tests for Place class
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test Functions
    """

    def test_place(self):
        """
        Testing Place attributes
        """

        instPlace = Place()
        self.assertEqual(instPlace.city_id, "")
        self.assertEqual(instPlace.user_id, "")
        self.assertEqual(instPlace.name, "")
        self.assertEqual(instPlace.description, "")
        self.assertEqual(instPlace.number_rooms, 0)
        self.assertEqual(instPlace.number_bathrooms, 0)
        self.assertEqual(instPlace.max_guest, 0)
        self.assertEqual(instPlace.price_by_night, 0)
        self.assertEqual(instPlace.latitude, 0.0)
        self.assertEqual(instPlace.longitude, 0.0)
        self.assertEqual(instPlace.amenity_ids, [])
