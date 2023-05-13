#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models common attributes/methods
    Public instance attributes:
    id: string - assign with an uuid when an instance is created:
        uuid.uuid4(): generate unique id but uuid4() used to convert to string
        the goal is to have unique id for each BaseModel
    created_at: datetime - assign with the current datetime when an instance
        is created
    updated_at: datetime - assign with the current datetime when an instance
        is created and it will be updated every time you change your object
    """

    def __init__(self, *args, **kwargs):
        """*args , **kwargs allow class accpet vaiable number of argument and keyword arguments during initialization
        Instatntiates a new model"""
        if not kwargs:

            from AirBnB_clone import storage

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
            del kwargs["__class__"]
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split(".")[-1]).split("'")[0]
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from AirBnB_clone import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format
        This Method will be first piece of the serialization/Deserialization process create dictionary simple object type of BaseModel
        """
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({"__class__": (str(type(self)).split(".")[-1]).split("'")[0]})
        """convert creat_at & update_at string objects into into ISO format"""
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
