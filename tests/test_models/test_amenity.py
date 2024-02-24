#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from datetime import datetime
from time import sleep
from models.amenity import Amenity
from models.base_model import BaseModel
from os import getenv
from unittest.mock import patch
import pycodestyle
import inspect
import unittest
storage_t = getenv("HBNB_TYPE_STORAGE")

class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


class Test_PEP8(unittest.TestCase):
    """test User"""
    def test_pep8_user(self):
        """test pep8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_inherit_basemodel(unittest.TestCase):
    """Test if user inherit from BaseModel"""
    def test_instance(self):
        """check if user is an instance of BaseModel"""
        user = Amenity()
        self.assertIsInstance(user, Amenity)
        self.assertTrue(issubclass(type(user), BaseModel))
        self.assertEqual(str(type(user)), "<class 'models.amenity.Amenity'>")


class test_Amenity_BaseModel(unittest.TestCase):
    """Testing user class"""
    def test_instances(self):
        with patch('models.amenity'):
            instance = Amenity()
            self.assertEqual(type(instance), Amenity)
            instance.name = "Barbie"
            expectec_attrs_types = {
                    "id": str,
                    "created_at": datetime,
                    "updated_at": datetime,
                    "name": str,
                    }
            inst_dict = instance.to_dict()
            expected_dict_attrs = [
                    "id",
                    "created_at",
                    "updated_at",
                    "name",
                    "__class__"
                    ]
            self.assertCountEqual(inst_dict.keys(), expected_dict_attrs)
            self.assertEqual(inst_dict['name'], 'Barbie')
            self.assertEqual(inst_dict['__class__'], 'Amenity')

            for attr, types in expectec_attrs_types.items():
                with self.subTest(attr=attr, typ=types):
                    self.assertIn(attr, instance.__dict__)
                    self.assertIs(type(instance.__dict__[attr]), types)
            self.assertEqual(instance.name, "Barbie")

    def test_user_id_and_createat(self):
        """testing id for every user"""
        usr1 = Amenity()
        sleep(2)
        usr2 = Amenity()
        sleep(2)
        usr3 = Amenity()
        sleep(2)
        list_users = [usr1, usr2, usr3]
        for instance in list_users:
            user_id = instance.id
            with self.subTest(user_id=user_id):
                self.assertIs(type(user_id), str)
        self.assertNotEqual(usr1.id, usr2.id)
        self.assertNotEqual(usr1.id, usr3.id)
        self.assertNotEqual(usr2.id, usr3.id)
        self.assertTrue(usr1.created_at <= usr2.created_at)
        self.assertTrue(usr2.created_at <= usr3.created_at)
        self.assertNotEqual(usr1.created_at, usr2.created_at)
        self.assertNotEqual(usr1.created_at, usr3.created_at)
        self.assertNotEqual(usr3.created_at, usr2.created_at)

    def test_str_method(self):
        """
        Testin str magic method
        """
        ins = Amenity()
        str_output = "[Amenity] ({}) {}".format(ins.id, ins.__dict__)
        self.assertEqual(str_output, str(ins))

    @patch('models.storage')
    def test_save_method(self, mock_storage):
        """Save method test"""
        inst5 = Amenity()
        created_at = inst5.created_at
        sleep(2)
        updated_at = inst5.updated_at
        inst5.save()
        new_created_at = inst5.created_at
        sleep(2)
        new_updated_at = inst5.updated_at
        self.assertNotEqual(updated_at, new_updated_at)
        self.assertEqual(created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)


class TestAmenity(unittest.TestCase):
    """Test for Amenity class"""

    def test_is_subclass(self):
        """Tests Amenity if is subclass of BaseModel"""
        amty = Amenity()
        self.assertIsInstance(amty, BaseModel)
        self.assertTrue(hasattr(amty, "id"))
        self.assertTrue(hasattr(amty, "created_at"))
        self.assertTrue(hasattr(amty, "updated_at"))

    def test_name_attr(self):
        """Test that Amenity for attribute name, and it's as an empty string"""
        amty = Amenity()
        self.assertTrue(hasattr(amty, "name"))
        if storage_t == 'db':
            self.assertEqual(amty.name, None)
        else:
            self.assertEqual(aty.name, "")

    def test_to_dict_creates_dict(self):
        """tests that dictionary with proper attrs created by to_dict"""
        amty = Amenity()
        print(amty.__dict__)
        nd = amty.to_dict()
        self.assertEqual(type(nd), dict)
        self.assertFalse("_sa_instance_state" in nd)
        for attr in amty.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in nd)
        self.assertTrue("__class__" in nd)

    def test_to_dict_values(self):
        """test for correct to_dict return value"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        amty = Amenity()
        nd = amty.to_dict()
        self.assertEqual(type(nd["created_at"]), str)
        self.assertEqual(type(nd["updated_at"]), str)
        self.assertEqual(nd["__class__"], "Amenity")
        self.assertEqual(nd["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(nd["updated_at"], am.updated_at.strftime(t_format))

    def test_str(self):
        """test for correct output of str methon"""
        amty = Amenity()
        string = "[Amenity] ({}) {}".format(amty.id, amty.__dict__)
        self.assertEqual(string, str(amty))
