#!/usr/bin/python3
"""Test suite for Amenity class of the models.amenity module """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test cases for the Amenity class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
