#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models import storage
from models.base_model import BaseModel
import os


class test_fileStorage(unittest.TestCase):
    """ File storage method test"""

    def setUp(self):
        """ Test environment setup"""
        delList = []
        for k in storage._FileStorage__objects.keys():
            delList.append(k)
        for k in delList:
            del storage._FileStorage__objects[k]

    def tearDown(self):
        """ Storage file at end of tests removd"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        nw = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        nw = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        nw = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        nw = BaseModel()
        thing = new.to_dict()
        nw.save()
        nw2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        nw = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        nw = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loded = obj
        self.assertEqual(nw.to_dict()['id'], loded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ File does not exist nothing happns"""
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        nw = BaseModel()
        nw.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ __file_path type test.is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ __objects type confimation.is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        nw = BaseModel()
        _id = nw.to_dict()['id']
        for k in storage.all().keys():
            temp = k
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)
