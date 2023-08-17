#!/usr/bin/python3
"""
review model
"""
from models.base_model import BaseModel
"""
Importing BaseModel -> Parent class of Review
"""


class Review(BaseModel):
    """
    Review class inherits form BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
