#!/usr/bin/python3
"""Defines User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class to Represent User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
