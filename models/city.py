#!/usr/bin/python3
"""
city model
"""
from models.base_model import BaseModel
"""
Importing BaseModel -> Parent class of City
"""


class City(BaseModel):
    """
    City class inherits form BaseModel
    """
    state_id = ""
    name = ""
