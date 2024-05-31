#!/usr/bin/pyhton3
"""This module returns True if the object is \
exactly an instancce of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """Check if true or not"""

    return type(obj) is a_class
