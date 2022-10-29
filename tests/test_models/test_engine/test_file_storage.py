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
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertEqual(len(all_objs), 0)
        instanceBase = BaseModel()
        instanceBase.save()
        self.assertGreater(len(all_objs), 0)
