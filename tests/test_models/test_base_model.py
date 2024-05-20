#!/usr/bin/python3
"""Unittest model to test all moduls
"""
import unittest
from models.base_model import BaseModel
class testBaseModel(unittest.TestCase):
    def test_init(self):
        model1 = BaseModel()
        self.assertIsNotNone(model1.id)
        self.assertIsNotNone(model1.created_at)
        self.assertIsNotNone(model1.updated_at)
    def test_save(self):
        model1 = BaseModel()
        self.assertNotEqual(model1.updated_at, model1.save())
    def test_to_dict(self):
        model1 = BaseModel()
        model2 = model1.to_dict()
        self.assertIsInstance(model2, dict)
        self.assertEqual(model2["__class__"], 'BaseModel')
        self.assertEqual(model2["id"], model1.id)
        self.assertEqual(model2["created_at"], model1.created_at.isoformat())
        self.assertEqual(model2["updated_at"], model1.updated_at.isoformat())
    def test_str(self):
        model1 = BaseModel()
        self.assertTrue(str(model1). startswith('[BaseModel]'))
        self.assertIn(model1.id, str(model1))
        self.assertIn(str(model1.__dict__), str(model1))


if __name__ == "__main__":
    unittest.main()
