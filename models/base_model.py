#!/usr/bin/python3
"""
This module defines the BaseModel class.

BaseModel serves as the base class for other classes in the project,
providing common attributes and methods for object management and serializ.
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    A base class for all project-specific classes.

    Attributes:
        id (str): A unique identifier generated using uuid4.
        created_at (datetime): The date and time when the object is created.
        updated_at (datetime): The date and time when the object last updated.

    Methods:
        __init__(self, *args, **kwargs): Initializes a new instance of class.
        __str__(self): Returns a formatted string representation of object.
        save(self): Updates the 'updated_at' attribute and saves object.
        to_dict(self): Returns a dictionary representation of object.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        Args:
            *args: Variable length argument list (not used).
            **kwargs: Arbitrary keyword arguments used for object initializ.
                If provided, the attributes of object are set based on values.
                If not provided, the object is created with a new unique ID
                and timestamps and saved to file.
        """
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, date_format)
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the object.

        Returns:
            str: A formatted string with class name, ID, and attribute dict.
        """
        f_p = "[{}] ({}) ".format(self.__class__.__name__, self.id)
        s_p = "{}".format(self.__dict__)
        return (f_p + s_p)

    def save(self):
        """
        Update the 'updated_at' attribute and save the object.

        This method updates the 'updated_at' atrb to the current date and time,
        and then triggers the saving of the object using the storage system.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert the object to a dictionary representation.

        Returns:
            dict containing the object's attributes and class information.
        """
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()

        return new_dict
