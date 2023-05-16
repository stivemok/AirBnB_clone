#!/usr/bin/python3
"""Test suite for Amenity class of the models.amenity module """
import unittest
import models
import os
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def tesst__init__amenity(self):
        """ test type amenity"""
        myobject = Amenity()
        self.assertIsInstance(myobject, Amenity)

    def test_docstring(self):
        """ test docstring"""
        message1 = "Class doesn't have docstring"
        self.assertIsNotNone(Amenity.__doc__, message1)
        message2 = "Modulo doesn't have docstring"
        self.assertIsNotNone(Amenity.__doc__, message2)

    def test_executable(self):
        """test executable permission"""
        is_write_true = os.access('models/amenity.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_read_true = os.access('models/amenity.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_exec_true = os.access('models/amenity.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_id(self):
        """ test if id is unique """
        myobjid = Amenity()
        myobjid1 = Amenity()
        self.assertNotEqual(myobjid.id, myobjid1.id)

    def test_str(self):
        """ check if str output """
        my_str_obj = Amenity()
        dic = my_str_obj.__dict__
        str1 = "[Amenity] ({}) {}".format(my_str_obj.id, dic)
        str2 = str(my_str_obj)
        self.assertEqual(str1, str2)

    """def test_save(self):
         check update when save
        update = Amenity()
        first_update = update.updated_at
        update.save()
        second_update = update.update_at
        self.assertNotEqual(first_update, second_update)"""

    def test_to_dict(self):
        """ check if to_dict returns a dictionary """
        model = Amenity()
        dict_model = model.to_dict()
        self.assertIsInstance(dict_model, dict)
        for key, value in dict_model.items():
            flag = 0
            if dict_model['__class__'] == 'Amenity':
                flag += 1
                self.assertTrue(flag == 1)
        for key, value in dict_model.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
