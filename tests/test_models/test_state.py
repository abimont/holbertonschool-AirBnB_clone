#!/usr/bin/python3
"""
Module ``test_state``
Tests for State class
"""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test class for State
    """

    def test_state(self):
        """
        Testing State attributes
        """

        instance = State()
        self.assertEqual(instance.name, "")
