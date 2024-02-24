#!/usr/bin/python3
"""File storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """Serialization class instances to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Dictionary returnd"""
        dic = {}
        if cls:
            dic = self.__objects
            for key in dic:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key] = self.__objects[key]
            return (dic)
        else:
            return self.__objects

    def new(self, obj):
        """__object to given obj set"""
        if obj:
            k = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[k] = obj

    def save(self):
        """File path to JSON file path serialized
        """
        myDict = {}
        for key, value in self.__objects.items():
            myDict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(myDict, f)

    def reload(self):
        """File path to JSON file path serializd
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Existing element deleted
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """Reload() called
        """
        self.reload()
