import unittest
import os
import json
from models.base_model import BaseModel
from engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        FileStorage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_empty(self):
        objects = self.storage.all()
        self.assertEqual(len(objects), 0)

    def test_new_and_all(self):
        obj = BaseModel()
        self.storage.new(obj)
        objects = self.storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIn(f"BaseModel.{obj.id}", objects)

    def test_save_and_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        
        # Clear the storage and load from the file
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        
        objects = self.storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIn(f"BaseModel.{obj.id}", objects)
        self.assertIsInstance(objects[f"BaseModel.{obj.id}"], BaseModel)

    def test_reload_existing_file(self):
        # Create a test file with object data
        obj_data = {
            "BaseModel.123": {
                "id": "123",
                "__class__": "BaseModel",
                "name": "Test Object"
            }
        }
        with open(self.file_path, "w") as f:
            json.dump(obj_data, f)

        # Reload the objects from the file
        self.storage.reload()
        objects = self.storage.all()

        self.assertEqual(len(objects), 0)
if __name__ == "__main__":
    unittest.main()
