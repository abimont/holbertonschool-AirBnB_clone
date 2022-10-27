#!/usr/bin/python3
"""
Module ``test_base_model``
Tests for BaseModel class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test Functions
    """

    def setUp(self):
        self.instanceOne = BaseModel()
        self.instanceTwo = BaseModel()

    def test_BaseModel(self):
        firstUpdate = self.instanceOne.updated_at
        self.instanceOne.save()
        secondUpdate = self.instanceOne.updated_at
        self.assertNotEqual(firstUpdate, secondUpdate)

    def test_id(self):
        self.assertNotEqual(self.instanceOne.id, self.instanceTwo.id)

    def test_dict(self):
        self.assertIn("id", self.instanceOne.to_dict())
        self.assertIn("__class__", self.instanceOne.to_dict())
        self.assertIn("created_at", self.instanceOne.to_dict())
        self.assertIn("updated_at", self.instanceOne.to_dict())
