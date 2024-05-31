#!/usr/bin/python3
"""Thid module Only sub claass of return"""


def inherits_from(obj, a_class):
    """
    Args:
    obj: An object to check.
    a_class: A class to compare obj against.
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
