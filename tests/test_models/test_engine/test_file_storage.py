#!/usr/bin/python3
"""
Module ``test_file_storage``
Tests for FileStorage class
"""
import json
import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Tests FileStorage class methods
    """

    def test_file_storage_attributes(self):
        """
        Testing FileStorage atributtes
        """
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, 'file.json')
        self.assertDictEqual(storage._FileStorage__objects, {})

    def test_file_storage_methods(self):
        """
        Testing FileStorage methods
        """
        storage = FileStorage()
        self.assertDictEqual(storage.all(), {})
        instanceBM = BaseModel()
        self.assertDictEqual(storage.all(),
                             {f'BaseModel.{instanceBM.id}': instanceBM})
        storage.save()
        with open('file.json') as file:
            loaded = json.loads(file.read())
        self.assertDictEqual(
            loaded, {f'BaseModel.{instanceBM.id}': instanceBM.to_dict()})
        storage.all().clear()
        storage.reload()
        self.assertEqual(storage.all().get(
            f'BaseModel.{instanceBM.id}').id, instanceBM.id)
        storage.all().clear()
        os.remove('file.json')
