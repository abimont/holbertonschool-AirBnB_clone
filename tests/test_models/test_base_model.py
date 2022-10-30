#!/usr/bin/python3
"""
Module ``test_base_model``
Tests for BaseModel class
"""
import json
import os
import unittest
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """
    Test Functions
    """

    def setUp(self):
        """
        Setting up the instances
        """

        self.instanceOne = BaseModel()
        self.instanceTwo = BaseModel()

    def test_BaseModel(self):
        """
        Testing:
            - save() method
            - updated_at attribute
        """

        storage.all().clear()
        instanceBM = BaseModel()
        instanceBM.save()
        with open('file.json') as file:
            loaded = json.loads(file.read())
        self.assertDictEqual(
            loaded, {f'BaseModel.{instanceBM.id}': instanceBM.to_dict()})
        os.remove('file.json')

    def test_id(self):
        """
        Testing if every instances's id is unique
        """

        self.assertNotEqual(self.instanceOne.id, self.instanceTwo.id)

    def test_dict(self):
        """
        Testing to_dict() method
        """

        self.assertIn("id", self.instanceOne.to_dict())
        self.assertIn("__class__", self.instanceOne.to_dict())
        self.assertIn("created_at", self.instanceOne.to_dict())
        self.assertIn("updated_at", self.instanceOne.to_dict())

    def test_str(self):
        """
        Testing __str__() method
        """

        self.assertIsInstance(self.instanceOne.__str__(), str)
        self.assertIn(self.instanceOne.id, self.instanceOne.__str__())
        self.assertIn(type(self.instanceOne).__name__,
                      self.instanceOne.__str__())
