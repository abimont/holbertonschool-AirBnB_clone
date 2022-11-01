#!/usr/bin/python3
"""
Module ``test_user``
Tests for User class
"""
import unittest
import os
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """
    Test Functions
    """

    def test_user(self):
        """
        Testing user attributes
        """

        instUser = User()
        self.assertEqual(instUser.first_name, "")
        self.assertEqual(instUser.last_name, "")
        self.assertEqual(instUser.email, "")
        self.assertEqual(instUser.password, "")
