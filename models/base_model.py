#!/usr/bin/python3
"""
Base models for all the classes 
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    A class named Base Model

    Attributes
    id:string - assign with an uuid when an instance is created
    created_at: datetime - assign with the current datetime when an instance is created
    updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
    """
    def __init__(self, *args, **kwargs):
        """ Initialize the base model"""
        if kwargs:
	    for key, value in kwargs.items():
		if key == 'created_at' or key == 'updated_at':
		    dt_obj = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
		    setattr(self, key, dt_obj)
		elif key != "__class":
		    setattr(self, key, value)
        else:
	    self.id = str(uuid4())
	    self.created_at = datetime.now()
	    self.updated_at = datetime.now()
	    models.storage.new(self)

    def __str__(self):
	"""Returns the string representation of the class Instance"""
	return "[{}] ({}) {}".format(self.__classs__.__name__,self.id, self.__dict__)

    def save(self):
	"""updates the public instance attribute updated_at with the current datetime"""
	self.updated_at = datetime.now()
	models.storage.save()

    def to_dict(self):
	"""returns a dictionary containing all keys/values of __dict__ of the instance"""
	new_dict = self.__dict__.copy()
	new_dict['created_at'] = datetime.isoformat(newdict['created_at'])
	new_dict['updated_at'] = datetime.isoformat(newdict['updated_at'])
	new_dict['__class__'] = self.__class__.__name__
	return newdict
