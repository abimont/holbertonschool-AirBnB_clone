#!/usr/bin/python3
"""
Module ``test_city``
Tests for City class
"""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test class for City
    """

    def test_city(self):
        """
        Testing City attributes
        """

        instance = City()
        self.assertEqual(instance.state_id, "")
        self.assertEqual(instance.name, "")
