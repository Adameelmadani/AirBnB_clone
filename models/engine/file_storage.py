#!/usr/bin/python3
"""Defines FileStorage class and its methods."""
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json
import os


class FileStorage:
    """
    A class to manage storage and serialization of objects.

    This class provides methods for managing and serializing objects to a JSON
    file. Objects are stored in the class attribute __objects, a dictionary.

    Attributes:
        __file_path (str): The path to the JSON file for storage.
        __objects (dict): A dictionary containing objects for storage.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve all objects stored in the storage.

        This method returns the dictionary containing all objects stored in
        the class attribute __objects.

        Args:
        None

        Returns:
        dict: A dictionary containing all objects stored in the storage.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the storage dictionary.

        This method adds the given object to the dictionary of objects stored
        in the class attribute __objects. The object is stored with a key
        constructed using the object's class name and its unique ID.

        Args:
            obj (BaseModel): The object to be added to the storage.

        Returns:
            None
        """
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """
        Save dict of objects to the JSON file.

        This method iterates through the dictionary of objects stored in the
        class attribute __objects. For each key-value pair, it converts the
        value (ex. <models.base_model.BaseModel object at 0x7f5594b968c0>) to
        a dictionary representation using the `to_dict()` method of the value,
        and creates new dictionary containing these converted representations.

        The resulting dictionary is then serialized to a JSON file specified
        by the class attribute __file_path, effectively updating the JSON file
        with the current state of the objects.

        Args:
        None

        Returns:
        None
        """
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            new_dict = {}
            for key, value in FileStorage.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        """
        Deserializes JSON file to __objects only if it exists
        Otherwise, do nothing
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value["__class__"]
                    attributes = {}
                    for k, v in value.items():
                        if k != "__class__":
                            attributes[k] = v
                    new_instance = eval(class_name)(**attributes)
                    self.new(new_instance)
