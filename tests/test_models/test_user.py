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
        storage = FileStorage()
        instUser = User()
        instUser.first_name = "Betty"
        instUser.last_name = "Bar"
        instUser.email = "airbnb@mail.com"
        instUser.password = "root"
        instUser.save()
        val = storage.all().get(f'User.{instUser.id}')
        self.assertEqual(val.__dict__['first_name'], instUser.first_name)
        self.assertEqual(val.__dict__['last_name'], instUser.last_name)
        self.assertEqual(val.__dict__['email'], instUser.email)
        self.assertEqual(val.__dict__['password'], instUser.password)
        storage.all().clear()
        os.remove('file.json')
