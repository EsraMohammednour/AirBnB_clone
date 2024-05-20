#!/usr/bin/python3
"""Base module to write Airbnb
"""

import uuid
import datetime
import models


class BaseModel:
    """ class base for all other classes with:
    BaseModelBaseModel: id
    """
    def __init__(self, *args, **kwargs):
        """Initialization of the attributes
        """

        time = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.datetime.strptime(value, time))
        else:
            id = uuid.uuid4()
            self.id = str(id)
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def save(self):

        """To update the update_at with current time
        """

        self.updated_at = datetime.datetime.utcnow()
        models.storage.save()

    def to_dict(self):

        """Return dictionary containing all keys/values
        """

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        return my_dict

    def __str__(self):

        """print all information in string
        """

        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
