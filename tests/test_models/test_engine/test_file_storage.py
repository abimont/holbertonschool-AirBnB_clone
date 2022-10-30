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
        """
        Testing FileStorage methods
        """
        dicOne = FileStorage.all(self)
        self.assertIsInstance(dicOne, dict)
        self.assertEqual(len(dicOne), 0)
        instanceBase = BaseModel()
        self.assertGreater(len(dicOne), 0)

    def test_save(self):
        """
        Provisional test
        """
        instanceBM = BaseModel()
        instanceFS = FileStorage()
        self.assertEqual(instanceBM.save(), None)
        self.assertEqual(instanceFS.reload(), None)

    def test_object(self):
        """
        Testing FileStorage attributes
        """
        instance = FileStorage()
        with self.assertRaises(AttributeError):
            instance.__objects
            instance.__file_path
