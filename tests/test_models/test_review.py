#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.place_id), str)

    def test_user_id(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.user_id), str)

    def test_text(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.text), str)
