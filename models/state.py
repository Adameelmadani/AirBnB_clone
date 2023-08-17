#!/usr/bin/python3
"""
state model
"""
from models.base_model import BaseModel
"""
Importing BaseModel -> Parent class of State
"""


class State(BaseModel):
    """
    State class inherits form BaseModel
    """
    name = ""
