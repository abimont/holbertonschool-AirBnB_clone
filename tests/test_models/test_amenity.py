#!/usr/bin/python3
"""
Module ``test_amenity``
Tests for Amenity class
"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test class for Amenity
    """

    def test_amenity(self):
        """
        Testing Amenity attributes
        """

        instance = Amenity()
        self.assertEqual(instance.name, "")
