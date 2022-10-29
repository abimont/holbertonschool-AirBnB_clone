#!/usr/bin/python3
"""
Module ``test_file_storage``
Tests for FileStorage class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    Tests FileStorage class methods
    """

    def test_file_storage(self):
        dicOne = FileStorage.all(self)
        self.assertIsInstance(dicOne, dict)
        self.assertEqual(len(dicOne), 0)
        instanceBase = BaseModel()
        self.assertGreater(len(dicOne), 0)
