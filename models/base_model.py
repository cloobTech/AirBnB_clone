#!/usr/bin/env python3
"""
A script that defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ defines all common attributes/methods for other classes """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.now()

    def __str__(self):
        cls_str = f"[{type(self).__name__}] ({type(self.id)}){self.__dict__}"
        return (cls_str)
