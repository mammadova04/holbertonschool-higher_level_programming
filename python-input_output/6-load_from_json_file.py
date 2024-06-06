#!/usr/bin/python3
"""JSON"""
import json


def load_from_json_file(filename):
    """JSON -> text -> file"""
    with open(filename, 'r') as fd:
        return json.loads(fd.read())
