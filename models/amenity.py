#!/usr/bin/python3
"""
amenity model
"""
from models.base_model import BaseModel
"""
Importing BaseModel -> Parent class of Amenity
"""


class Amenity(BaseModel):
    """
    Amenity class inherits form BaseModel
    """
    name = ""
