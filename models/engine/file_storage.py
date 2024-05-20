#!/usr/bin/python3
"""Storge all the data
"""
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """Class foe storge the data
    """
    __file_path = "file.json"
    __objects = {} 
    
    
    def all(self):
        """Return privite __objects
        """
        return self.__objects
    
    def new(self, obj):
        """Add a new object
        """
        obj_name = obj.__class__.__name__
        key = f"{obj_name}.{obj.id}"
        self.__objects[key] = obj
    def save(self):
        """Save object to the file.
        """
        objs = self.__objects
        obj_dict = {}
        for key, value in objs.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(obj_dict, f)
    def reload(self):
        """Load the object from the file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                try:        
                    obj2 = json.load(f)
                    for key, value in obj2.items():
                        name, obj_id = key.split(".")
                        esra = eval(name)
                        hind = esra(**value)
                        FileStorage.__objects[key] = hind
                except Exception:
                    pass

if __name__ == "__main__":
    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)
