#!/usr/bin/python3
"""
Module ``test_file_storage``
Tests for FileStorage class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """
    Tests FileStorage class methods
    """

    def setUp(self):
        """
        Setting up an instance
        """

        self.instanceBM = BaseModel()
        self.instanceFS = FileStorage()
