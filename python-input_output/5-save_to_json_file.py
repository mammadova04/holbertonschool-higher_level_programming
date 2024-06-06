#!/usr/bin/python3
"""JSON"""
import json


def save_to_json_file(my_obj, filename):
    """JSON -> text -> file"""
    with open(filename, 'w') as fd:
        fd.write(json.dumps(my_obj))
