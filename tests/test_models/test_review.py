#!/usr/bin/python3
"""
Module ``test_review``
Tests for Review class
"""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test class for Review
    """

    def test_review(self):
        """
        Testing Review attributes
        """

        instance = Review()
        self.assertEqual(instance.place_id, "")
        self.assertEqual(instance.user_id, "")
        self.assertEqual(instance.text, "")
