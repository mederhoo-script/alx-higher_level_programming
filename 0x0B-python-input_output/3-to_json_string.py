#!/usr/bin/python3
"""define a function that return json"""
import json


def to_json_string(my_obj):
    """function that return json

    Args:
        my_obj: str that return as json

    Return: JSON
        """
    return json.dumps(my_obj)
