#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """append to a file"""
    with open(filename, 'a', encoding="utf-8") as fd:
        return fd.write(text)
