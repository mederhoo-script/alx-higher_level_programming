#!/usr/bin/python3
"""base module parent class start here"""


class Base:
    """Base class for parent class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """contructor for parent class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
